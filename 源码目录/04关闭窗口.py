# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019/11/19 15:54
# 文件名称: 04关闭窗口.py
# 开发工具: PyCharm

import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QToolTip
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont


class LxgApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建退出按钮
        qbtn = QPushButton("退出", self)
        # 添加点击事件为退出事件
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        # 设置大小和位置
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 50)
        # 设置窗口的大小和位置
        self.setGeometry(300, 300, 250, 150)
        # 设置窗口标题
        self.setWindowTitle("点击退出")
        # 设置窗口图标
        self.setWindowIcon(QIcon("favicon.ico"))
        # 设置退出按钮提示
        QToolTip.setFont(QFont("sansSerif", 10))
        qbtn.setToolTip("点击退出程序")
        # 显示窗口
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    lxg = LxgApp()
    sys.exit(app.exec_())
