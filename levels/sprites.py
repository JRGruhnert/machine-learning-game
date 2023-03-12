import arcade
from levels import level_const
import window

HEALTH = 3
SQUARE_SPRITE_FILE = ":resources:images/animated_characters/female_person/femalePerson_idle.png"
CIRCLE_SPRITE_FILE =  ":resources:images/animated_characters/female_person/femalePerson_idle.png"
SPRITE_SCALING = 0.5

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
        if self.left < level_const.DZ_LEFT or self.right > level_const.DZ_RIGHT :
            self.change_x *= -1

        if self.bottom < level_const.DZ_BOTTOM or self.top > level_const.DZ_TOP:
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
        
        

