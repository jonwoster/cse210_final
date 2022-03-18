from game.shared.color import Color



CELL_SIZE = 30
MAX_X = 1200
MAX_Y = 900
FRAME_RATE = 5
FONT_SIZE = 30
COLUMNS = int(MAX_X/CELL_SIZE)   # Columns * cell size = MAX_X
ROWS = int(MAX_Y/FONT_SIZE)     # Rows * cell size = MAX_Y
CAPTION = "Alien Invasion"
CYCLE_LENGTH = 1
WHITE = Color(255, 255, 255)
RED = Color(255, 0, 0)
YELLOW = Color(255, 255, 0)
GREEN = Color(0, 255, 0)
BLUE = Color(0, 0, 255)
SCORE_X = 350   # x component for where score is displayed
SCORE_Y = 5     # y component for where score is displayed
RT = 'rt'    # right direction arrow
LT = 'lt'     # left direction arrow