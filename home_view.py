import arcade
import window

from levels import level


class HomeView(arcade.View):
    def on_show_view(self):
        arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)

    def on_draw(self):
        self.clear()
        arcade.draw_text("Menu Screen", window.CENTER_X, window.CENTER_Y,
                         arcade.color.BLACK, font_size=50, anchor_x="center")
        arcade.draw_text("Click to advance.", window.CENTER_X, window.CENTER_Y - 75,
                         arcade.color.GRAY, font_size=20, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game = level.LevelOne()
        self.window.show_view(game)
