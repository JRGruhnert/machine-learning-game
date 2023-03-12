import arcade
from home_view import HomeView
from window import Window


def main():
    window = Window()
    menu = HomeView()
    window.show_view(menu)
    arcade.run()


if __name__ == "__main__":
    main()