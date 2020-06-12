import random

class Monster():
    def __init__(self, x, y, direction, counter, width, height):
        self.x = x
        self.y = y
        self.direction = direction
        self.counter = 0
        self.width = width
        self.height = height

    def move(self):
        self.counter += 1
        if self.counter == 20:
            self.direction = random.randint(1,5)
            self.counter = 0

        if self.direction == 1:
            self.x += 2
        elif self.direction == 2:
            self.x += -2
        elif self.direction == 3:
            self.y += 2
        elif self.direction == 4:
            self.y += -2
        
        if self.x >= self.width:
            self.x = 0
        elif self.x <= 0:
            self.x = self.width
        
        if self.y >= self.height:
            self.y = 0
        elif self.y <= 0:
            self.y = self.height
        