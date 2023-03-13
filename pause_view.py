import arcade
import window


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
        arcade.draw_lrwh_rectangle_textured(0, 0,
                                            window.WIDTH, window.HEIGHT,
                                            self.game_view.background)
        self.game_view.all_sprites_list.draw()

        # draw an orange filter over him
        arcade.draw_lrtb_rectangle_filled(left=0,
                                          right=window.WIDTH,
                                          top=window.HEIGHT,
                                          bottom=0,
                                          color=arcade.color.ORANGE + (150,))

        arcade.draw_text("PAUSED", window.CENTER_X, window.CENTER_Y + 50,
                         arcade.color.BLACK, font_size=50, anchor_x="center")

        # Show tip to return or reset
        arcade.draw_text("Press Esc. to return",
                         window.CENTER_X,
                         window.CENTER_Y,
                         arcade.color.BLACK,
                         font_size=20,
                         anchor_x="center")

    def on_key_press(self, key, _modifiers):
        if key == arcade.key.ESCAPE:   # resume game
            self.window.show_view(self.game_view)

