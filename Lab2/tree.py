from __future__ import annotations


class Node:
    def __init__(self, value):
        """Initialize a Node with an integer value."""
        self.value = value
        self.parent: Node = None
        self.children: list[Node] = []

    def set_parent(self, parent: Node):
        """Set the parent of this node."""
        self.parent = parent

    def get_parent(self) -> Node:
        """Return the parent of this node."""
        return self.parent

    def add_child(self, child: Node):
        """Add a child and assign this as its parent."""
        child.set_parent(self)
        self.children.append(child)

    def get_children(self) -> list[Node]:
        """Return the children of this node."""
        return self.children


def create_the_tree() -> Node:
    """
    Creates a simple tree with depth = 3 and values from 0 to 6.

    Manual structure:
        0
        ├── 1
        │    ├── 3
        │    └── 4
        └── 2
             ├── 5
             └── 6

    Returns:
        The root node (value 0).
    """

    n0 = Node(0)
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)

    n1.add_child(n3)
    n1.add_child(n4)

    n2.add_child(n5)
    n2.add_child(n6)

    n0.add_child(n1)
    n0.add_child(n2)

    return n0

