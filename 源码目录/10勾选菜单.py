# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019/11/19 20:47
# 文件名称: 10勾选菜单.py
# 开发工具: PyCharm
import sys
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QApplication
from PyQt5.QtWidgets import QMessageBox, QPushButton, QToolTip
from PyQt5.QtWidgets import QAction, qApp, QMenu
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication


class LxgApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置按钮和提示框
        QToolTip.setFont(QFont("sansSerif", 12))
        exitButton = QPushButton("退出", self)
        exitButton.setToolTip("点击按钮退出程序")

        # 设置大小和位置
        exitButton.resize(exitButton.sizeHint())
        exitButton.move(50, 50)
        # 点击按钮退出
        exitButton.clicked.connect(QCoreApplication.instance().quit)

        # 设置图标和标题
        self.setWindowIcon(QIcon("favicon.ico"))
        self.setWindowTitle("演示勾选菜单")
        # 状态栏
        self.statusBar().showMessage("状态栏")

        # 添加一级菜单
        exitAction = QAction(QIcon("退出.png"), "&退出", self)
        exitAction.setShortcut("Ctrl+Q")
        exitAction.setStatusTip("退出程序")
        exitAction.triggered.connect(qApp.quit)
        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu("&文件")
        fileMenu.addAction(exitAction)
        # 添加二级菜单
        impMenu = QMenu("导入", self)
        impAction = QAction("导入邮箱", self)
        impMenu.addAction(impAction)
        fileMenu.addMenu(impMenu)

        # 勾选菜单
        viewMenu = menuBar.addMenu("查看")
        viewStatAct = QAction("查看状态栏", self)
        viewStatAct.setCheckable(True)
        viewStatAct.setChecked(True)
        viewStatAct.setStatusTip("查看状态栏")
        viewStatAct.triggered.connect(self.toggleMenu)
        viewMenu.addAction(viewStatAct)

        # 显示窗口
        self.resize(800, 600)
        self.center()
        self.show()

    def toggleMenu(self, state):
        if state:
            self.statusbar.show()
        else:
            self.statusbar.hide()

    def center(self):
        frame = self.frameGeometry()
        screenCenter = QDesktopWidget().availableGeometry().center()
        frame.moveCenter(screenCenter)
        self.move(frame.topLeft())

    # 关闭监听
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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    lxg = LxgApp()
    sys.exit(app.exec_())
