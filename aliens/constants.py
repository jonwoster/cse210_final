from game.shared.color import Color



CELL_SIZE = 15
MAX_X = 900
MAX_Y = 600
MIN_Y = 0 # set min Y to be used for making bullets go away
FRAME_RATE = 5
FONT_SIZE = 19
COLUMNS = int(MAX_X/CELL_SIZE)   # Columns * cell size = MAX_X
ROWS = int(MAX_Y/FONT_SIZE)     # Rows * cell size = MAX_Y
CAPTION = "Alien Invasion"
WHITE = Color(255, 255, 255)
RED = Color(255, 0, 0)
YELLOW = Color(255, 255, 0)
GREEN = Color(0, 255, 0)
BLUE = Color(0, 0, 255)
SCORE_X = 350   # x component for where score is displayed
SCORE_Y = 5     # y component for where score is displayed
RT = 'rt'    # right direction arrow
LT = 'lt'     # left direction arrow
MAX_ALIEN_ROWS = 1  # how many rows of aliens to create