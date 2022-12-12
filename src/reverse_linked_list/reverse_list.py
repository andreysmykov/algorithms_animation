# See 'Leetcode 206. Reverse Linked List' for practice

from manim import *

from src.list_utilities.LinkedList import LinkedList
from src.list_utilities.Node import Node, NoneNode


class ReverseList(Scene):
    def construct(self):
        title = MarkupText("Reverse linked list", font_size=45).shift(UP * 3)
        self.add(title)

        self.show_task(title)
        self.show_reverse_list_code(title)

        orig_nodes = [Node(str(j)) for j in range(1, 4)]
        orig_list = LinkedList(nodes=orig_nodes)
        self.play(FadeIn(orig_list.visual_list))
        self.wait(1)

        none_start = NoneNode()
        none_start.set_next(orig_list.head)
        none_end = NoneNode()
        orig_list.tail.set_next(none_end)
        self.show_none_start_end(orig_list, none_start, none_end)

        self.reverse_list(none_start, orig_list.head)
        self.play(FadeOut(none_start.vn_arrows.vnode.group),
                  FadeOut(orig_list.head.vn_arrows.left_arrow))
        self.wait(2)

    def show_task(self, title: MarkupText) -> None:
        orig_nodes = [Node(str(j)) for j in range(1, 4)]
        orig_list = LinkedList(nodes=orig_nodes)

        rev_nodes = [Node(str(j)) for j in range(3, 0, -1)]
        rev_list = LinkedList(nodes=rev_nodes)

        down_arrow = MathTex(r"\Downarrow", color=WHITE)
        result = VGroup(orig_list.visual_list, down_arrow, rev_list.visual_list)\
            .arrange(DOWN, buff=0.5).next_to(title, DOWN * 5)
        self.play(FadeIn(result, run_time=3))
        self.wait(2)
        self.play(FadeOut(result))

    def show_reverse_list_code(self, title: MarkupText) -> None:
        code = '''
        prev, cur = None, head
        while cur:
            next_node = cur.next
            cur.next = prev
            prev, cur = cur, next_node
        return prev
        '''
        rendered_code = Code(code=code, tab_width=4, insert_line_no=False,
                             language="Python", font="Monospace", font_size=14)\
            .next_to(title, RIGHT * 2)
        self.play(Create(rendered_code))

    def show_none_start_end(self, list_: LinkedList, start: Node, end: Node) -> None:
        end.vn_arrows.group.next_to(list_.visual_list, RIGHT)
        start.vn_arrows.group.next_to(list_.visual_list, LEFT)
        self.play(FadeIn(end.vn_arrows.group, run_time=2))

        start.vn_arrows.remove_arrow()
        self.play(FadeIn(start.vn_arrows.group, run_time=2))
        self.wait(1)

    def reverse_list(self, none_node: Node, head: Node) -> Node:
        prev, cur = none_node, head
        tp = TextPointers(prev, cur, self)
        self.wait(0.8)

        while not cur.is_none:
            next_node = cur.next
            move_arrow(prev, cur, self)
            cur.next = prev
            tp.move_prev_cur()
            prev, cur = cur, next_node
            tp.update_next(cur)
            self.wait(0.8)

        self.play(FadeOut(tp.cur, cur.vn_arrows.group), tp.get_prev_to_cur_transform())
        self.wait(0.5)
        return prev


def move_arrow(prev: Node, cur: Node, scene: Scene) -> None:
    scene.wait(0.8)
    prev.vn_arrows.flip_arrow()
    scene.play(CounterclockwiseTransform(cur.vn_arrows.right_arrow, prev.vn_arrows.right_arrow))
    cur.vn_arrows.set_right_to_left_arrow()
    cur.vn_arrows.set_right_arrow()


class TextPointers:
    def __init__(self, prev: Node, cur: Node, scene: Scene) -> None:
        self.__font_size = 18
        self.__prev = Text("prev", font_size=self.__font_size)
        self.__cur = Text("cur", font_size=self.__font_size)
        self.__next = Text("next", font_size=self.__font_size)
        self.scene = scene

        self.__prev.next_to(prev.vn_arrows.vnode.group, DOWN)
        self.__cur.next_to(cur.vn_arrows.vnode.group, DOWN)
        if cur.next:
            self.__next.next_to(cur.next.vn_arrows.vnode.group, DOWN)
        self.scene.play(FadeIn(self.__prev, self.__cur))

    @property
    def cur(self) -> Text:
        return self.__cur

    def move_prev_cur(self) -> None:
        self.__prev.generate_target()
        self.__prev.target.move_to(self.__cur)

        self.__cur.generate_target()
        self.__cur.target.move_to(self.__next)

        self.scene.play(MoveToTarget(self.__prev), MoveToTarget(self.__cur))
        self.scene.wait(1)

    def update_next(self, cur: Node) -> None:
        if cur.next:
            self.__next.next_to(cur.next.vn_arrows.vnode.group, DOWN)

    def get_prev_to_cur_transform(self) -> Transform:
        head_text = Text("head", font_size=self.__font_size).shift(self.__prev.get_center())
        return Transform(self.__prev, head_text)
