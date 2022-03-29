# from copyreg import constructor
import constants
from game.casting.actor import Actor
from game.services.video_service import VideoService
from game.shared.point import Point

class Alien(Actor):

    def __init__(self):
        super().__init__()
        self.aliens = []
        self.generate_aliens()
        self.rows = 1
        self.timer = 0

    def generate_aliens(self):
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
        return self.aliens

    def move_next(self):
        self.timer += 1
        if self.timer >= 10:
            for alien in self.aliens:
                alien.move_next()
            if self.rows < constants.MAX_ALIEN_ROWS:
                self.generate_aliens()
                VideoService().draw_actors(self.aliens)
                self.rows += 1
            self.timer = 0

