from turtle import Turtle
from typing import List

# Constants
UP: int = 90
DOWN: int = 270
LEFT: int = 180
RIGHT: int = 0


class Snake:
    def __init__(self) -> None:
        """
        Initializes a new Snake object with default values for snake color, spacing, distance, segments, and head.
        Creates a snake body with three segments.
        """
        self.snake_color: str = "white"
        self.square_spacing: int = -20
        self.distance: int = 20
        self.segments: List[Turtle] = []
        self.create_snake()
        self.head: Turtle = self.segments[0]

    def create_snake(self) -> None:
        """
        Creates a snake body with three segments.
        """
        # Creates a snake with three segments
        for _ in range(3):
            self.add_segment()

    def add_segment(self) -> None:
        """
        Adds a new segment to the snake's body.
        """
        # Creates a new segment with a square shape, sets its color and position,
        # and appends it to the snake's segments list
        new_segment: Turtle = Turtle(shape="square")
        new_segment.color(self.snake_color)
        new_segment.penup()
        if len(self.segments) == 0:
            new_segment.goto(0, 0)
        else:
            last_segment: Turtle = self.segments[-1]
            new_segment.goto(last_segment.position())
        self.segments.append(new_segment)

    def extend(self) -> None:
        """
        Extends the length of the snake by adding a new segment.
        """
        self.add_segment()

    def move(self) -> None:
        """
        Moves the snake forward by one square.
        """
        # Moves each segment of the snake to the position of the segment in front of it, except for the head,
        # which is moved forward by one square.
        for i in range(len(self.segments) - 1, 0, -1):
            new_x: float = self.segments[i - 1].xcor()
            new_y: float = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)
        self.head.forward(self.distance)

    def up(self) -> None:
        """
        Changes the direction of the snake's head to up, but only if the current direction is not down.
        """
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self) -> None:
        """
        Changes the direction of the snake's head to down, but only if the current direction is not up.
        """
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self) -> None:
        """
        Changes the direction of the snake's head to left, but only if the current direction is not right.
        """
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self) -> None:
        """
        Changes the direction of the snake's head to right, but only if the current direction is not left.
        """
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
