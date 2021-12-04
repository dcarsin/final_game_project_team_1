import os

#Screen Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "TEAM 01 ARCADE GAME"
PLATFORM_LENGTH = 2500

#Sprite Constants scaled in relation to the original pics
CHARACTER_SCALING = 1
TILE_SCALING = 0.5

# Player Movement
PLAYER_MOVEMENT_SPEED = 5
GRAVITY = 1
MAX_JUMP_LENGTH = 128
PLAYER_JUMP_SPEED = 20

# Path
PATH = os.path.dirname(os.path.abspath(__file__))
BACKGROUND_MUSIC_PATH = PATH + "/sounds/background.wav"

# Music files
JUMP_SOUND = ":resources:sounds/phaseJump1.wav"
COIN_SOUND = ":resources:sounds/coin1.wav"
GEM_SOUND = ":resources:sounds/coin1.wav"

# Sprites Images
IMAGE_PLAYER = ":resources:images/animated_characters/female_person/femalePerson_idle.png"
GROUND_IMAGE = ":resources:images/tiles/grassMid.png"
COINS_IMAGE = ":resources:images/items/gold_1.png"
GEMS_IMAGE = ":resources:images/items/gemGreen.png"
CRATE_IMAGE = ":resources:images/tiles/boxCrate_double.png"
SMALL_PLATFORMS_IMAGE = ":resources:images/tiles/grassHalf.png"
SIGN_RX_IMAGE = ":resources:images/tiles/signRight.png"
FINAL_FLAG = ":resources:images/items/flagGreen1.png"

# Sprites Coordinates
COINS_COORDINATES = [[256, 150], [512, 150], [900, 150], [965, 150], [1030, 150]]
GEMS_COORDINATES = [[384, 325], [640, 325],[750, 600], [815, 600], [1300, 350]]
CRATES_COORDINATES = [[256, 96], [384, 275], [512, 96], [640, 275], [768, 275], [1300, 96], [1300,155], [1300, 214], [1300, 273], [1235, 96]]
AIR_PLATFORM = [[900, 275], [965, 275], [1030, 275], [500, 450], [565, 450], [750, 550], [815, 550]]
ENEMY_COORDINATES = [[400, 128], [565, 550], [1100, 128]]
# Constants for keeping track if left or right facing
RIGHT_FACING = 0
LEFT_FACING = 1

LAYER_NAME_ENEMIES = "Enemies"

# Timer count
GAME_TIMER_LENGTH = 100 #SECONDS