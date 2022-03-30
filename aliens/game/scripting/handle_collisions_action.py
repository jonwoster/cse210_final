import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point
import raylib

# encode file to be read by raylib for game over sounds
if constants.OS.lower() == "darwin":
    lose_sound = raylib.LoadSound("aliens/game/sounds/lose_sound.wav".encode('ascii'))
    win_sound = raylib.LoadSound("aliens/game/sounds/win_sound.wav".encode('ascii'))
elif constants.OS.lower() == "windows":
    lose_sound = raylib.LoadSound("aliens\game\sounds\lose_sound.wav".encode('ascii'))
    win_sound = raylib.LoadSound("aliens\game\sounds\win_sound.wav".encode('ascii'))


class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when bullet collides with aliens, or aliens with the ground, or the game is over.

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

    
    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the cycle1 collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """

        # Get the list of bullets
        bullet_group = cast.get_first_actor("bullets")

        # Get the list of aliens
        alien_group = cast.get_first_actor("aliens")
        aliens = alien_group.get_aliens()
        
        # loop through the aliens
        for alien in aliens:

            # if the Y posiiton of the current alien reaches max Y, then set game over flag
            # remove all items from the alien list and display game over message
            if alien.get_position().get_y() >= constants.BOTTOM_SCREEN:
                self._is_game_over = True
                aliens.clear()  # remove all aliens

                # set up position for game over message
                x = int(constants.MAX_X / 2)
                y = int(constants.MAX_Y / 2)
                position = Point(x, y)
                # set up message for game over
                message = Actor()
                message.set_text("Game Over!" " *** " "You Lost!!!")
                message.set_position(position)
                cast.add_actor("messages", message)
                #play sound
                raylib.PlaySound(lose_sound)
                break

            # get the list of bullets
            bullets = bullet_group.get_bullets()
            
            #loop through the bullets
            for bullet in bullets:

                # if position of current bullet equals position of current alien, remove both the alien and the bullet
                if bullet.get_position().equals(alien.get_position()):
                    bullets.remove(bullet)
                    aliens.remove(alien)

                # if Y position of the current bullet reaches the top of screen, then remove the bullet 
                # so it doesn't come back up from the bottom
                if (bullet.get_position().get_y()) <= (constants.MIN_Y):
                    bullets.remove(bullet)

            # if the count of aliens reaches 0, then set game over flag and display game over message
            if len(aliens) == 0:
                self._is_game_over = True
                bullets.clear()  # remove all bullets

                # setup the location of game over message
                x = int(constants.MAX_X / 2)
                y = int(constants.MAX_Y / 2)
                _position = Point(x, y)
                # setup the message for game over, indicating player won
                message = Actor()
                message.set_text("Game Over! "" *** "" You Win!!!")
                message.set_position(position)
                cast.add_actor("messages", message)

                #play sound
                raylib.PlaySound(win_sound)









            

        
            
            
           
