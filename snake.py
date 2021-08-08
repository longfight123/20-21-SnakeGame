from turtle import Turtle
START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
FORWARD_MOVEMENT = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    """
    A class used to represent a Snake.

    ...

    Attributes
    ----------
    segment_list: list
        a list that contains a list of turtle objects to
        represent the body of the snake
    head: turtle
        the head of the snake

    Methods
    -------
    create_snake()
        creates the starting snake
    add_segment(position)
        appends a new turtle object to the segment_list
    reset()
        resets the snake game
    extend()
        calls add_segment and passes in the position
        of the end of the snake
    move()
        moves each turtle object in segment_list
    up(), left(), right(), down()
        controls the direction of the head
    """

    def __init__(self):
        self.segment_list = []
        self.create_snake()
        self.head = self.segment_list[0]

    def create_snake(self):
        """creates the starting snake
        """
        for position in START_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """appends a new turtle object to the segment_list

        :param position: tuple
            x and y coordinates for new segment
        """
        new_segment = Turtle(shape='square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.setposition(position)
        self.segment_list.append(new_segment)

    def reset(self):
        """resets the snake game
        """
        for segment in self.segment_list:
            segment.goto(x=600, y=600)
        self.segment_list.clear()
        self.create_snake()
        self.head = self.segment_list[0]

    def extend(self):
        """calls add_segment and passes in the position
        of the end of the snake
        """
        self.add_segment(self.segment_list[-1].position())

    def move(self):
        """moves each turtle object in segment_list
        """
        for seg_number in range(len(self.segment_list) - 1, 0, -1):
            new_x = self.segment_list[seg_number - 1].xcor()
            new_y = self.segment_list[seg_number - 1].ycor()
            self.segment_list[seg_number].goto(x=new_x, y=new_y)
        self.head.forward(FORWARD_MOVEMENT)

    def up(self):
        """controls the direction of the head
        """
        if self.head.heading() == DOWN:
            pass
        else:
            self.head.setheading(to_angle=UP)

    def down(self):
        """controls the direction of the head
        """
        if self.head.heading() == UP:
            pass
        else:
            self.head.setheading(to_angle=DOWN)

    def right(self):
        """controls the direction of the head
        """
        if self.head.heading() == LEFT:
            pass
        else:
            self.head.setheading(to_angle=RIGHT)

    def left(self):
        """controls the direction of the head
        """
        if self.head.heading() == RIGHT:
            pass
        else:
            self.head.setheading(to_angle=LEFT)

