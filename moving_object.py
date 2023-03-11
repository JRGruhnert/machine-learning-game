import arcade
import const

HEALTH = 3
SPACESHIP_SPRITE_FILE = ":resources:images/animated_characters/female_person/femalePerson_idle.png"
METEOR_SPRITE_FILE =  ":resources:images/animated_characters/female_person/femalePerson_idle.png"
SPRITE_SCALING = 0.5

class Moving_Object(arcade.Sprite):
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
        if self.left < const.DZ_LEFT or self.right > const.DZ_RIGHT :
            self.change_x *= -1

        if self.bottom < const.DZ_BOTTOM or self.top > const.DZ_TOP:
            self.change_y *= -1
            
        


class Spaceship(Moving_Object):
    def __init__(self):
        super().__init__(SPACESHIP_SPRITE_FILE)

        self.center_x = const.WIN_CENTER_X
        self.center_y = const.WIN_CENTER_Y
        self.velocity = [3, 3]

    def update(self):
        super().update()

        #calculate if agnet got hit by a bullet
        #if yes game over
        #if no go ahead


class Meteor(Moving_Object):
    def __init__(self):
        super().__init__(METEOR_SPRITE_FILE)

        self.center_x = const.WIN_CENTER_X
        self.center_y = const.WIN_CENTER_Y
        self.crossed_border = False

    def update(self):
        super().update()
        
        

