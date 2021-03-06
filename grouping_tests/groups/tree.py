from typing import List

from .base import GroupNode

class TreeNode(GroupNode):

    """ Represents a tree of event groups """

    def _insert(self, flat_hashes: List[str], hierarchical_hashes: List[str], item):
        """ Event hashes are interpreted as a path down a tree of event groups """
        if hierarchical_hashes:
            head, *tail = hierarchical_hashes
            self._child(head).insert([], tail, item)
        else:
            self.items.append(item)

    @staticmethod
    def _child_type():
        return TreeNode