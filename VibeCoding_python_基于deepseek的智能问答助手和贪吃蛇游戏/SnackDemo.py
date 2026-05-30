import sys
import random
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPainter, QColor, QPen


# ==========================================
# 稳定性配置：防止 PyQt 闪退吞掉错误日志
# ==========================================
def traceback_excepthook(type, value, tback):
    sys.__excepthook__(type, value, tback)


sys.excepthook = traceback_excepthook

# ==========================================
# 游戏核心配置常量
# ==========================================
GRID_SIZE = 20  # 每个网格的像素大小
GRID_COUNT = 25  # 地图网格数量 (25x25)
BOARD_SIZE = GRID_SIZE * GRID_COUNT  # 窗口实际显示区域大小 (500x500)


class SnakeGame(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.init_game()

    def init_ui(self):
        """初始化纯黑白视觉界面"""
        self.setWindowTitle('Snake - Minimalist')
        self.setFixedSize(BOARD_SIZE, BOARD_SIZE)
        # 设置窗口背景为纯黑
        self.setStyleSheet("background-color: black;")
        self.show()

    def init_game(self):
        """初始化或重置游戏数据"""
        # 蛇的初始位置（网格坐标），身体由一组坐标元组组成
        self.snake = [(12, 12), (12, 13), (12, 14)]
        # 初始移动方向：向上
        self.direction = Qt.Key_Up

        # 计时器：控制蛇的移动速度（单位：毫秒）
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.game_loop)
        self.timer.start(150)  # 150ms 走一步

        # 游戏状态
        self.game_over = False
        self.score = 0

        # 生成第一个食物
        self.spawn_food()

    def spawn_food(self):
        """在随机空白网格生成食物"""
        while True:
            self.food = (random.randint(0, GRID_COUNT - 1), random.randint(0, GRID_COUNT - 1))
            # 确保食物不会生成在蛇的身体上
            if self.food not in self.snake:
                break

    def keyPressEvent(self, event):
        """处理键盘输入，防止直接掉头"""
        key = event.key()
        if key == Qt.Key_Left and self.direction != Qt.Key_Right:
            self.direction = key
        elif key == Qt.Key_Right and self.direction != Qt.Key_Left:
            self.direction = key
        elif key == Qt.Key_Up and self.direction != Qt.Key_Down:
            self.direction = key
        elif key == Qt.Key_Down and self.direction != Qt.Key_Up:
            self.direction = key
        # 游戏结束后，按下空格键重新开始
        elif key == Qt.Key_Space and self.game_over:
            self.init_game()

    def game_loop(self):
        """游戏主逻辑循环"""
        if self.game_over:
            return

        # 1. 计算新蛇头的位置
        head_x, head_y = self.snake[0]
        if self.direction == Qt.Key_Left:
            head_x -= 1
        elif self.direction == Qt.Key_Right:
            head_x += 1
        elif self.direction == Qt.Key_Up:
            head_y -= 1
        elif self.direction == Qt.Key_Down:
            head_y += 1

        new_head = (head_x, head_y)

        # 2. 边界与自身碰撞检测
        if (head_x < 0 or head_x >= GRID_COUNT or
                head_y < 0 or head_y >= GRID_COUNT or
                new_head in self.snake):
            self.game_over = True
            self.timer.stop()
            self.update()  # 触发重绘以显示 Game Over
            return

        # 3. 移动与进食逻辑
        self.snake.insert(0, new_head)  # 前进：在头部插入新坐标

        if new_head == self.food:
            self.score += 1
            self.spawn_food()  # 吃到食物：不删尾部（身体变长），生成新食物
        else:
            self.snake.pop()  # 没吃到食物：弹出尾部（保持原长）

        # 4. 刷新屏幕
        self.update()

    def paintEvent(self, event):
        """画布渲染（标准的 self, event 传参）"""
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # 如果游戏结束，绘制全屏提示
        if self.game_over:
            painter.setPen(QPen(Qt.white))
            # 设置一个稍微大一点的系统字体
            font = self.font()
            font.setPointSize(14)
            painter.setFont(font)
            painter.drawText(self.rect(), Qt.AlignCenter,
                             f"GAME OVER\n\nScore: {self.score}\n\nPress SPACE to Restart")
            return

        # 设置纯白画笔和无边框填充
        white_brush = QColor(255, 255, 255)
        painter.setBrush(white_brush)
        painter.setPen(Qt.NoPen)

        # 1. 绘制蛇身（满格白方块，留1px间隙）
        for x, y in self.snake:
            painter.drawRect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE - 1, GRID_SIZE - 1)

        # 2. 绘制食物（缩进3px的小白方块，视觉上与蛇区分）
        fx, fy = self.food
        padding = 3
        painter.drawRect(
            fx * GRID_SIZE + padding,
            fy * GRID_SIZE + padding,
            GRID_SIZE - padding * 2,
            GRID_SIZE - padding * 2
        )


if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = SnakeGame()
    sys.exit(app.exec_())