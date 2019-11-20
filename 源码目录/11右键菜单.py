# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019/11/20 12:42
# 文件名称: 11右键菜单.py
# 开发工具: PyCharm

import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtWidgets import QMessageBox, QToolTip, QPushButton
from PyQt5.QtWidgets import QDesktopWidget, QMenu
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon, QFont


# 主程序
class LxgApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置图标和标题
        self.setWindowIcon(QIcon("favicon.ico"))
        self.setWindowTitle("演示右键菜单")

        # 设置按钮,绑定退出事件,设置提示框
        exitButton = QPushButton("退出", self)
        exitButton.setToolTip("点击按钮退出程序")
        exitButton.resize(exitButton.sizeHint())
        exitButton.move(50, 50)
        exitButton.clicked.connect(QCoreApplication.instance().exit)

        # 设置状态栏
        self.statusBar().showMessage("状态栏")

        menuBar = self.menuBar()

        # 设置一级菜单
        exitAction = QAction(QIcon("退出.png"), '&退出', self)
        exitAction.setShortcut("Ctrl+Q")
        exitAction.setStatusTip("退出程序")
        exitAction.triggered.connect(qApp.quit)
        fileMenu = menuBar.addMenu("&文件")
        # 设置二级菜单
        newMenu = QMenu("新建", self)
        newPythonFile = QAction("新建Python文件", self)
        newMenu.addAction(newPythonFile)

        # 将一级菜单和二级菜单添加到文件按钮下
        fileMenu.addMenu(newMenu)
        fileMenu.addAction(exitAction)

        self.resize(800, 600)
        self.center()
        self.show()

    # 菜单栏右键菜单
    def contextMenuEvent(self, QContextMenuEvent):
        rightClickMenu = QMenu(self)
        newAction = rightClickMenu.addAction("新建")
        openAction = rightClickMenu.addAction("打开")
        quitAction = rightClickMenu.addAction("退出")
        # 监听点击动作绑定的事件
        action = rightClickMenu.exec_(self.mapToGlobal(QContextMenuEvent.pos()))
        if action == quitAction:
            qApp.quit()

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

    # 窗口居中
    def center(self):
        frame = self.frameGeometry()
        screenCenter = QDesktopWidget().availableGeometry().center()
        frame.moveCenter(screenCenter)
        self.move(frame.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    lxg = LxgApp()
    sys.exit(app.exec_())
