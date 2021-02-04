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
