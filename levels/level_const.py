import window


#Dodge Zone Coords

DZ_FACTOR = 0.6
DZ_WIDTH = window.WIDTH * DZ_FACTOR
DZ_HEIGHT = window.HEIGHT * DZ_FACTOR
DZ_LEFT = window.CENTER_X - (DZ_WIDTH / 2)
DZ_RIGHT = window.CENTER_X + (DZ_WIDTH / 2)
DZ_TOP = window.CENTER_Y + (DZ_HEIGHT / 2)
DZ_BOTTOM = window.CENTER_Y - (DZ_HEIGHT / 2)
