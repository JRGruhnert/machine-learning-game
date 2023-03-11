import arcade
import arcade.gui

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Machine learning game"
BACKGROUND_COLOR = arcade.csscolor.GREEN


class MyGame(arcade.Window):

    def __init__(self):

        # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)


        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        arcade.set_background_color(BACKGROUND_COLOR)


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





    def on_click_start(self, event):
        print("Start:", event)

    def on_click_train(self, event):
        print("Train:", event)


    def setup(self):
        """Set up the game here. Call this function to restart the game."""
        pass

    def on_draw(self):
        """Render the screen."""

        self.clear()
        # Code to draw the screen goes here
        self.manager.draw()


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()