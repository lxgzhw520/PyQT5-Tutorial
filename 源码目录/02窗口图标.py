# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019/11/19 15:09
# 文件名称: 02窗口图标.py
# 开发工具: PyCharm

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


class Lxg(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle("理想国真恵玩")
        self.setWindowIcon(QIcon("favicon.ico"))
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    lxg = Lxg()
    sys.exit(app.exec_())
