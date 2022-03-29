from game.scripting.action import Action


class MoveBulletsAction(Action):
    """
    An update action that moves the bullet actors.
    
    The responsibility of MoveBulletAction is to move the bullet actors that have a velocity greater
    than zero.
    """

    def execute(self, cast, script):
        """Executes the move actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        bullets = cast.get_actors("bullets")
        for actor in bullets:
            actor.move_next()