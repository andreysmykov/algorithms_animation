from dataclasses import dataclass
from src.list_utilities.VisualNodeWithArrows import VNWithArrows


@dataclass
class Node:
    value: str = '0'
    next: 'Node' = None
    vn_arrows: VNWithArrows = None

    def __post_init__(self):
        self.vn_arrows = VNWithArrows(self.value)

    def set_next(self, n):
        self.next = n
        self.vn_arrows.set_right_arrow()
        self.vn_arrows.add_arrow()

    @property
    def is_none(self):
        return self.vn_arrows.is_none()


@dataclass
class NoneNode(Node):
    def __post_init__(self):
        self.vn_arrows = VNWithArrows("N")
