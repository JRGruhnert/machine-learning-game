import arcade
import arcade.gui

from moving_object import Agent

# game const
class GameField():
    def __init__(self, center_x, center_y, width, height):
        self.center_x = center_x
        self.center_y = center_y
        self.width = width
        self.height = height
        self.left_border = center_x - (width / 2)
        self.right_border = center_x + (width / 2)
        self.bottom_border = center_y - (height / 2)
        self.top_border = center_y + (height / 2)
        
# const
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800
WINDOW_TITLE = "Machine learning game"
  
GAME_FIELD = GameField(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, WINDOW_WIDTH * 0.6, WINDOW_HEIGHT * 0.6)
BACKGROUND_COLOR = arcade.color.AMAZON
SPRITE_SCALING = 0.5


class Game(arcade.Window):
    def __init__(self):
        # Call the parent class and set up the window
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)


class GameView(arcade.View):
    def __init__(self):
        super().__init__()

        #init all elements
        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/female_person/femalePerson_idle.png",
                                           SPRITE_SCALING)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_sprite.velocity = [3, 3]



        # Variables that will hold sprite lists
        self.all_sprites_list = None
        self.bullet_sprites_list = None

        # Set up the player info
        self.agent_sprite = Agent(":resources:images/animated_characters/female_person/femalePerson_idle.png", SPRITE_SCALING, GAME_FIELD)
        self.seconds_survived = 0.0






    def on_show_view(self):
        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        self.clear()

        arcade.draw_rectangle_outline(GAME_FIELD.center_x, GAME_FIELD.center_y, GAME_FIELD.width + 2, GAME_FIELD.height + 2,
                              arcade.color.BLACK)
        arcade.draw_rectangle_filled(GAME_FIELD.center_x, GAME_FIELD.center_y, GAME_FIELD.width, GAME_FIELD.height,
                              arcade.color.APPLE_GREEN)
        
        # Draw all the sprites.
        self.player_sprite.draw()

        # Show tip to pause screen
        arcade.draw_text("Press Esc. to pause",
                         WINDOW_WIDTH / 2,
                         WINDOW_HEIGHT - 100,
                         arcade.color.BLACK,
                         font_size=20,
                         anchor_x="center")

    def on_update(self, delta_time):
        # Call update on all sprites
        self.player_sprite.update()

        # Bounce off the edges
        if self.player_sprite.left < 0 or self.player_sprite.right > WINDOW_WIDTH:
            self.player_sprite.change_x *= -1
        if self.player_sprite.bottom < 0 or self.player_sprite.top > WINDOW_HEIGHT:
            self.player_sprite.change_y *= -1

    def on_key_press(self, key, _modifiers):
        if key == arcade.key.ESCAPE:
            # pass self, the current view, to preserve this view's state
            pause = PauseView(self)
            self.window.show_view(pause)


class PauseView(arcade.View):
    def __init__(self, game_view):
        super().__init__()
        self.game_view = game_view

    def on_show_view(self):
        arcade.set_background_color(arcade.color.ORANGE)

    def on_draw(self):
        self.clear()

        # Draw player, for effect, on pause screen.
        # The previous View (GameView) was passed in
        # and saved in self.game_view.
        player_sprite = self.game_view.player_sprite
        player_sprite.draw()

        # draw an orange filter over him
        arcade.draw_lrtb_rectangle_filled(left=player_sprite.left,
                                          right=player_sprite.right,
                                          top=player_sprite.top,
                                          bottom=player_sprite.bottom,
                                          color=arcade.color.ORANGE + (200,))

        arcade.draw_text("PAUSED", WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 + 50,
                         arcade.color.BLACK, font_size=50, anchor_x="center")

        # Show tip to return or reset
        arcade.draw_text("Press Esc. to return",
                         WINDOW_WIDTH / 2,
                         WINDOW_HEIGHT / 2,
                         arcade.color.BLACK,
                         font_size=20,
                         anchor_x="center")
        arcade.draw_text("Press Enter to reset",
                         WINDOW_WIDTH / 2,
                         WINDOW_HEIGHT / 2 - 30,
                         arcade.color.BLACK,
                         font_size=20,
                         anchor_x="center")

    def on_key_press(self, key, _modifiers):
        if key == arcade.key.ESCAPE:   # resume game
            self.window.show_view(self.game_view)
        elif key == arcade.key.ENTER:  # reset game
            game = GameView()
            self.window.show_view(game)


class MenuView(arcade.View):
    def on_show_view(self):
        arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)

    def on_draw(self):
        self.clear()
        arcade.draw_text("Menu Screen", WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2,
                         arcade.color.BLACK, font_size=50, anchor_x="center")
        arcade.draw_text("Click to advance.", WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 - 75,
                         arcade.color.GRAY, font_size=20, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game = GameView()
        self.window.show_view(game)


def main():
    window = Game()
    menu = MenuView()
    window.show_view(menu)
    arcade.run()


if __name__ == "__main__":
    main()