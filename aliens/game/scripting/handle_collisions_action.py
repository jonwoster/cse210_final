import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point
import raylib

#encode file to be read by raylib
if constants.OS.lower() == "darwin":
    lose_sound = raylib.LoadSound("aliens/game/sounds/lose_sound.wav".encode('ascii'))
    win_sound = raylib.LoadSound("aliens/game/sounds/win_sound.wav".encode('ascii'))
elif constants.OS.lower() == "windows":
    lose_sound = raylib.LoadSound("aliens\game\sounds\lose_sound.wav".encode('ascii'))
    win_sound = raylib.LoadSound("aliens\game\sounds\win_sound.wav".encode('ascii'))


class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the cycle1 collides
    with the food, or the cycle1 collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_segment_collision(cast)
            self._handle_game_over(cast)

    
    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the cycle1 collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """

        # Get the list of bullets
        _bullet_dad = cast.get_first_actor("bullets")

        # Get the list of aliens
        _alien_dad = cast.get_first_actor("aliens")
        _aliens = _alien_dad.get_aliens()

        _player = cast.get_first_actor("player")

        # alien_to_destroy = []
            # loop through the aliens
        for _alien in _aliens:
                # if the Y posiiton of the current alien reaches max Y, then set game over flag
                # remove all items from the alien list
            # print(_alien.get_position().get_y())
            if _alien.get_position().get_y() >= constants.BOTTOM_SCREEN:
                self._is_game_over = True
                _aliens.clear()  # remove all aliens

                
                x = int(constants.MAX_X / 2)
                y = int(constants.MAX_Y / 2)
                position = Point(x, y)
                message = Actor()
                #if alien touch the bottom 
                message.set_text("Game Over!" " *** " "You Lost!!!")
            
                message.set_position(position)
                cast.add_actor("messages", message)
                #play sound
                raylib.PlaySound(lose_sound)
                break

            _bullets = _bullet_dad.get_bullets()
            # bullets_to_destory=[]
            #loop through the bullets
            for _bullet in _bullets:

                # if position of current bullet equals position of current alien, remove both the alien and the bullet

                if _bullet.get_position().equals(_alien.get_position()):

                    _bullets.remove(_bullet)
                    _aliens.remove(_alien)


                # if Y position of the current bullet reaches the top of screen, then remove the bullet 
                # so it doesn't come back up from the bottom
    
                if (_bullet.get_position().get_y()) <= (constants.MIN_Y):
                    _bullets.remove(_bullet)



            # if the count of aliens reaches 0, then set game over flag and exit method

            if len(_aliens) == 0:
                self._is_game_over = True
                _bullets.clear()  # remove all bullets
                x = int(constants.MAX_X / 2)
                y = int(constants.MAX_Y / 2)
                position = Point(x, y)
                message = Actor()
                
                
                #if player kill aliens
                message.set_text("Game Over! "" *** "" You Win!!!")
                
                message.set_position(position)
                cast.add_actor("messages", message)

                #play sound
                raylib.PlaySound(win_sound)







    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the cycle1 and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        #if self._is_game_over:
        

            

        
            
            
            #play sound
            # raylib.PlaySound(sound)

            # for segment in segments1:
            #     segment.set_color(constants.WHITE)
            # for segment in segments2:
            #     segment.set_color(constants.WHITE)
