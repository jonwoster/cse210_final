import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Player(Actor):
    """
    Icon player moves around the screen to shot at aliens.
    
    The responsibility of Player is to be moved by the player.

    Attributes:
        _body (str): The player icon.
    """
    def __init__(self):
        super().__init__()
        # self._body = Actor()
        self._prepare_body()
    
    def _prepare_body(self):
        x = int(constants.MAX_X / 2)
        y = int(constants.MAX_Y - constants.CELL_SIZE)

        position = Point(x, y)
        text = "#"
        color = constants.WHITE
        # body = self._body
      
        self.set_position(position)
        self.set_text(text)
        self.set_color(color)
