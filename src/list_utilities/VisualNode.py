from dataclasses import dataclass
from manim import Text, VGroup, Circle, Square, WHITE, VMobject


class VisualNode:
    def __init__(self, text: str, fz):
        self._text = Text(text, font_size=fz)
        self._circle = self.type_node
        self._surround()
        self.__group = VGroup(self._circle, self._text)

    @property
    def group(self) -> VGroup:
        return self.__group

    @property
    def type_node(self) -> VMobject:
        return Circle(radius=0.3, color=WHITE, stroke_width=2)

    def set_red(self) -> None:
        red_color = "#c1292e"
        self._circle.set_fill(color=red_color, opacity=1)
        self._circle.set_color(red_color)

    def _surround(self) -> None:
        self._circle.surround(self._text, buffer_factor=2)


@dataclass
class VisualNoneNode(VisualNode):
    def __init__(self, text: str, fz: int) -> None:
        super(VisualNoneNode, self).__init__(text, fz)

    @property
    def type_node(self) -> VMobject:
        return Square(side_length=0.6, color="#fe5d26", stroke_width=3)

    def _surround(self) -> None:
        self._circle.surround(self._text, buff=0.3)
