import random

speed = 3

class Character():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height    

class Monster(Character):
    def __init__(self, x, y, width, height):
        super(Monster, self).__init__(x, y, width, height)
        self.direction = random.randint(1,9)
        self.counter = 0
        self.dead = False

    def update(self):
        self.counter += 1
        if self.counter == 20:
            self.direction = random.randint(1,9)
            self.counter = 0

        if self.direction == 1:
            self.x += speed
        elif self.direction == 2:
            self.x += -speed
        elif self.direction == 3:
            self.y += speed
        elif self.direction == 4:
            self.y += -speed
        elif self.direction == 5:
            self.x -= speed
            self.y -= speed
        elif self.direction == 6:
            self.x += speed
            self.y -= speed
        elif self.direction == 7:
            self.x += speed
            self.y += speed
        elif self.direction == 8:
            self.x -= speed
            self.y += speed

        if self.x >= self.width:
            self.x = 0
        elif self.x <= 0:
            self.x = self.width
        
        if self.y >= self.height:
            self.y = 0
        elif self.y <= 0:
            self.y = self.height

KEY_UP = 273
KEY_DOWN = 274
KEY_LEFT = 276
KEY_RIGHT = 275

class Hero(Character):
    def __init__(self, x, y, width, height):
        super(Hero, self).__init__(x, y, width, height)
        self.speed_x = 0
        self.speed_y = 0

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y
        if self.x <= 32:
            self.x = 32
        elif self.x >= self.height - 32:
            self.x = self.height - 32

        if self.y <= 32:
            self.y = 32
        elif self.y >= self.height - 64:
            self.y = self.height - 64