import arcade
from game import constants
from game.coins import Coins
from game.gems import Gems
from game.stone import Stone
from game.crate import Crate
from game.small_platforms import SmallPlatforms
import random

class Helper(arcade.View):
    def __init__(self):
        # call the parent class and setup a window
        super().__init__()
        self.x = None
        self.y = None
    # def create_ground(self, list, length):
    #     counter = 0
    #     length += 300
    #     for x in range(0, length, 60):
    #         if counter < 31 and counter > 27:
    #             counter += 1
    #             continue
    #         self.stone = Stone(x)
    #         list.append(self.stone)
    #         counter += 1

    # def create_coins(self, coordinates, list):
    #     for position in coordinates:
    #         coin = Coins()
    #         coin.position = position
    #         list.append(coin)

    # def create_gems(self, coordinates, list):
    #     for position in coordinates:
    #         gem = Gems()
    #         gem.position = position
    #         list.append(gem)

    # def create_crates(self, coordinates, list):
    #     for position in coordinates:
    #         crate = Crate()
    #         crate.position = position
    #         list.append(crate)

    # def create_small_platforms(self, coordinates, list):
    #     for position in coordinates:
    #         small_platforms = SmallPlatforms()
    #         small_platforms.position = position
    #         list.append(small_platforms)

    #def create_Scene(self, creates, coins, gems):
    def create_Scene(self, creates):
        creates = []
        # coins = []
        # gems = []
        # air_platform = []
        "Create different objects on screen"        
        self.x = 300        #where to start
        self.y = 96
        # # self.creates = [[self.x,self.y]]
        # self.creates.append([self.x, self.y])
        #parts = self.level * 10
        parts = 10
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
                # if (self.y % 2 == 0):
                crate = Crate()
                crate.position = [self.x, self.y]
                creates.append(crate)
                # else:   
                #     small_platforms = SmallPlatforms()
                #     small_platforms.position = [self.x, self.y]
                #     air_platform.append(small_platforms)
                # appears = random.randint(1,2)
                # if appears == 1:
                #     if option == 1:
                #         coin = Coins()
                #         coin.position = [self.x, self.y + 64]
                #         coins.append(coin)
                #     else:
                #         gem = Gems()
                #         gem.position = [self.x, self.y + 64]
                #         gems.append(gem)
                #     self.x += 64
                block += 1            
            times += 1
        counter = 0
        self.x += 300
        for x in range(0, self.x, 60):
            if counter < 31 and counter > 27:
                counter += 1
                continue
            self.stone = Stone(self.x)
            creates.append(self.stone)
            counter += 1
