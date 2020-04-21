"""@package VisualStructsPy
Graphically displays data structures such as arrays, lists, and trees.
"""

from VisualStructsPy.VSNode import VSNode


class VSTree:
    def __init__(self, children=None):
        if children.__len__() >= 0:
            self._numElems = children.__len__()
        else:
            self._numElems = 0

    class VSTreeNode(VSNode):
        def __init__(self, config, data=None, index=0, children=None):
            super().__init__(config, data, index)
            if children:
                self._children = children
            else:
                self._children = []
