import constants
from game.casting.bullet import Bullet
from game.casting.cast import Cast
from game.casting.score import Score
from game.casting.player import Player
# from game.casting.cycle1 import Cycle1
# from game.casting.cycle2 import Cycle2
from game.casting.alien import Alien
from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.shared.color import Color
from game.shared.point import Point


def main():
    
    # create the cast
    cast = Cast()
    cast.add_actor("player", Player())
    # cast.add_actor("cycles2", Cycle2())
    # cast.add_actor("cycles1", Cycle1())    
    cast.add_actor("scores", Score())
    cast.add_actor("aliens", Alien())
    cast.add_actor("bullets", Bullet())
   
    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))
    
    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()