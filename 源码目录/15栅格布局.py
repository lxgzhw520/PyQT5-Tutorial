# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019/11/20 19:28
# 文件名称: 15栅格布局.py
# 开发工具: PyCharm
import sys
from PyQt5.QtWidgets import (
    QWidget, QGridLayout, QPushButton, QApplication)


class LxgApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置布局为栅格布局
        grid = QGridLayout()
        self.setLayout(grid)

        names = ['重置', '删除', '', '关闭',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']

        # i代表行,j代表列 这是一个嵌套循环
        positions = [(i, j) for i in range(5) for j in range(4)]

        for position, name in zip(positions, names):
            print(position, name)
            if name == '':
                continue
            button = QPushButton(name)
            grid.addWidget(button, *position)

        self.move(300, 150)
        self.setWindowTitle("计算器")
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    lxg = LxgApp()
    sys.exit(app.exec_())
