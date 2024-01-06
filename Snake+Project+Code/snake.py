from typing import List, Tuple
from turtle import Turtle

STARTING_POSITIONS: List[Tuple[int, int]] = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE: int = 20
UP: int = 90
DOWN: int = 270
LEFT: int = 180
RIGHT: int = 0


class Snake:
    def __init__(self) -> None:
        self.segments: List[Turtle] = []
        self.create_snake()
        self.head: Turtle = self.segments[0]

    def create_snake(self) -> None:
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position: Tuple[int, int]) -> None:
        new_segment: Turtle = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self) -> None:
        self.add_segment(self.segments[-1].position())

    def move(self) -> None:
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x: float = self.segments[seg_num - 1].xcor()
            new_y: float = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self) -> None:
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self) -> None:
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self) -> None:
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self) -> None:
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self) -> None:
        for seg in self.segments:
            seg.goto(400, 400)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
