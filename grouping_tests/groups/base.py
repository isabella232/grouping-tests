from typing import Any, Dict, List


class GroupNode:

    """ Group of events. Subclasses differ in the way they insert / merge events """

    def __init__(self, name: str):

        self.name = name

        self.total_item_count = 0  # Sum of items in self + descendants
        self.items: List[Any] = []
        self.children: Dict[str, GroupNode] = {}

        self.exemplar = None  # Item representing this node

    @property
    def item_count(self):
        return len(self.items)

    def insert(self, flat_hashes: List[str], hierarchical_hashes: List[str], item):

        self._insert(flat_hashes, hierarchical_hashes, item)

        if self.exemplar is None:
            self.exemplar = item

        self.total_item_count += 1

    def visit(self, visitor, ancestors=None):
        if ancestors is None:
            ancestors = []
        visitor(self, ancestors)
        for child in self.children.values():
            child.visit(visitor, ancestors + [self])

    def _insert(self, flat_hashes: List[str], hierarchical_hashes: List[str], item):
        """ Override in subclasses """
        raise NotImplementedError

    @staticmethod
    def _child_type():
        """ Override in subclasses """
        raise NotImplementedError

    def _child(self, name):
        if name not in self.children:
            klass = self._child_type()
            child = self.children[name] = klass(name)
        else:
            child = self.children[name]

        return child
