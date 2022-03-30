from game.casting.bullet import Bullet
from game.casting.cast import Cast
from game.casting.score import Score
from game.casting.player import Player
from game.casting.alien import Alien
from game.scripting.script import Script 
from game.scripting.control_actors_action import ControlActorsAction                        
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.move_bullets_action import MoveBulletsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

# Main sets up the cast groups, the script of actions and then calls Director to start the game

def main():
    
    # create the cast
    cast = Cast()
    cast.add_actor("player", Player())
    cast.add_actor("scores", Score())
    cast.add_actor("aliens", Alien())
    cast.add_actor("bullets", Bullet())
   
    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    # add in actions to the script
    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("update", MoveBulletsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))
    
    # Start the game by invoking Director's start_game method
    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()