import arcade
import arcade.gui
import const

from moving_object import Spaceship

class Game(arcade.Window):
    def __init__(self):
        # Call the parent class and set up the window
        super().__init__(const.WIN_WIDTH, const.WIN_HEIGHT, const.WINDOW_TITLE)


class GameView(arcade.View):
    def __init__(self):
        super().__init__()

        #init all elements
        self.ai_sprite = Spaceship()
        self.background = arcade.load_texture(":resources:images/backgrounds/abstract_1.jpg")
        x_factor = self.background.width / const.WIN_WIDTH
        y_factor = self.background.height / const.WIN_HEIGHT
        self.background_inner = arcade.load_texture(":resources:images/backgrounds/abstract_1.jpg", 
                                                    const.DZ_LEFT * x_factor, const.DZ_BOTTOM * y_factor, const.DZ_WIDTH * x_factor, const.DZ_HEIGHT * y_factor)
        #init gui elements
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        # Render button
        default_style = {
            "font_name": ("calibri", "arial"),
            "font_size": 15,
            "font_color": arcade.color.WHITE,
            "border_width": 2,
            "border_color": None,
            "bg_color": (21, 19, 21),

            # used if button is pressed
            "bg_color_pressed": arcade.color.WHITE,
            "border_color_pressed": arcade.color.WHITE,  # also used when hovered
            "font_color_pressed": arcade.color.BLACK,
        }

        red_style = {
            "font_name": ("calibri", "arial"),
            "font_size": 15,
            "font_color": arcade.color.WHITE,
            "border_width": 2,
            "border_color": None,
            "bg_color": arcade.color.REDWOOD,

            # used if button is pressed
            "bg_color_pressed": arcade.color.WHITE,
            "border_color_pressed": arcade.color.RED,  # also used when hovered
            "font_color_pressed": arcade.color.RED,
        }


        
         # Create a vertical BoxGroup to align buttons
        self.h_box = arcade.gui.UIBoxLayout(vertical=False)

        # Create the buttons
        start_button = arcade.gui.UIFlatButton(text="Start", width=200, style=default_style)
        self.h_box.add(start_button.with_space_around(bottom=20, right= 10, left=10, top=20))

        train_button = arcade.gui.UIFlatButton(text="Train", width=200, style=red_style)
        self.h_box.add(train_button.with_space_around(bottom=20, right= 10, left=10, top=20))

        # assign  callback
        start_button.on_click = self.on_click_start
        train_button.on_click = self.on_click_train

     
        # Create a widget to hold the v_box widget, that will center the buttons
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="bottom",
                child=self.h_box)
        )



        # Variables that will hold sprite lists
        self.all_sprites_list = None
        self.bullet_sprites_list = None

        # Set up the player info
        self.seconds_survived = 0.0

    def on_show_view(self):
        arcade.set_background_color(arcade.color.BLACK)
        
    def on_draw(self):
        self.clear()
        
        #draw background
        arcade.draw_lrwh_rectangle_textured(0, 0, const.WIN_WIDTH, const.WIN_HEIGHT, self.background, alpha=100)
        arcade.draw_rectangle_outline(const.WIN_CENTER_X, const.WIN_CENTER_Y, const.DZ_WIDTH + 2, const.DZ_HEIGHT + 2,
                              arcade.color.BLACK)
        arcade.draw_lrwh_rectangle_textured(const.DZ_LEFT, const.DZ_BOTTOM, const.DZ_WIDTH, const.DZ_HEIGHT, self.background_inner)
        #arcade.draw_rectangle_filled(const.WIN_CENTER_X, const.WIN_CENTER_Y, const.DZ_WIDTH, const.DZ_HEIGHT , [255,255,255,50])
        
        # Draw all the sprites.
        self.ai_sprite.draw()

        # Draw ui on top of everything
        self.manager.draw()
        arcade.draw_text("Press Esc. to pause",
                         const.WIN_CENTER_X,
                         const.WIN_HEIGHT - 100,
                         arcade.color.BLACK,
                         font_size=20,
                         anchor_x="center")

    def on_update(self, delta_time):
        # Call update on all sprites
        self.ai_sprite.update()
        

    def on_key_press(self, key, _modifiers):
        if key == arcade.key.ESCAPE:
            # pass self, the current view, to preserve this view's state
            pause = PauseView(self)
            self.window.show_view(pause)


    def on_click_start(self, event):
        print("Start:", event)

    def on_click_train(self, event):
        print("Train:", event)


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
        ai_sprite = self.game_view.ai_sprite
        ai_sprite.draw()

        # draw an orange filter over him
        arcade.draw_lrtb_rectangle_filled(left=ai_sprite.left,
                                          right=ai_sprite.right,
                                          top=ai_sprite.top,
                                          bottom=ai_sprite.bottom,
                                          color=arcade.color.ORANGE + (200,))

        arcade.draw_text("PAUSED", const.WIN_CENTER_X, const.WIN_CENTER_Y + 50,
                         arcade.color.BLACK, font_size=50, anchor_x="center")

        # Show tip to return or reset
        arcade.draw_text("Press Esc. to return",
                         const.WIN_CENTER_X,
                         const.WIN_CENTER_Y,
                         arcade.color.BLACK,
                         font_size=20,
                         anchor_x="center")
        arcade.draw_text("Press Enter to reset",
                         const.WIN_CENTER_X,
                         const.WIN_CENTER_Y - 30,
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
        arcade.draw_text("Menu Screen", const.WIN_CENTER_X, const.WIN_CENTER_Y,
                         arcade.color.BLACK, font_size=50, anchor_x="center")
        arcade.draw_text("Click to advance.", const.WIN_CENTER_X, const.WIN_CENTER_Y - 75,
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