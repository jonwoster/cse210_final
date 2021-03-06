import constants
from game.scripting.action import Action
from game.shared.point import Point
import raylib #import all needed info for sound

#initialize audio device
raylib.InitAudioDevice()
#encode file to be read by raylib for game sounds
if constants.OS.lower() == "darwin":
    sound = raylib.LoadSound("aliens/game/sounds/player_sound.wav".encode('ascii'))
elif constants.OS.lower() == "windows":
    sound = raylib.LoadSound("aliens\game\sounds\player_sound.wav".encode('ascii'))


class ControlActorsAction(Action):
    """
    An input action that controls the player movement left and right
    
    The responsibility of ControlActorsAction is to get the direction and move the player left and right

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        self._direction = Point(constants.CELL_SIZE, 0)

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """

        # get player and bullets for use in the method
        player = cast.get_first_actor("player")
        bullet = cast.get_first_actor("bullets")

        # The default is that the player is not moving
        self._direction = Point(0,0)
        player.set_velocity(self._direction) 

        # Move the player left if they hit the left arrow
        if self._keyboard_service.is_key_down(constants.LT):
            self._direction = Point(-constants.CELL_SIZE, 0)
            player.set_velocity(self._direction)
            # play sound
            raylib.PlaySound(sound)
        
        # Move the player right if they hit the right arrow
        if self._keyboard_service.is_key_down(constants.RT):
            self._direction = Point(constants.CELL_SIZE, 0)
            player.set_velocity(self._direction)
            # play sound
            raylib.PlaySound(sound)

        # Fire bullet if the spacebar is pressed
        if self._keyboard_service.is_key_down('space'):
            bullet.create_bullet(cast)
            # play sound
            # raylib.PlaySound(sound)   # Can be commented or uncommented if desired, depending on desire for more sounds.

       
       