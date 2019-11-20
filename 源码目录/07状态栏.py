# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019/11/19 16:54
# 文件名称: 07状态栏.py
# 开发工具: PyCharm

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtWidgets import QMessageBox, QToolTip
from PyQt5.QtWidgets import QPushButton, QDesktopWidget
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon, QFont


class LxgApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建提示框的字体
        QToolTip.setFont(QFont("sansSerif", 12))

        # 创建退出按钮并添加退出事件
        qbtn = QPushButton("退出", self)
        qbtn.setToolTip("点击按钮退出程序")
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 50)
        qbtn.clicked.connect(QCoreApplication.instance().quit)

        # 状态栏
        # 设置图标,标题,显示窗口
        self.setWindowIcon(QIcon("favicon.ico"))
        self.setWindowTitle("演示状态栏")
        self.statusBar().showMessage("状态栏")
        self.resize(250, 150)
        self.center()
        self.show()

    def closeEvent(self, event):
        reply = QMessageBox.question(
            self, "退出确认", "您确定要退出吗?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.Yes
        )
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def center(self):
        # 本窗口
        qr = self.frameGeometry()
        # 居中窗口
        cp = QDesktopWidget().availableGeometry().center()
        # 移动本窗口到居中窗口的中心
        qr.moveCenter(cp)
        # 左上角
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    lxg = LxgApp()
    sys.exit(app.exec_())
