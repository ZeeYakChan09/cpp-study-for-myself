# C++ Self-Study & Project Portfolio
本项目主要记录了我从零基础到进阶的 C 学习历程、核心算法与数据结构的实现，以及围绕计算机视觉（OpenCV）、系统设计等领域的实战项目。
---

## 🚀 项目概览 (Project Portfolio)

仓库内主要包含以下核心实战项目：

### 1. 📂 学生信息管理系统 (Student Information Management System)
* **开发环境**：CLion, Git, C/C++
* **核心技术**：面向对象编程 (OOP)、结构体与类设计、文件输入输出流 (fstream)、指针与动态链表/数组。
* **功能特点**：
  * 实现了学生数据的增删改查 (CRUD) 核心逻辑。
  * 支持数据的持久化存储（本地文件读写），确保程序退出后数据不丢失。
  * 优化了健壮性，具备基础的输入校验与异常处理机制。
* **收获**：深刻理解了 C++ 的内存管理、文件指针操作，以及如何使用 Git 进行版本控制与代码迭代。

### 2. 👁️ 计算机视觉实战项目 (基于 OpenCV)
利用 C++ 结合 OpenCV 库开发了三个有趣且实用的图像与视频处理项目，深入探索了数字图像处理的基础算法：

* **📷 证件照自动换底 (ID Photo Background Changer)**
  * **实现原理**：通过颜色空间转换（如 RGB 转 HSV），精准提取背景颜色掩膜（Mask），结合图像形态学处理（腐蚀、膨胀）平滑边缘，最后进行像素级的背景融合。
* **🖼️ 静态图像“隐身术” (Static Image Invisibility Cloak)**
  * **实现原理**：利用动态背景建模或预存背景图，检测特定颜色（如绿色/蓝色斗篷）的 ROI 区域，并通过掩膜覆盖技术，将背景像素实时替换到该区域，达到“隐身”效果。
* **🎥 视频动态“隐身术” (Video Invisibility Cloak)**
  * **实现原理**：基于静态图像隐身术延伸至视频流。逐帧读取视频，利用颜色分量识别特定遮挡物，结合多线程或帧率优化，实现流畅的动态“哈利波特隐形斗篷”视觉特效。

---

## 🛠️ 技术栈 (Tech Stack)

* **编程语言**：C++, C
* **开发工具**：CLion, CMake, GCC/G++, Git
* **核心库**：OpenCV (Computer Vision)
* **核心领域**：面向对象设计、文件 IO、数字图像处理、基础数据结构与算法

---

## 📂 目录结构 (Directory Structure)

```text
├── StudentManagementSystem/   # 学生信息管理系统源码
├── OpenCV-Projects/           # OpenCV 计算机视觉项目
│   ├── ID_Photo_Changer/      # 证件照换底
│   ├── Static_Invisibility/   # 静态图像隐身术
│   └── Video_Invisibility/    # 视频动态隐身术
└── README.md                  # 项目说明文档
