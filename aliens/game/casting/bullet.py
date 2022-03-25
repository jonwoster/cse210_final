
# from game.casting.actor import Actor
# from game.shared.point import Point
# import constants

# class Bullet(Actor):

#     def __init__(self):
#         super().__init__()
#         self.bullets = []
#         self.x = 0
#         self.y=0
#         self._velocity = 10
#         self.timer = 0
#         self._is_alive = True

#     def fire(self):
#         return self.bullets

    
#     def create_bullet(self):
#         bullet = Bullet()
#         self.x = 0
#         self.y = int(constants.MAX_Y - constants.CELL_SIZE)
#         position = Point(self.x, self.y)
#         velocity = Point(0, constants.CELL_SIZE)
#         text = "*"
#         color = constants.RED
#         bullet.set_position(position)
#         bullet.set_velocity(velocity)
#         bullet.set_text(text)
#         bullet.set_color(color)
#         self.bullets.append(bullet)

#     def move_next(self):
#         self.timer += 1
#         y = int(constants.MAX_Y)
#         x = constants.MAX_X/2
#         self._position = Point(x, y)
#         if self.timer >= 5:
#             self._is_alive = False

from copyreg import constructor
import constants
from game.casting.actor import Actor
from game.services.video_service import VideoService
from game.shared.point import Point
from game.casting.player import Player
from game.casting.cast import Cast

class Bullet(Actor):

    def __init__(self):
        super().__init__()
        self.bullets = []
        self.timer = 0
        
    def create_bullet(self, cast):
        player = cast.get_first_actor("player")
        player_position = player.get_position()
        # position = Point(0, 0)
        # velocity = Point(0, constants.CELL_SIZE)
        text = "*"
        color = constants.RED
        bullet = Actor()
        bullet.set_position(player_position)
        # bullet.set_velocity(velocity)
        bullet.set_text(text)
        bullet.set_color(color)
        self.bullets.append(bullet)
    
    def get_bullets(self):
        return self.bullets

    def move_next(self):
        # self.timer += 1
        # if self.timer >= 5:
        for bullet in self.bullets:
            bullet.move_next()
        # if self.rows < 7:
        #     self.generate_bullets()
            # VideoService().draw_actors(self.bullets)
               
            # self.timer = 0
        else:
            pass