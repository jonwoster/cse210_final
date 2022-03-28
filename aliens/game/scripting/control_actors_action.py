import constants
from game.scripting.action import Action
from game.shared.point import Point

#import all needed info for sound
import raylib
#initialize audio device
raylib.InitAudioDevice()
#encode file to be read by raylib
sound = raylib.LoadSound("snake\game\sounds\player_sound.wav".encode('ascii'))


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
        player = cast.get_first_actor("player")
        bullet = cast.get_first_actor("bullets")
        # player_position = player.get_position()
        # cycle2 = cast.get_first_actor("cycles2")

        # The default is that the player is not moving
        self._direction = Point(0,0)
        player.set_velocity(self._direction) 

        # Move the player left if they hit the left arrow
        if self._keyboard_service.is_key_down(constants.LT):
            self._direction = Point(-constants.CELL_SIZE, 0)
            player.set_velocity(self._direction)
            #play sound
            raylib.PlaySound(sound)
        
        # Move the player right if they hit the right arrow
        if self._keyboard_service.is_key_down(constants.RT):
            self._direction = Point(constants.CELL_SIZE, 0)
            player.set_velocity(self._direction)
            raylib.PlaySound(sound)

        # Fire bullet if the spacebar is pressed
        if self._keyboard_service.is_key_down('space'):
            bullet.create_bullet(cast)
            for bullet in bullet.bullets:
                # bullet.set_position(player_position)
                self._direction = Point(0, -constants.CELL_SIZE)
                bullet.set_velocity(self._direction)
                # while bullet._is_alive:
                #     bullet._velocity = Point(0, 1+=1)
                # bullet.move_next(Point(0,50))
            raylib.PlaySound(sound)

       
        # left
        # if self._keyboard_service.is_key_down('a'):
        #     self._direction = Point(-constants.CELL_SIZE, 0)
        #     cycle1.turn_head(self._direction)
        #     #play sound
        #     raylib.PlaySound(sound)
        
        # right
        # if self._keyboard_service.is_key_down('d'):
        #     self._direction = Point(constants.CELL_SIZE, 0)
        #     cycle1.turn_head(self._direction)
        #     raylib.PlaySound(sound)
        
        # up
    #     if self._keyboard_service.is_key_down('w'):
    #         self._direction = Point(0, -constants.CELL_SIZE)
    #         cycle1.turn_head(self._direction)
    #         #play sound
    #         raylib.PlaySound(sound)
        
    #     # down
    #     if self._keyboard_service.is_key_down('s'):
    #         self._direction = Point(0, constants.CELL_SIZE)
    #         cycle1.turn_head(self._direction)
    #         #play sound
    #         raylib.PlaySound(sound)
            
            
            

    #    # left
    #     if self._keyboard_service.is_key_down('j'):
    #         self._direction = Point(-constants.CELL_SIZE, 0)
    #         cycle2.turn_head(self._direction)
    #         #play sound
    #         raylib.PlaySound(sound)
        
    #     # right
    #     if self._keyboard_service.is_key_down('l'):
    #         self._direction = Point(constants.CELL_SIZE, 0)
    #         cycle2.turn_head(self._direction)
    #         #play sound
    #         raylib.PlaySound(sound)
        
    #     # up
    #     if self._keyboard_service.is_key_down('i'):
    #         self._direction = Point(0, -constants.CELL_SIZE)
    #         cycle2.turn_head(self._direction)
    #         #play sound
    #         raylib.PlaySound(sound)
        
    #     # down
    #     if self._keyboard_service.is_key_down('k'):
    #         self._direction = Point(0, constants.CELL_SIZE)
    #         cycle2.turn_head(self._direction)
    #         #play sound
    #         raylib.PlaySound(sound)
        

        