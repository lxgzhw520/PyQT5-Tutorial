# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019/11/19 16:11
# 文件名称: 05消息盒子.py
# 开发工具: PyCharm

import sys
from PyQt5.QtWidgets import (QWidget, QMessageBox, QApplication,
                             QPushButton, QToolTip)
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QFont, QIcon


class LxgApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置提示框的字体
        QToolTip.setFont(QFont("sansSerif", 12))
        # 创建一个关闭按钮
        qbtn = QPushButton("退出", self)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 50)

        # 创建窗口
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle("演示消息盒子")
        self.setWindowIcon(QIcon("favicon.ico"))
        self.setToolTip("退出事件")
        self.show()

    def closeEvent(self, event):
        """退出事件"""
        reply = QMessageBox.question(self, "消息",
                                     "您确定要退出吗?",
                                     QMessageBox.Yes |
                                     QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    lxg = LxgApp()
    sys.exit(app.exec_())
