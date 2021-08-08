from turtle import Turtle
ALIGNMENT = 'center'
FONT = ("Arial", 15, "normal")


class Scoreboard(Turtle):

    """
    A class used to represent a Scoreboard.

    ...

    Attributes
    ----------
    high_score: int
        the current high score
    current_score: int
        the current score in the game

    Methods
    -------
    update_score()
        updates the current_score on the screen
    reset()
        updates the high_score if the current score is greater
        resets the current score to 0
    increase_score
        increases the current_score by 1
    export_high_score
        writes the high_score to a text file
    """

    def __init__(self):
        """Requires a high_score.txt file to keep track of the high score
        """
        super().__init__()
        self.shapesize(stretch_len=0.1, stretch_wid=0.1)
        with open('high_score.txt', mode='r') as file:
            self.high_score = int(file.read())
        self.current_score = 0
        self.penup()
        self.speed('fastest')
        self.color('white')
        self.goto(x=0, y=270)
        self.write(arg=f'Score: {self.current_score} High Score: {self.high_score}', align=ALIGNMENT, font=FONT)

    def update_score(self):
        """Updates the current_score on the screen
        """
        self.clear()
        self.write(arg=f'Score: {self.current_score} High Score: {self.high_score}', align=ALIGNMENT, font=FONT)

    def reset(self):
        """updates the high_score if the current score is greater
        resets the current score to 0
        """
        if self.current_score > self.high_score:
            self.high_score = self.current_score
            self.export_high_score()
        self.current_score = 0
        self.update_score()

    def increase_score(self):
        """increases the current_score by 1
        """
        self.current_score += 1
        self.update_score()

    def export_high_score(self):
        """writes the high_score to a text file
        """
        with open('high_score.txt', mode='w') as file:
            file.write(str(self.high_score))

    # def game_over(self):
    #     self.clear()
    #     self.goto(x=0, y=0)
    #     self.write(arg=f'Game Over. Score: {self.current_score}', align=ALIGNMENT, font=FONT)

