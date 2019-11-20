# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019/11/19 19:52
# 文件名称: 09子菜单.py
# 开发工具: PyCharm

import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtWidgets import QMessageBox, QToolTip, QPushButton
from PyQt5.QtWidgets import QDesktopWidget, QMenu
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon, QFont


class LxgApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 提示框和退出按钮
        QToolTip.setFont(QFont("sansSerif", 12))
        exitButton = QPushButton("退出", self)
        exitButton.setToolTip("点击按钮,退出程序")
        exitButton.clicked.connect(QCoreApplication.instance().quit)
        exitButton.resize(exitButton.sizeHint())
        exitButton.move(50, 50)
        # 设置图标和标题
        self.setWindowIcon(QIcon("favicon.ico"))
        self.setWindowTitle("演示子菜单的使用")

        # 设置状态栏
        self.statusBar().showMessage("状态栏")

        # 设置菜单
        # 动作
        exitAction = QAction(QIcon("退出.png"), '&退出', self)
        exitAction.setShortcut("Ctrl+Q")
        exitAction.setStatusTip("退出程序")
        exitAction.triggered.connect(qApp.quit)
        # 菜单栏
        menubar = self.menuBar()
        fileMenu = menubar.addMenu("&文件")
        fileMenu.addAction(exitAction)

        # 子菜单
        impMenu = QMenu("导入", self)
        impAction = QAction("导入邮箱", self)
        impMenu.addAction(impAction)

        # 菜单
        newAction = QAction("新建", self)
        fileMenu.addAction(newAction)
        fileMenu.addMenu(impMenu)

        # 展示窗口
        self.resize(800, 600)
        self.center()
        self.show()

    # 窗口居中
    def center(self):
        frame = self.frameGeometry()
        screenCenter = QDesktopWidget().availableGeometry().center()
        frame.moveCenter(screenCenter)
        self.move(frame.topLeft())

    # 监听退出事件
    def closeEvent(self, event):
        isExit = QMessageBox.question(
            self, "退出确认", "您确定要退出程序吗?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )
        if isExit == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    lxg = LxgApp()
    sys.exit(app.exec_())
