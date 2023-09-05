from turtle import Turtle

ALIGNMENT: str = "center"
FONT: tuple = ("Times New Roman", 24, "normal")


class ScoreBoard(Turtle):
    """
    A class to represent the scoreboard in the game.

    Attributes
    ----------
    score : int
        The current score of the player.

    Methods
    -------
    update_score() -> None:
        Updates the displayed score on the scoreboard turtle.
    """

    def __init__(self) -> None:
        """
        Constructs the scoreboard object and initializes its attributes.
        """
        super().__init__()
        self.score: int = 0
        with open("data.txt") as data:
            self.high_score: int = int(data.read().strip())
        self.color("white")
        self.penup()
        self.goto(0, 265)
        self.hideturtle()
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()

    def update_score(self) -> None:
        """
        Updates the displayed score on the scoreboard turtle.
        """
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset_scoreboard(self):

        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_score()

    # def game_over(self) -> None:
    #     """
    #     Displays the game over message on the scoreboard turtle.
    #     """
    #     self.color("red")
    #     self.home()
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)
