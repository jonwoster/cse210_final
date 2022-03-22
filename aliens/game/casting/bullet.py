from asyncio import constants
from actor import Actor
from aliens.game.shared.point import Point

class Bullet(Actor):

    def __init__(self):
        self.bullets = {}
        self.x = 0
        self.y=0
        self.is_alive = True

    def fire(self):
        return self.bullets

    def create_bullet(self, x, y):
        bullet = Actor()
        position = Point(x, y)
        velocity = Point(0, constants.CELL_SIZE * 2)
        text = "*"
        color = constants.RED
        bullet.set_position(position)
        bullet.set_velocity(velocity)
        bullet.set_text(text)
        bullet.set_color(color)
        self.bullets.append(bullet)
