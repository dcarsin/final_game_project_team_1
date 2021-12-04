import arcade
from game import constants
from game.coins import Coins
from game.gems import Gems
from game.stone import Stone
from game.crate import Crate
from game.small_platforms import SmallPlatforms
from game.entity import RobotEnemy
import random

class Helper():
    def __init__(self):
        super().__init__()
        self.x = 0
        self.y = 0
    
    def create_scene(self, creates, coins, gems, robots):
        # creates = []
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
            option = random.randint(1,6)   #even for coins, odd for gems, 5 for enemy
            lenght = random.randint(1,10)   #amounts of blocks together
            block = 0
            if option > 4:
                crate = Crate()
                crate.position = [self.x, self.y]
                creates.append(crate)
                robot = RobotEnemy()
                robot.position = [self.x, self.y + 96]
                robots.append(robot)
            else:                
                while block < lenght:
                    if (self.y % 2 == 0):
                        crate = Crate()
                        crate.position = [self.x, self.y]
                        creates.append(crate)
                    else:   
                        small_platforms = SmallPlatforms()
                        small_platforms.position = [self.x, self.y]
                        creates.append(small_platforms)
                    appears = random.randint(1,2)
                    if appears == 1:
                        if option < 3:
                            coin = Coins()
                            coin.position = [self.x, self.y + 64]
                            coins.append(coin)
                        elif option < 5:
                            gem = Gems()
                            gem.position = [self.x, self.y + 64]
                            gems.append(gem)
                        self.x += 64
                    block += 1            
            times += 1
        return self.x

    def create_ground(self, x_coordinate, creates):
        counter = 0
        x_coordinate += 300
        for x in range(0, x_coordinate, 60):
            if counter < 31 and counter > 27:
                counter += 1
                continue
            self.stone = Stone(x)
            creates.append(self.stone)
            counter += 1import arcade
from game import constants
from game.coins import Coins
from game.gems import Gems
from game.stone import Stone
from game.crate import Crate
from game.small_platforms import SmallPlatforms
from game.entity import RobotEnemy
import random

class Helper():
    def __init__(self):
        super().__init__()
        self.x = 0
        self.y = 0
    
    def create_scene(self, creates, coins, gems, robots):
        # creates = []
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
            option = random.randint(1,6)   #even for coins, odd for gems, 5 for enemy
            lenght = random.randint(1,10)   #amounts of blocks together
            block = 0
            if option > 4:
                crate = Crate()
                crate.position = [self.x, self.y]
                creates.append(crate)
                robot = RobotEnemy()
                robot.position = [self.x, self.y + 96]
                robots.append(robot)
            else:                
                while block < lenght:
                    if (self.y % 2 == 0):
                        crate = Crate()
                        crate.position = [self.x, self.y]
                        creates.append(crate)
                    else:   
                        small_platforms = SmallPlatforms()
                        small_platforms.position = [self.x, self.y]
                        creates.append(small_platforms)
                    appears = random.randint(1,2)
                    if appears == 1:
                        if option < 3:
                            coin = Coins()
                            coin.position = [self.x, self.y + 64]
                            coins.append(coin)
                        elif option < 5:
                            gem = Gems()
                            gem.position = [self.x, self.y + 64]
                            gems.append(gem)
                        self.x += 64
                    block += 1            
            times += 1
        return self.x

    def create_ground(self, x_coordinate, creates):
        counter = 0
        x_coordinate += 300
        for x in range(0, x_coordinate, 60):
            if counter < 31 and counter > 27:
                counter += 1
                continue
            self.stone = Stone(x)
            creates.append(self.stone)
            counter += 1
