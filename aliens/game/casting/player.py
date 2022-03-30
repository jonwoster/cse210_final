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
        self._prepare_body()
    
    def _prepare_body(self):
        _x = int(constants.MAX_X / 2)
        _y = int(constants.MAX_Y - constants.CELL_SIZE)

        _position = Point(_x, _y)
        _text = "#"
        _color = constants.WHITE
      
        self.set_position(_position)
        self.set_text(_text)
        self.set_color(_color)
