"""@package VisualStructsPy
Graphically displays data structures such as arrays, lists, and trees.
"""

from PyQt5.QtGui import (QColor, QFont)


class VSNode:
    def __init__(self, config, data=None, index=0):
        self._config = config

        if data:
            self._data = data
        else:
            self._data = ''

        if index >= 0:
            self._index = index
        else:
            self._index = 0

        self._x = 100
        self._y = 100
        self._w = 70
        self._h = 50

    def drawNode(self, qp):
        qp.setFont(QFont(self._config.fontFam, self._config.fontSz))
        qp.setPen(QColor(0, 0, 0))
        qp.setBrush(QColor(250, 150, 150))
        qp.drawEllipse(self._x, self._y, self._w, self._h)
        qp.drawText(self._x + self._config.txtMargin + (self._w / 3),
                    self._y + self._config.txtMargin + (self._h / 1.6),
                    str(self._index))
