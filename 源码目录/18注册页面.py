# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019/11/20 19:49
# 文件名称: 17登录界面.py
# 开发工具: PyCharm

import sys
from PyQt5.QtWidgets import (
    QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout, QApplication,
    QToolTip, QPushButton
)
from PyQt5.QtGui import (
    QIcon, QFont,
)


class LxgApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont("sansSerif", 12))
        # 创建栅格布局
        grid = QGridLayout()
        grid.setSpacing(10)

        # 用户名
        username = QLabel("用户名")
        usernameEdit = QLineEdit()
        grid.addWidget(username, 1, 0)
        grid.addWidget(usernameEdit, 1, 1)

        # 密码
        password = QLabel("密码")
        passwordEdit = QLineEdit()
        grid.addWidget(password, 2, 0)
        grid.addWidget(passwordEdit, 2, 1)

        # 确认密码
        password1 = QLabel("确认密码")
        password1Edit = QLineEdit()
        grid.addWidget(password1, 3, 0)
        grid.addWidget(password1Edit, 3, 1)

        # 登录按钮
        loginButton = QPushButton("登录")
        loginButton.setToolTip("点击登录")
        grid.addWidget(loginButton, 4, 1)

        # 设置窗口布局
        self.setLayout(grid)

        # 窗口
        self.setWindowIcon(QIcon("favicon.ico"))
        self.setWindowTitle("用户登录")
        self.resize(300, 200)
        self.move(300, 300)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    lxg = LxgApp()
    sys.exit(app.exec_())
