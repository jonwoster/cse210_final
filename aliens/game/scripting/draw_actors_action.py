from game.scripting.action import Action


class DrawActorsAction(Action):
    """
    An output action that draws all the actors.
    
    The responsibility of DrawActorsAction is to draw all the actors.

    Attributes:
        _video_service (VideoService): An instance of VideoService.
    """

    def __init__(self, video_service):
        """Constructs a new DrawActorsAction using the specified VideoService.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service

    def execute(self, cast, script):
        """Executes the draw actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        # get element info to be drawn
        _player = cast.get_first_actor("player")
        _score = cast.get_first_actor("scores")
        _messages = cast.get_actors("messages")
        _alien = cast.get_first_actor("aliens")
        _aliens = _alien.get_aliens()
        _bullet =cast.get_first_actor("bullets")
        _bullets = _bullet.get_bullets()

        # draw elements on GUI
        self._video_service.clear_buffer()
        self._video_service.draw_actor(_player)
        self._video_service.draw_actor(_score)
        self._video_service.draw_actors(_messages, True)
        self._video_service.draw_actors(_aliens)
        self._video_service.draw_actors(_bullets)
        self._video_service.flush_buffer()