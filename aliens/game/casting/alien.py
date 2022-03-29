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
        self.aliens = []
        self.generate_aliens()
        self.rows = 1
        self.timer = 0

    def generate_aliens(self):
        """generates a row of aliens at the top"""
        for n in range(constants.COLUMNS):
            x = (n)*constants.CELL_SIZE
            y = 0
            position = Point(x, y)
            velocity = Point(0, constants.CELL_SIZE)
            text = "H"
            color = constants.GREEN
            alien = Actor()
            alien.set_position(position)
            alien.set_velocity(velocity)
            alien.set_text(text)
            alien.set_color(color)
            self.aliens.append(alien)
    
    def get_aliens(self):
        """returns the list of aliens"""
        return self.aliens

    def move_next(self):
        """
        Moves the aliens down one row when the timer is ready.
        Generates more aliens if the max rows haven't been filled yet.
        Resets the timer.
        """
        self.timer += 1
        if self.timer >= 10:
            for alien in self.aliens:
                alien.move_next()
            if self.rows < constants.MAX_ALIEN_ROWS:
                self.generate_aliens()
                VideoService().draw_actors(self.aliens)
                self.rows += 1
            self.timer = 0

