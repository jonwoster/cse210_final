import constants
from game.casting.actor import Actor
from game.services.video_service import VideoService
from game.shared.point import Point

class Alien(Actor):
    """
    The aliens are enemies that will move down the screen until they are
    hit by a bullet or reach the bottom making the player lose.
    
    Attributes:
        self.aliens[list]: When an alien is created it will append to this list
    """

    def __init__(self):
        super().__init__()
        self._aliens = []
        self._generate_aliens()
        self._rows = 1
        self._timer = 0

    def _generate_aliens(self):
        """generates a row of aliens at the top"""
        for n in range(constants.COLUMNS):
            _x = (n)*constants.CELL_SIZE
            _y = 0
            _position = Point(_x, _y)
            _velocity = Point(0, constants.CELL_SIZE)
            _text = "H"
            _color = constants.GREEN
            alien = Actor()
            alien.set_position(_position)
            alien.set_velocity(_velocity)
            alien.set_text(_text)
            alien.set_color(_color)
            self._aliens.append(alien)
    
    def get_aliens(self):
        """returns the list of aliens"""
        return self._aliens

    def move_next(self):
        """
        Moves the aliens down one row when the timer is ready.
        Generates more aliens if the max rows haven't been filled yet.
        Resets the timer.
        """
        self._timer += 1
        if self._timer >= 10:
            for alien in self._aliens:
                alien.move_next()
            if self._rows < constants.MAX_ALIEN_ROWS:
                self._generate_aliens()
                VideoService().draw_actors(self._aliens)
                self._rows += 1
            self._timer = 0

