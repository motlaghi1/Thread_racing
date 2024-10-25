"""Game constants and configuration values."""

# Window Settings
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FPS = 60

# Track Settings
TRACK_MARGIN = 50
TRACK_WIDTH = WINDOW_WIDTH - (2 * TRACK_MARGIN)
TRACK_HEIGHT = WINDOW_HEIGHT - (2 * TRACK_MARGIN)
NUM_LANES = 4
TRACK_LENGTH = 1.0  # Normalized track length

# Car Settings
NUM_CARS = 4
MIN_SPEED = 0.001        # Minimum movement per frame
MAX_SPEED = 0.003        # Maximum normal speed
MAX_BOOST_SPEED = 0.005  # Maximum speed with boost
ACCELERATION_RATE = 0.0001  # How quickly car speeds up
COLLISION_THRESHOLD = 0.05  # Minimum distance between cars

# Colors (RGB)
COLORS = {
    'WHITE': (255, 255, 255),
    'BLACK': (0, 0, 0),
    'RED': (255, 0, 0),
    'GREEN': (0, 255, 0),
    'BLUE': (0, 0, 255),
    'YELLOW': (255, 255, 0),
    'GRAY': (128, 128, 128),
    'LIGHT_GRAY': (200, 200, 200),
}

# UI Settings
BUTTON_HEIGHT = 40
BUTTON_WIDTH = 120
FONT_SIZE = 36
SMALL_FONT_SIZE = 24
LARGE_FONT_SIZE = 48

# Game States
GAME_STATES = {
    'MENU': 'menu',
    'RUNNING': 'running',
    'PAUSED': 'paused',
    'FINISHED': 'finished'
}

# File paths
ASSETS_PATH = 'assets/'
SOUNDS_PATH = ASSETS_PATH + 'sounds/'
IMAGES_PATH = ASSETS_PATH + 'images/'