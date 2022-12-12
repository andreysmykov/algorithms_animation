# See 'Leetcode 806. Middle of the Linked List' for practice

from typing import Tuple
from manim import *

from src.list_utilities.Node import Node, NoneNode
from src.list_utilities.LinkedList import LinkedList


class MiddleLinkedList(Scene):
    def construct(self):
        title = MarkupText("Middle of Linked List", font_size=40).shift(UP * 3)
        self.add(title)
        self.show_task(title)
        self.show_middle_code(title)
        self.show_middle(range(1, 5))
        self.wait(2)
        self.show_middle(range(1, 6))
        self.wait(2)

    def show_task(self, title: MarkupText) -> None:
        odd_nodes = [Node(str(j)) for j in range(1, 6)]
        odd_list = LinkedList(nodes=odd_nodes)
        middle_odd_node = self.get_middle_node(odd_list.head)

        even_nodes = [Node(str(j)) for j in range(1, 5)]
        even_list = LinkedList(nodes=even_nodes)
        middle_even_node = self.get_middle_node(even_list.head)

        for middle in [middle_odd_node, middle_even_node]:
            middle.vn_arrows.vnode.set_red()

        result = VGroup(even_list.visual_list, odd_list.visual_list)\
            .arrange(DOWN, buff=1).next_to(title, DOWN * 7)
        self.play(FadeIn(result, run_time=2))
        self.wait(2)
        self.play(FadeOut(result))

    def show_middle(self, range_) -> None:
        orig_nodes = [Node(str(j)) for j in range_]
        orig_list = LinkedList(nodes=orig_nodes)
        self.play(FadeIn(orig_list.visual_list))
        self.wait(1)

        none_end = NoneNode()
        orig_list.tail.set_next(none_end)
        self.show_none_end(orig_list, none_end)
        middle, tp = self.middle_node_visual(orig_list.head)
        self.wait(1)
        middle.vn_arrows.vnode.set_red()
        self.wait(1)

        self.play(FadeOut(none_end.vn_arrows.vnode.group),
                  FadeOut(orig_list.tail.vn_arrows.left_arrow),
                  FadeOut(orig_list.visual_list),
                  FadeOut(tp.slow_fast))

    def show_none_end(self, list_: LinkedList, end) -> None:
        end.vn_arrows.group.next_to(list_.visual_list, RIGHT)
        self.play(FadeIn(end.vn_arrows.vnode.group, run_time=2))
        self.wait(1)

    def show_middle_code(self, title: MarkupText) -> None:
        code = '''
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
        '''
        rendered_code = Code(code=code, tab_width=4, insert_line_no=False,
                             language="Python", font="Monospace", font_size=14)\
            .next_to(title, RIGHT * 2)
        self.play(Create(rendered_code))

    def get_middle_node(self, head: Node) -> Node:
        slow = fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow

    def middle_node_visual(self, head: Node) -> Tuple[Node, 'TextPointers']:
        slow = fast = head
        tp = TextPointers(head, self)
        while not fast.is_none and not fast.next.is_none:
            tp.move_slow_fast(slow, fast)
            slow = slow.next
            fast = fast.next.next
        return slow, tp


class TextPointers:
    def __init__(self, head: Node, scene: Scene) -> None:
        self.__font_size = 18
        self.__scene = scene

        self.__slow = Text("s", font_size=self.__font_size)
        self.__fast = Text("f", font_size=self.__font_size)

        self.__slow_fast = VGroup(self.__fast, self.__slow).arrange(buff=0.2)\
            .next_to(head.vn_arrows.vnode.group, UP)
        scene.play(FadeIn(self.__slow_fast))

        traced_path_slow = TracedPath(lambda: self.__slow.get_bottom() - 0.1, dissipating_time=1,
                                      stroke_opacity=[0, 1])
        scene.add(traced_path_slow)

        traced_path_fast = TracedPath(lambda: self.__fast.get_bottom() - 0.1, dissipating_time=1,
                                      stroke_opacity=[0, 1])
        scene.add(traced_path_fast)
        scene.wait(1)

    @property
    def slow_fast(self) -> VGroup:
        return self.__slow_fast

    def move_slow_fast(self, slow: Node, fast: Node) -> None:
        slow_next, fast_next = self.__slow.copy(), self.__fast.copy()
        slow_next.next_to(slow.next.vn_arrows.vnode.group, UP)
        fast_next.next_to(fast.next.next.vn_arrows.vnode.group, UP)

        self.__scene.play(
            Transform(
                self.__slow,
                slow_next,
                path_func=utils.paths.path_along_arc(arc_angle=TAU / 4, axis=IN),
                run_time=2
            ),
            Transform(
                self.__fast,
                fast_next,
                path_func=utils.paths.path_along_arc(arc_angle=TAU / 4, axis=IN),
                run_time=2
            ),
        )
        self.__scene.wait(0.7)
