# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019/11/20 16:08
# 文件名称: 13主窗口.py
# 开发工具: PyCharm

import sys
from PyQt5.QtWidgets import QMainWindow, QMenu, QAction, qApp, QApplication
from PyQt5.QtWidgets import QMessageBox, QToolTip, QPushButton, QDesktopWidget
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon, QFont

from LxgApp import LxgApp


# 主程序
class App(LxgApp):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("演示主窗口的使用")
        # 编辑框
        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)
        # 添加菜单栏
        self.getMenuBar()
        # 添加工具栏
        toolbar = self.addToolBar("退出")
        toolbar.addAction(self.getExitAction())
        # 添加状态栏
        self.getStatusBar()

    # 获取状态栏
    def getStatusBar(self):
        self.statusBar().showMessage("状态栏")

    # 获取菜单
    def getMenuBar(self):
        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu("&文件")
        fileMenu.addAction(self.getExitAction())

    # 退出动作
    def getExitAction(self):
        exitAction = QAction(QIcon("exit.png"), "退出", self)
        exitAction.setShortcut("Ctrl+Q")
        exitAction.setStatusTip("退出程序")
        exitAction.triggered.connect(self.close)
        return exitAction


# 测试
if __name__ == '__main__':
    app = QApplication(sys.argv)
    lxg = App()
    sys.exit(app.exec_())
