# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019/11/20 14:58
# 文件名称: 12工具栏.py
# 开发工具: PyCharm

import sys
from PyQt5.QtWidgets import QMainWindow, QMenu, QAction, qApp, QApplication
from PyQt5.QtWidgets import QMessageBox, QToolTip, QPushButton, QDesktopWidget
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon, QFont


# 主程序
class LxgApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置窗口图标和窗口标题
        self.setWindowTitle("展示工具栏的使用")
        self.setWindowIcon(QIcon("favicon.ico"))

        # 设置提示框字体和大小,添加按钮,绑定提示框和退出事件
        QToolTip.setFont(QFont("sansSerif", 12))
        exitButton = QPushButton("退出", self)
        exitButton.setFont(QFont("sansSerif", 24))
        exitButton.setToolTip("点击退出程序")
        exitButton.resize(exitButton.sizeHint())
        exitButton.move(400, 300)
        exitButton.clicked.connect(QApplication.instance().quit)

        # 设置状态栏
        self.statusBar().showMessage("状态栏")

        # 添加文件->新建->新建Python文件菜单
        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu("&文件")
        fileMenu.addMenu(self.newMenu())

        # 添加文件->退出菜单
        fileMenu.addAction(self.exitAction())

        # 添加工具栏
        self.toolbar = self.addToolBar("退出")
        self.toolbar.addAction(self.exitAction())
        
        self.resize(800, 600)
        self.center()
        self.show()

    # 鼠标右键菜单
    def contextMenuEvent(self, QContextMenuEvent):
        rightClickMenu = QMenu(self)
        newMenu = rightClickMenu.addAction("新建")
        exitAction = rightClickMenu.addAction("退出")
        exitAction1 = rightClickMenu.addAction(self.exitAction())

        # 监听点击事件
        # 右键菜单,这才是关键
        action = rightClickMenu.exec_(self.mapToGlobal(QContextMenuEvent.pos()))
        if action == exitAction:
            qApp.quit()

    # 新建菜单
    def newMenu(self):
        menu = QMenu("新建", self)
        pythonFile = QAction("新建Python文件", self)
        menu.addAction(pythonFile)
        return menu

    # 退出动作
    def exitAction(self):
        exitAction = QAction(QIcon("退出.png"), '&退出', self)
        exitAction.setShortcut("Ctrl+Q")
        exitAction.setStatusTip("退出程序")
        exitAction.triggered.connect(qApp.quit)
        return exitAction

    # 居中
    def center(self):
        frame = self.frameGeometry()
        screenCenter = QDesktopWidget().availableGeometry().center()
        frame.moveCenter(screenCenter)
        self.move(frame.topLeft())


# 测试
if __name__ == '__main__':
    app = QApplication(sys.argv)
    lxg = LxgApp()
    sys.exit(app.exec_())
