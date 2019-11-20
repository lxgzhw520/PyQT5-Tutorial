# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019/11/19 17:36
# 文件名称: 08菜单栏.py
# 开发工具: PyCharm

import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtWidgets import QMessageBox, QToolTip, QPushButton
from PyQt5.QtWidgets import QDesktopWidget
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon, QFont


class LxgApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置提示框字体
        QToolTip.setFont(QFont("sansSerif", 12))
        # 添加按钮,监听退出事件,设置提示
        qbtn = QPushButton("退出", self)
        qbtn.setToolTip("点击按钮退出程序")
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        # 设置按钮的大小,位置
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 50)
        # 设置图标,标题
        self.setWindowIcon(QIcon("favicon.ico"))
        self.setWindowTitle("演示菜单栏")

        # 设置状态栏
        self.statusBar().showMessage("状态栏")
        # 设置菜单栏
        exitAct = QAction(QIcon("退出.png"), '&退出', self)
        exitAct.setShortcut("Ctrl+Q")
        exitAct.setStatusTip("退出程序")
        exitAct.triggered.connect(qApp.quit)

        self.statusBar()
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&文件')
        fileMenu.addAction(exitAct)

        # 设置居中
        self.resize(800, 600)
        self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    # 监听退出事件
    def closeEvent(self, event):
        reply = QMessageBox.question(
            self, "退出确认", "您确定要退出吗?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    lxg = LxgApp()
    sys.exit(app.exec_())
