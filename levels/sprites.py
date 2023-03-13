import math
import random
import arcade
import window

HEALTH = 3
SQUARE_SPRITE_FILE = "res/square.png"
CIRCLE_SPRITE_FILE =  "res/circle.png"
SPRITE_SCALING = 0.2
SPACESHIP_SCALING = 0.5
METEOR_SCALING = 0.5

MAX_SPEED = 5
ACCLERATION = 0.4

SPACESHIP_LIST = ["playerShip1_orange.png", "playerShip1_blue.png", "playerShip1_green.png", 
                  "playerShip2_orange.png", "playerShip3_orange.png"]
    
SPACESHIP_LIFE_LIST = ["playerLife1_orange.png", "playerLife1_blue.png", "playerLife1_green.png"]

LASER_LIST = ["laserBlue01.png", "laserRed01.png"]

METEOR_LIST = ["meteorGrey_tiny1.png", "meteorGrey_tiny2.png", "meteorGrey_small1.png", "meteorGrey_small2.png", "meteorGrey_med1.png",
          "meteorGrey_med2.png","meteorGrey_big1.png", "meteorGrey_big2.png", "meteorGrey_big3.png", "meteorGrey_big4.png"]


class Shape(arcade.Sprite):
    def __init__(self, filename):
        super().__init__(filename, SPRITE_SCALING)

        self.change_x = 0
        self.change_y = 0
        self.health = HEALTH
  
    def update(self):

        # Move
        self.center_x += self.change_x
        self.center_y += self.change_y

        # Bounce off the edges
        if self.left < 0 or self.right > window.WIDTH :
            self.change_x *= -1

        if self.bottom < 0 or self.top > window.HEIGHT:
            self.change_y *= -1
            
        
class Square(Shape):
    def __init__(self):
        super().__init__(SQUARE_SPRITE_FILE)

        self.center_x = window.CENTER_X
        self.center_y = window.CENTER_Y
        self.velocity = [3, 3]

    def update(self):
        super().update()

        #calculate if agnet got hit by a bullet
        #if yes game over
        #if no go ahead


class Circle(Shape):
    def __init__(self):
        super().__init__(CIRCLE_SPRITE_FILE)

        self.center_x = window.CENTER_X
        self.center_y = window.CENTER_Y
        self.crossed_border = False

    def update(self):
        super().update()
        
        

class Spaceship(arcade.Sprite):
    def __init__(self):
        super().__init__(":resources:images/space_shooter/" + SPACESHIP_LIST[random.choice(range(0,3))], SPACESHIP_SCALING)

        self.center_x = window.CENTER_X
        self.center_y = window.CENTER_Y
        self.crossed_border = False
        self.angle = 0

    def update(self, direction_x=0, direction_y=0):
        
        # Calculate velocity
        # accleration can be 1, -1 or 0 and the speed has a max of 5
        if(abs(self.change_x + direction_x * ACCLERATION) <= MAX_SPEED):
            self.change_x += direction_x
        
        if(abs(self.change_y + direction_y * ACCLERATION) <= MAX_SPEED):
            self.change_y += direction_y
        
        # Rotate sprite in moving direction
        self.change_angle = math.atan2(self.change_y, self.change_x) * 180 / math.pi
        self.angle = self.change_angle -90
        
        # Move
        self.center_x += self.change_x
        self.center_y += self.change_y

        # Bounce off the edges
        if self.left < 0:
            self.left = 0
        elif self.right > window.WIDTH - 1:
            self.right = window.WIDTH - 1

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > window.HEIGHT - 1:
            self.top = window.HEIGHT - 1

        
        
class Meteor(arcade.Sprite):
    def __init__(self):
        super().__init__(":resources:images/space_shooter/" + random.choice(METEOR_LIST), METEOR_SCALING)

        self.center_x = window.CENTER_X
        self.center_y = window.CENTER_Y
        self.crossed_border = False

    def update(self):
      pass
        
        

