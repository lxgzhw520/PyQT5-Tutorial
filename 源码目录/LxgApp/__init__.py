# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019/11/20 16:11
# 文件名称: __init__.py.py
# 开发工具: PyCharm

import sys
import os
from PyQt5.QtWidgets import QMainWindow, QMenu, QAction, qApp, QApplication
from PyQt5.QtWidgets import QMessageBox, QToolTip, QPushButton, QDesktopWidget
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon, QFont

BASE_DIR = os.path.abspath(__file__)


# 主程序
class LxgApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("favicon.ico"))
        self.setWindowTitle("理想国真恵玩")
        self.resize(800, 600)
        self.center()
        # self.show()

    # 退出事件
    def closeEvent(self, event, *args, **kwargs):
        isExist = QMessageBox.question(
            self, "退出确认", "您确定要退出程序吗?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )
        if isExist == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    # 居中
    def center(self):
        frame = self.frameGeometry()
        screenCenter = QDesktopWidget().availableGeometry().center()
        frame.moveCenter(screenCenter)
        self.move(frame.topLeft())


if __name__ == '__main__':
    print(BASE_DIR)
