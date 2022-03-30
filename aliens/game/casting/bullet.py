import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Bullet(Actor):
    """This class contains all of the info to create a bullet that shoots from the player position.
    An instance of the bullet is created and put into a list of all active bullets on the screen.
    
    Attributes:
        Self.bullets[list]: when a bullet is created, it will appenc to this list."""

    def __init__(self):
        """Constructs a new Bullet and starts an empty list."""
        super().__init__()
        self._bullets = []
        self._timer = 0
        
    def create_bullet(self, cast):
        """Creates a bullet with needed attributes and appends it to self.bullets."""
        _player = cast.get_first_actor("player")
        _player_position = _player.get_position()
        _velocity = Point(0, -constants.CELL_SIZE)
                
        #set attributes for the display of the bullet:
        _text = "*"
        _color = constants.RED
        bullet = Actor()
        bullet.set_position(_player_position)
        bullet.set_velocity(_velocity)
        bullet.set_text(_text)
        bullet.set_color(_color)
        # Add bullet to the list of active bullets.
        self._bullets.append(bullet)
    
    def get_bullets(self):
        """Returns the list of bullets."""
        return self._bullets

    def move_next(self):
        """Tells the bullet to progress in the game."""
        for bullet in self._bullets:
            bullet.move_next()
        else:
            pass