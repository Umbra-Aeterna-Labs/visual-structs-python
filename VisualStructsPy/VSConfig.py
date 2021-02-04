"""
    Copyright (C) 2021 Umbra Aeterna Labs <https://github.com/Umbra-Aeterna-Labs>

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


class VSConfig:
    def __init__(self):
        self.guiX = 100
        self.guiY = 100
        self.guiW = 600
        self.guiH = 600
        self.titleSz = 28
        self.fontSz = 18
        self.fontFam = 'Sans Serif'
        self.padd = 4 / self.fontSz
        self.txtMargin = self.fontSz / 4
