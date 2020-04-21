"""@package VisualStructsPy
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
