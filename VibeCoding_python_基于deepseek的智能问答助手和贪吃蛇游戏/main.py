import sys
import os
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                             QHBoxLayout, QTextEdit, QLineEdit, QPushButton,
                             QLabel, QMessageBox)
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtGui import QFont, QTextCursor

# 尝试导入 openai 库，若未安装则提示
try:
    from openai import OpenAI
except ImportError:
    # 必须先创建 QApplication 才能显示对话框
    _app = QApplication(sys.argv)
    QMessageBox.critical(None, "缺少依赖", "请先安装 openai 库：\npip install openai")
    sys.exit(1)

# ================== 配置信息 ==================
# 请在此处填入你的 DeepSeek API Key，或设置环境变量 DEEPSEEK_API_KEY
DEEPSEEK_API_KEY = os.environ.get("DEEPSEEK_API_KEY", "sk-e2b7a473c79d4911904fc83868cb3183")
DEEPSEEK_BASE_URL = "https://api.deepseek.com/v1"
MODEL_NAME = "deepseek-chat"          # DeepSeek-V3 模型

# 检查 API Key 是否有效
if DEEPSEEK_API_KEY == "your-api-key-here":
    print("警告：未设置有效的 DeepSeek API Key，请修改代码中的 DEEPSEEK_API_KEY 或设置环境变量。")
    # 程序仍可启动，但调用 API 时会报错


# ================== 工作线程 ==================
class ChatWorker(QThread):
    """与 DeepSeek API 通信的工作线程，避免阻塞 UI"""
    finished = pyqtSignal(str)   # 成功时返回助手回复
    error = pyqtSignal(str)      # 失败时返回错误信息

    def __init__(self, messages, api_key, base_url, model):
        super().__init__()
        self.messages = messages      # 对话历史列表，每个元素是 {"role": "user/assistant", "content": "..."}
        self.api_key = api_key
        self.base_url = base_url
        self.model = model

    def run(self):
        try:
            # 创建 OpenAI 客户端（兼容 DeepSeek）
            client = OpenAI(api_key=self.api_key, base_url=self.base_url)


            response = client.chat.completions.create(
                model=self.model,
                messages=self.messages,
                stream=False,          # 不使用流式，简单起见
                temperature=0.7,
                max_tokens=2048,
            )

            # 提取回复内容
            reply = response.choices[0].message.content
            self.finished.emit(reply)

        except Exception as e:
            error_msg = f"API 请求失败：{str(e)}"
            self.error.emit(error_msg)


# ================== 主窗口 ==================
class CustomerServiceWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("智能客服助手")
        # 设置窗口大小限制
        self.setMinimumSize(800, 600)
        self.resize(800, 800)

        # 对话历史，存储格式：{"role": "user/assistant", "content": "..."}
        self.history = []

        # 最大保留消息数量（用户+助手），避免 token 过多
        self.max_history_length = 20

        # 工作线程引用
        self.worker = None

        # 创建 UI
        self.init_ui()

        # 显示欢迎消息
        self.append_system_message("欢迎使用智能客服！请输入您的问题。")

    def init_ui(self):
        """初始化界面布局"""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        layout.setSpacing(10)

        # 标题标签
        title_label = QLabel("智能客服聊天室")
        title_label.setAlignment(Qt.AlignCenter)
        title_font = QFont("微软雅黑", 16, QFont.Bold)
        title_label.setFont(title_font)
        layout.addWidget(title_label)

        # 聊天显示区域（只读）
        self.chat_display = QTextEdit()
        self.chat_display.setReadOnly(True)
        self.chat_display.setFont(QFont("微软雅黑", 12))
        self.chat_display.setStyleSheet("background-color: #f8f9fa; border: 1px solid #ddd;")
        layout.addWidget(self.chat_display)

        # 输入区域（水平布局）
        input_layout = QHBoxLayout()
        self.input_edit = QLineEdit()
        self.input_edit.setPlaceholderText("请输入您的问题，按 Enter 发送...")
        self.input_edit.setFont(QFont("微软雅黑", 10))
        self.input_edit.returnPressed.connect(self.send_message)   # 回车发送

        self.send_btn = QPushButton("发送")
        self.send_btn.setFont(QFont("微软雅黑", 12))
        self.send_btn.clicked.connect(self.send_message)

        # 清空历史按钮
        self.clear_btn = QPushButton("清空对话")
        self.clear_btn.setFont(QFont("微软雅黑", 12))
        self.clear_btn.clicked.connect(self.clear_history)

        input_layout.addWidget(self.input_edit)
        input_layout.addWidget(self.send_btn)
        input_layout.addWidget(self.clear_btn)
        layout.addLayout(input_layout)

        # 状态栏
        self.statusBar().showMessage("就绪")

    def append_message(self, role, content):
        """向聊天显示区域追加一条消息（角色：我 / 客服 / 系统）"""
        if role == "user":
            prefix = "👤 我："
            color = "#007bff"
        elif role == "assistant":
            prefix = "🤖 客服："
            color = "#28a745"
        else:  # system
            prefix = "ℹ️ 系统："
            color = "#6c757d"

        # 格式化显示
        display_text = f'<p style="margin:5px 0;"><b style="color:{color};">{prefix}</b> {content}</p>'
        self.chat_display.append(display_text)
        # 滚动到底部
        scrollbar = self.chat_display.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())

    def append_system_message(self, content):
        """显示系统消息（例如欢迎语、错误提示）"""
        self.append_message("system", content)

    def add_to_history(self, role, content):
        """将一条消息加入历史记录，并自动裁剪超出长度的旧消息"""
        self.history.append({"role": role, "content": content})
        # 如果历史超过最大长度，删除最早的消息（保留最近的）
        if len(self.history) > self.max_history_length:
            self.history = self.history[-self.max_history_length:]

    def send_message(self):
        """处理用户发送消息"""
        user_input = self.input_edit.text().strip()
        if not user_input:
            return

        # 禁用输入控件，防止重复发送
        self.set_controls_enabled(False)

        # 显示用户消息并加入历史
        self.append_message("user", user_input)
        self.add_to_history("user", user_input)

        # 清空输入框
        self.input_edit.clear()

        # 显示“正在思考...”的临时提示
        self.statusBar().showMessage("客服正在思考中，请稍候...")
        self.append_system_message("客服正在输入...")  # 临时提示

        # 创建并启动工作线程（传入当前历史的副本，避免后续修改影响线程）
        # 注意：工作线程内部不会修改这个列表，因此直接传递引用是安全的
        self.worker = ChatWorker(
            messages=self.history.copy(),
            api_key=DEEPSEEK_API_KEY,
            base_url=DEEPSEEK_BASE_URL,
            model=MODEL_NAME
        )
        self.worker.finished.connect(self.on_reply_received)
        self.worker.error.connect(self.on_api_error)
        self.worker.start()

    def remove_last_block(self):
        """删除聊天框中最后一个段落（用于移除"正在输入..."临时提示）"""
        cursor = self.chat_display.textCursor()
        cursor.movePosition(QTextCursor.End)
        cursor.select(QTextCursor.BlockUnderCursor)
        # 连同前面的换行符一起删除
        cursor.movePosition(QTextCursor.EndOfBlock, QTextCursor.MoveAnchor)
        cursor.movePosition(QTextCursor.StartOfBlock, QTextCursor.KeepAnchor)
        # 向前扩展一个字符以包含段落分隔符
        cursor.movePosition(QTextCursor.PreviousCharacter, QTextCursor.KeepAnchor)
        cursor.removeSelectedText()

    def on_reply_received(self, reply):
        """API 成功返回时的处理"""
        # 删除"正在输入..."临时提示，替换为真实回复
        self.remove_last_block()
        self.append_message("assistant", reply)
        self.add_to_history("assistant", reply)

        self.statusBar().showMessage("回复完成", 3000)
        self.set_controls_enabled(True)

    def on_api_error(self, error_msg):
        """API 出错时的处理"""
        # 删除"正在输入..."临时提示，显示错误信息
        self.remove_last_block()
        self.append_system_message(f"错误：{error_msg}")
        self.statusBar().showMessage("请求失败，请检查网络或 API Key", 5000)

        # 注意：用户消息已经加入历史，但回复失败，可以保留让用户重新发送或手动修改。
        # 启用控件，让用户可以继续尝试
        self.set_controls_enabled(True)

    def clear_history(self):
        """清空对话历史及显示区域"""
        self.history.clear()
        self.chat_display.clear()
        self.append_system_message("对话历史已清空，开始新的交流。")
        self.statusBar().showMessage("已清空历史", 2000)

    def set_controls_enabled(self, enabled):
        """启用/禁用输入框和发送按钮，防止并发请求"""
        self.input_edit.setEnabled(enabled)
        self.send_btn.setEnabled(enabled)
        self.clear_btn.setEnabled(enabled)  # 清空按钮在请求期间也可以禁用，避免混乱
        if not enabled:
            self.input_edit.setFocus()
        else:
            self.input_edit.setFocus()

    def closeEvent(self, event):
        """窗口关闭时，如果线程还在运行则等待其结束"""
        if self.worker and self.worker.isRunning():
            self.worker.quit()
            self.worker.wait(1000)
        event.accept()


# ================== 程序入口 ==================
if __name__ == "__main__":
    app = QApplication(sys.argv)
    #实例化窗口
    window = CustomerServiceWindow()
    #显示窗口
    window.show()
    sys.exit(app.exec_())