import arcade


TITLE = "Machine learning game"
WIDTH = 1200
HEIGHT = 800
CENTER_X = WIDTH / 2
CENTER_Y = HEIGHT / 2


class Window(arcade.Window):
    def __init__(self):
        super().__init__(WIDTH, HEIGHT, TITLE)

