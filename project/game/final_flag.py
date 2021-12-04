import arcade
from game import constants

class FinalFlag(arcade.Sprite):
    def __init__(self):
        super().__init__(constants.SIGN_RX_IMAGE, constants.TILE_SCALING)
        self.center_x = 0
        self.center_y = 96
    
    def set_position(self, x):
        """Updates the actor's position to the given one.
        
        Args:
            self (Actor): An instance of Actor.
            position (Point): The given position.
        """
        self.center_x = x
