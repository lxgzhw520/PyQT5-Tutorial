# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019/11/20 16:41
# 文件名称: 13绝对定位.py
# 开发工具: PyCharm
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget, QLabel
from LxgApp import LxgApp


class App(LxgApp):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label1 = QLabel("理想国", self)
        label1.move(33, 10)
        label2 = QLabel("真恵玩", self)
        label2.move(66, 30)
        label3 = QLabel("张大鹏", self)
        label3.move(99, 60)
        self.setWindowTitle("绝对定位")
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    lxg = App()
    sys.exit(app.exec_())
