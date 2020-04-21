"""@package VisualStructsPy
Graphically displays data structures such as arrays, lists, and trees.
"""

import sys
from VisualStructsPy.VSConfig import VSConfig
from VisualStructsPy.VSNode import VSNode
from PyQt5.QtWidgets import (QMainWindow, QApplication, QAction, qApp)
from PyQt5.QtGui import (QPainter, QIcon)

testData = [
    'Nulla ac tellus lacus.',
    'Morbi euismod mi lorem, non placerat tellus iaculis et.',
    'Ut in feugiat nisl, in fringilla leo.',
    'In hendrerit blandit velit vitae ullamcorper.',
    'Nullam a pretium ex, in hendrerit nulla.',
    'Donec fermentum purus eget magna fermentum blandit.',
    'Nulla id neque vel diam vestibulum convallis id a felis.',
    'Quisque ac eros at magna mollis suscipit in vitae turpis.',
    'Duis sodales mattis scelerisque.'
]


class Canvas(QMainWindow):
    def __init__(self, data):
        super().__init__()

        self._guiX = 100
        self._guiY = 100
        self._guiWidth = 1000
        self._guiHeight = 600
        self._guiMargins = 50

        self._node = VSNode(cfg, data[0], 0)

        self._initUI()

    def _initUI(self):
        exitAct = QAction(QIcon('exit.png'), '&Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAct)

        self.setGeometry(cfg.guiX, cfg.guiY, cfg.guiW, cfg.guiH)
        self.setWindowTitle('Visual Structs')
        self.show()

    def _longestStr(self, data):
        i = 0
        longest = 0
        while i < data.__len__():
            if longest < data[i].__len__():
                longest = data[i].__len__()
            i += 1

        return longest

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self._node.drawNode(qp)
        qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    cfg = VSConfig()
    ex = Canvas(testData)
    sys.exit(app.exec_())
