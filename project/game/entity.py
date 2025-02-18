import arcade
from game import constants

def load_texture_pair(filename):
    """ used to load a texture pair; second being a mirror image
    """
    return [
        arcade.load_texture(filename),
        arcade.load_texture(filename, flipped_horizontally = True),
    ]

class Entity(arcade.Sprite):
    def __init__(self, name_folder, name_file):
        super().__init__()

        # Default for facing right
        self.facing_direction = constants.RIGHT_FACING

        # Image sequences
        self.cur_texture = 0
        self.scale = constants.CHARACTER_SCALING
        self.character_face_direction = constants.RIGHT_FACING

        main_path = f":resources:images/animated_characters/{name_folder}/{name_file}"

        self.idle_texture_pair = load_texture_pair(f"{main_path}_idle.png")
        self.jump_texture_pair = load_texture_pair(f"{main_path}_jump.png")
        self.fall_texture_pair = load_texture_pair(f"{main_path}_fall.png")

        # Load texture for walking
        self.walk_textures = []
        for i in range(8):
            texture = load_texture_pair(f"{main_path}_walk{i}.png")
            self.walk_textures.append(texture)

        # Load textures for climbing
        self.climbing_textures = []
        texture = arcade.load_texture(f"{main_path}_climb0.png")
        self.climbing_textures.append(texture)
        texture = arcade.load_texture(f"{main_path}_climb1.png")
        self.climbing_textures.append(texture)
        
        # Set the initial texture
        self.texture = self.idle_texture_pair[0]

        # set the hit box
        self.hit_box = self.texture.hit_box_points

class Enemy(Entity):
    def __init__(self, name_folder, name_file):

        # Setup parent class
        super().__init__(name_folder, name_file)
        
class RobotEnemy(Entity):
    def __init__(self, name_folder, name_file):

        # Setup parent class
        super().__init__("robot", "robot")

class ZombieEnemy(Entity):
    def __init__(self, name_folder, name_file):

        # Setup parent class
        super().__init__("zombie", "zombie")

class Player(Entity):

    def __init__(self):
        super().__init__("female_person", "femalePerson") 
        
        # set initial position
        self._center_x = 64
        self._center_y = 128

        # set initial state
        self.jumping = False
        self.climbing = False
        self.is_on_ladder = False
    
    def get_x(self):
        return self._center_x

    def get_y(self):
        return self._center_y



