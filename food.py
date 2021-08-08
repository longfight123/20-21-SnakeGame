from turtle import Turtle
import random


class Food(Turtle):
    """
    A class used to represent a Food.

    ...

    Attributes
    ----------

    Methods
    -------
    refresh()
        moves the food to a random location
    """

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed(speed='fastest')
        self.color('blue')
        self.refresh()

    def refresh(self):
        """moves the food to a random location
        """
        self.goto(x=random.randint(-270, 270), y=random.randint(-270, 270))
