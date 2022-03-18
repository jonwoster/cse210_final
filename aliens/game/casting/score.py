from game.casting.actor import Actor
from game.shared.point import Point
import constants

class Score(Actor):
    """
    A record of points made or lost. 
    
    The responsibility of Score is get the number of segments created and pass it to get_text() to get a string 
    representation of the segment count.
    Attributes:
        _seg_count (int): The number of segments created before the game is over
    """
    def __init__(self):
        super().__init__()

        position = Point(constants.SCORE_X, constants.SCORE_Y)  # Import location of score from Constants file
        self.set_position(position) # Set the position of the score
    
    def update_seg_count(self, segment_count): # new method to replace add_points
        """Shows the total number of cycle segments that were created before game is over
        
        Args:
            segment_count: the number of segments
        """
        self._seg_count = segment_count # grab the segment count that was passed into this method
        self.set_text(f"Segments Created: {self._seg_count}")  # Updated to show Segments created instead of points
        # print(f"count at end of Score's update_seg_count method is {self._seg_count}")  # for debugging
    