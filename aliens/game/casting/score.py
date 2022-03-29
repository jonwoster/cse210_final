from game.casting.actor import Actor
from game.shared.point import Point
import constants

class Score(Actor):
    """
    A record of points made or lost. 
    
    The responsibility of Score is set the location for the game over messages
    
    Attributes:
        None
    """
    def __init__(self):
        super().__init__()

        position = Point(constants.SCORE_X, constants.SCORE_Y)  # Import location of score from Constants file
        self.set_position(position) # Set the position of the score

    