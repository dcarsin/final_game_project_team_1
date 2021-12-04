import math
from logging import raiseExceptions
import arcade
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
from game.entity import RobotEnemy
import random

class GameView(arcade.View):
    """ This will be the main application class """
    def __init__(self):
        # call the parent class and setup a window
        super().__init__()
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
        # Create Enemy List
        self.robot_enemy_list = None
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

        # Create enemies
        self.robot_enemy_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.gem_list = arcade.SpriteList()
        # Create the Score and timer
        self.score = Score()
        self.timer = Timer()
        # Create the ground
        # Adding Crates
        self.x = self.helper.create_scene(self.platform_list, self.coin_list, self.gem_list, self.robot_enemy_list)
        self.helper.create_ground(self.x, self.platform_list)
        # Adding the sign
        self.sign_rx = SignRx()
        self.sign_list = arcade.SpriteList()
        self.sign_list.append(self.sign_rx)
        # Adding Final Flag
        self.final_flag = FinalFlag()
        self.final_flag_list = arcade.SpriteList()
        self.final_flag.set_position(self.x + 300)
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
        self.drawing.draw_objects(self.sign_list,self.final_flag_list, self.player_list, self.robot_enemy_list, self.platform_list, self.coin_list, self.gem_list)
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
        self.do_updates.check_falling()
        # Process final flag
        self.do_updates.check_flag_collision(self.final_flag_list, self.setup)
        # Update Animation
        self.do_updates.update_animation()
        # Check collision with enemies
        self.do_updates.check_collision_enemies(self.robot_enemy_list, self.setup)

        



    
