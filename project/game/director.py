import math
import arcade
import random
from logging import raiseExceptions
from game.entity import Player
from game import constants
from game.follow_camera import Follow_camera
from game.key_press import UserMovement
from game.drawing import Drawing
from game.do_updates import DoUpdates
from game.score import Score
from game.timer import Timer
from game.helper import Helper
from game.view_over import Game_overView
from game.small_platforms import SmallPlatforms
from game.sign_rx import SignRx
from game.final_flag import FinalFlag
from game.entity import RobotEnemy, ZombieEnemy

class GameView(arcade.View):
    """ This will be the main application class """
    def __init__(self):
        # call the parent class and setup a window
        super().__init__()
        #David coded
        self.level = 1
        self.x = None
        self.y = None
        # self.creates = [[self.x,self.y]]
        self.creates = []
        self.coins = []
        self.gems = []
        self.air_platform = []
        # Initialize game lists
        self.platform_list = None
        self.player_list = None
        self.coin_list = None
        self.gem_list = None
        self.camera = None
        self.gui_camera = None
        self.player_movement = None
        self.drawing = None
        self.do_updates = None
        # Create Sprites
        self.player_sprite = None
        # Create the physics engine
        self.physics_engine = None
        # Create the variable to store the score
        self.score = None
        self.timer = None
        # Create Small Platforms
        self.small_platforms = None
        # Create the helper
        self.helper = None
        # Create the sign
        self.sign_rx = None
        # Create Final Flag
        self.final_flag = None
        # Create the sounds
        self.background_sound = arcade.load_sound(constants.BACKGROUND_MUSIC_PATH)
        self.jump_sound = arcade.load_sound(constants.JUMP_SOUND)
        self.collect_coin_sound = arcade.load_sound(constants.COIN_SOUND)
        self.collect_gem_sound = arcade.load_sound(constants.GEM_SOUND)
        # Set the background and play the sound
        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)
        arcade.play_sound(self.background_sound, 0.1)

    def setup(self): 
        # Setup the helper
        self.helper = Helper()
        # setup camera
        self.camera = Follow_camera(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
        self.gui_camera = arcade.Camera(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
        # Create the Sprites lists
        self.player_list = arcade.SpriteList()
        self.platform_list = arcade.SpriteList(use_spatial_hash=True)
        # Create the player
        self.player_sprite = Player()
        self.player_list.append(self.player_sprite)
        # # Add Enemies
        # enemies_layer = self.tile_map.object_lists[constants.LAYER_NAME_ENEMIES]

        # for my_object in enemies_layer:
        #     cartesian = self.tile_map.get_cartesian(
        #         my_object.shape[0], my_object.shape[1]
        #     )
        #     enemy_type = my_object.properties["type"]
        #     if enemy_type == "robot":
        #         enemy = RobotEnemy()
        #     elif enemy_type == "zombie":
        #         enemie = ZombieEnemy()
        #     else:
        #         raise Exception(f"Unknown enemy type: {enemy_type}")
        #     enemy.center_x = math.floor(
        #         cartesian[0] * constants.TILE_SCALING * self.tile_map.tile_width
        #     )
        #     enemy.center_y = math.floor(
        #         (cartesian[1] + 1) * (self.tile_map.tile_height * constants.TILE_SCALING)
        #     )
        #     self.scene.add_sprite(constants.LAYER_NAME_ENEMIES, enemy)
        # Create the Score and timer
        self.score = Score()
        self.timer = Timer()
        self.create_Scene()
        # Create the ground
        self.helper.create_ground(self.platform_list)
        
        # Adding Crates
        self.helper.create_crates(self.creates, self.platform_list)
        # Create Coins
        self.coin_list = arcade.SpriteList()
        self.helper.create_coins(self.coins, self.coin_list)
        # Create Gems
        self.gem_list = arcade.SpriteList()
        self.helper.create_gems(self.gems, self.gem_list)
        # Create small platforms
        self.small_platforms = SmallPlatforms()
        self.helper.create_small_platforms(self.air_platform, self.platform_list)
        # Adding the sign
        self.sign_rx = SignRx()
        self.sign_list = arcade.SpriteList()
        self.sign_list.append(self.sign_rx)
        # Adding Final Flag
        self.final_flag = FinalFlag()
        self.final_flag_list = arcade.SpriteList()
        self.final_flag_list.append(self.final_flag)
        # Create the 'physics engine'
        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player_sprite, gravity_constant=constants.GRAVITY, walls=self.platform_list
        )
        # Create the movement checker
        self.player_movement = UserMovement()
        # Create the update object
        self.do_updates = DoUpdates(self.player_sprite, self.physics_engine, self.camera, self.score, self.timer)

    def on_draw(self):
        """ Draw all the elements on the screen """
        self.drawing = Drawing()
        self.drawing.use_camera(self.camera)
        self.drawing.draw_objects(self.sign_list,self.final_flag_list, self.player_list, self.platform_list, self.coin_list, self.gem_list)
        # Activate the GUI camera before drawing GUI elements
        self.drawing.use_camera(self.gui_camera)
        self.drawing.draw_gui(self.score)
        self.drawing.draw_gui_timer(self.timer)

    def on_key_press(self, key, modifiers):
        """Update the player's movement on key press"""
        self.player_movement.movement(key, modifiers, self.player_sprite, self.physics_engine, self.jump_sound)

    def on_key_release(self, key, modifiers):
        """Update the player's movement on key release"""
        self.player_movement.movement_stop(key, modifiers, self.player_sprite)
        
    def on_update(self, delta_time):
        self.timer.add_time(delta_time)
        if self.timer.timer <= 0:
            view = Game_overView()
            self.window.show_view(view)
        """Movement and game logic"""
        # Update the physics engine and camera
        self.do_updates.do_updates()
        # Process the coin hit
        self.do_updates.check_prop_collision(self.coin_list, self.collect_coin_sound)
         # Process the gem hit
        self.do_updates.check_prop_collision(self.gem_list, self.collect_gem_sound)
        # Check falling
        self.do_updates.check_falling(self.player_sprite)
        # Process final flag
        self.do_updates.check_flag_collision(self.final_flag_list, self.setup)

    def create_Scene(self):
        self.creates = []
        self.coins = []
        self.gems = []
        self.air_platform = []
        "Create different objects on screen"        
        self.x = 300        #where to start
        self.y = 96
        # # self.creates = [[self.x,self.y]]
        # self.creates.append([self.x, self.y])
        parts = self.level * 10
        times = 0
        while times < parts:
            last_x = self.x
            last_y = self.y
            self.x = random.randint(last_x + 64, (last_x + 200))
            self.y = random.randint(96, (last_y + constants.MAX_JUMP_LENGTH))
            option = random.randint(1, 2)   #1 for coins, 2 for gems
            lenght = random.randint(1,10)   #amounts of blocks together
            block = 0
            while block < lenght:
                if (self.y % 2 == 0):
                    self.creates.append([self.x, self.y])
                else:                    
                    self.air_platform.append([self.x, self.y])
                appears = random.randint(1,2)
                if appears == 1:
                    if option == 1:
                        self.coins.append([self.x, self.y + 64])
                    else:
                        self.gems.append([self.x, self.y + 64])
                    self.x += 64
                block += 1            
            times += 1
        counter = 0


