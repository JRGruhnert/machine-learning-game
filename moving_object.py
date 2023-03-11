import arcade


class Moving_Object(arcade.Sprite):
     def __init__(self, filename, sprite_scaling, game_bounds):
        super().__init__(filename, sprite_scaling)

        self.game_bounds = game_bounds
        self.change_x = 0
        self.change_y = 0
  
     def update(self):

        # Move the coin
        self.center_x += self.change_x
        self.center_y += self.change_y

        # If we are out-of-bounds, then 'bounce'
        if self.left < self.game_field.left_border:
            self.change_x *= -1

        if self.right > self.game_field.right_border:
            self.change_x *= -1

        if self.bottom < self.game_field.bottom_border:
            self.change_y *= -1

        if self.top > self.game_field.top_border:
            self.change_y *= -1


class Agent(Moving_Object):

    def __init__(self, filename, sprite_scaling, game_bounds):

        super().__init__(filename, sprite_scaling, game_bounds)

        self.center_x = 50
        self.center_y = 50

    def update(self):
        super().update(self)


class Bullet(Moving_Object):

    def __init__(self, filename, sprite_scaling, game_bounds, window_bounds):

        super().__init__(filename, sprite_scaling, game_bounds)

        self.center_x = window_bounds
        self.center_y = 50

    def update(self):
        super().update(self)

