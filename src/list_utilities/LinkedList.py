from dataclasses import dataclass
from typing import List
from manim import VGroup

from src.list_utilities.Node import Node


@dataclass
class LinkedList:
    nodes: List[Node]
    head: Node = None
    tail: Node = None

    def __post_init__(self):
        for j in range(len(self.nodes) - 1):
            self.nodes[j].set_next(self.nodes[j + 1])
        self.head = self.nodes[0]
        self.tail = self.nodes[-1]
        self.visual_list = VGroup(*[n.vn_arrows.group for n in self.nodes]).arrange()
