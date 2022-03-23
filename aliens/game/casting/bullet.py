import constants
from game.casting.actor import Actor
from game.shared.point import Point

class Bullet(Actor):

    def __init__(self):
        super().__init__()
        self.bullets = []
        self.x = 0
        self.y=0
        self.create_bullet()
        self._velocity = 10

    def fire(self):
        return self.bullets

    def create_bullet(self):
        bullet = Actor()
        x = 0
        y = int(constants.MAX_Y - constants.CELL_SIZE)
        position = Point(x, y)
        velocity = Point(0, constants.CELL_SIZE * 2)
        text = "*"
        color = constants.RED
        bullet.set_position(position)
        bullet.set_velocity(velocity)
        bullet.set_text(text)
        bullet.set_color(color)
        self.bullets.append(bullet)
