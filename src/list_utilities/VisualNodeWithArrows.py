from dataclasses import dataclass
from manim import Arrow, VGroup, ORIGIN, RIGHT

from src.list_utilities.VisualNode import VisualNode, VisualNoneNode


@dataclass
class VNWithArrows:
    inner_text: str
    vnode: VisualNode = None
    right_arrow: Arrow = None
    left_arrow: Arrow = None
    group: VGroup = None

    def __post_init__(self):
        self.vnode = VisualNode(self.inner_text, 22) if self.inner_text != "N"\
            else VisualNoneNode(self.inner_text, 17)
        self.group = VGroup(self.vnode.group)

    def set_right_arrow(self) -> None:
        self.right_arrow = Arrow(ORIGIN, RIGHT * 1).next_to(self.vnode.group, RIGHT)

    def set_right_to_left_arrow(self) -> None:
        self.left_arrow = self.right_arrow

    def add_arrow(self) -> None:
        self.group.add(self.right_arrow)

    def remove_arrow(self) -> None:
        self.group.remove(self.right_arrow)

    def flip_arrow(self) -> None:
        self.right_arrow.flip()

    def is_none(self):
        return isinstance(self.vnode, VisualNoneNode)
