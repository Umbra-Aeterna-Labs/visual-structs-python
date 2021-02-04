"""
    Copyright 2021 Umbra Aeterna Labs <https://github.com/Umbra-Aeterna-Labs>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

@package VisualStructsPy
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
