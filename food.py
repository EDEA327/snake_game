import random
from turtle import Turtle


class Food(Turtle):
    """
    A class representing a food object that inherits from the Turtle class.
    """
    def __init__(self):
        """
        Initializes the food object by setting its shape, color, size, and position.
        """
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("yellow")
        self.speed("fastest")
        self.change_position()

    def change_position(self) -> None:
        """
        Changes the position of the food object to a random position within the screen boundaries.
        """
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
