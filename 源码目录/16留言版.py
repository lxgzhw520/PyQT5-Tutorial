# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019/11/20 19:40
# 文件名称: 16留言版.py
# 开发工具: PyCharm

import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
    QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout, QApplication
)


class LxgApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("留言板")
        self.setWindowIcon(QIcon("favicon.ico"))
        # 三个提示文本
        title = QLabel("标题")
        author = QLabel("作者")
        review = QLabel("留言")
        # 三个输入框
        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        reviewEdit = QTextEdit()

        # 创建栅格布局
        grid = QGridLayout()
        grid.setSpacing(10)

        # 将组建添加到栅格中
        grid.addWidget(title, 1, 0)
        grid.addWidget(author, 2, 0)
        grid.addWidget(review, 3, 0)
        grid.addWidget(titleEdit, 1, 1)
        grid.addWidget(authorEdit, 2, 1)
        grid.addWidget(reviewEdit, 3, 1, 5, 1)

        # 设置布局
        self.setLayout(grid)
        self.resize(800, 600)
        self.move(300, 300)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    lxg = LxgApp()
    sys.exit(app.exec_())
