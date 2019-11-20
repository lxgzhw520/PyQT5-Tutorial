# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019/11/20 19:17
# 文件名称: 14盒子布局.py
# 开发工具: PyCharm

import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
                             QHBoxLayout, QVBoxLayout, QApplication)
from LxgApp import LxgApp


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        okButton = QPushButton("确认")
        cancelButton = QPushButton("取消")
        # 创建水平布局盒子
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        # 创建垂直布局盒子
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        # 设置布局
        self.setLayout(vbox)

        self.resize(800, 600)
        self.move(300, 300)
        self.setWindowTitle("理想国真恵玩")
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    lxg = App()
    sys.exit(app.exec_())
