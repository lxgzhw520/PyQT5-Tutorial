# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019/11/19 15:37
# 文件名称: 03提示框.py
# 开发工具: PyCharm
import sys
from PyQt5.QtWidgets import (QWidget, QToolTip,
                             QPushButton, QApplication)
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QIcon


class LxgApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 字体
        QToolTip.setFont(QFont("sansSerif", 10))
        # 继承自父类
        self.setToolTip("这是一个<b>QWidget</b>组件")
        # 创建按钮
        btn = QPushButton("按钮", self)
        btn.setToolTip("这是一个<i>QPushButton</i>组件")
        # 设置按钮的大小和位置
        btn.resize(btn.sizeHint())
        btn.move(50, 50)
        # 设置窗口的大小和位置
        self.setGeometry(300, 300, 300, 200)
        # 设置窗口的标题
        self.setWindowTitle("提示框")
        # 设置图标
        self.setWindowIcon(QIcon("favicon.ico"))
        # 显示窗口
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    lxg = LxgApp()
    sys.exit(app.exec_())
