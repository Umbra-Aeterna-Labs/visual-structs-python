"""@package VisualStructsPy
Graphically displays data structures such as arrays, lists, and trees.
"""

from VisualStructsPy.VSNode import VSNode


class VSArray:
    def __init__(self):
        self._numElems = 0

    class VSArrNode(VSNode):
        def __init__(self, config, data=None, index=0):
            super().__init__(config, data, index)
