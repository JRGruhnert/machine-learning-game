import arcade
from arcade import gui
from levels import sprites
from levels import level_const
from pause_view import PauseView

import window
import styles


class LevelOne(arcade.View):
    def __init__(self):
        super().__init__()

        #init all elements
        self.ai_sprite = sprites.Square()
        self.background = arcade.load_texture(":resources:images/backgrounds/abstract_1.jpg")
        x_factor = self.background.width / window.WIDTH
        y_factor = self.background.height / window.HEIGHT
        self.background_inner = arcade.load_texture(":resources:images/backgrounds/abstract_1.jpg", 
                                                    level_const.DZ_LEFT * x_factor, level_const.DZ_BOTTOM * y_factor, level_const.DZ_WIDTH * x_factor, level_const.DZ_HEIGHT * y_factor)
        #init gui elements
        self.manager = arcade.gui.UIManager()
        self.manager.enable()


        
         # Create a vertical BoxGroup to align buttons
        self.h_box = arcade.gui.UIBoxLayout(vertical=False)

        # Create the buttons
        start_button = arcade.gui.UIFlatButton(text="Start", width=200, style=styles.button_default_style)
        self.h_box.add(start_button.with_space_around(bottom=20, right= 10, left=10, top=20))

        train_button = arcade.gui.UIFlatButton(text="Train", width=200, style=styles.button_red_style)
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
        arcade.draw_lrwh_rectangle_textured(0, 0, window.WIDTH, window.HEIGHT, self.background, alpha=100)
        arcade.draw_rectangle_outline(window.CENTER_X, window.CENTER_Y, level_const.DZ_WIDTH + 2, level_const.DZ_HEIGHT + 2,
                              arcade.color.BLACK)
        arcade.draw_lrwh_rectangle_textured(level_const.DZ_LEFT, level_const.DZ_BOTTOM, level_const.DZ_WIDTH, level_const.DZ_HEIGHT, self.background_inner)
        #arcade.draw_rectangle_filled(const.WIN_CENTER_X, const.WIN_CENTER_Y, const.DZ_WIDTH, const.DZ_HEIGHT , [255,255,255,50])
        
        # Draw all the sprites.
        self.ai_sprite.draw()

        # Draw ui on top of everything
        self.manager.draw()
        arcade.draw_text("Press Esc. to pause",
                         window.CENTER_X,
                         window.HEIGHT - 100,
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

