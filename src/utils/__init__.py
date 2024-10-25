
"""Utilities module for the racing game."""

# Import all constants
from .constants import *

# Import helper functions
from .helpers import (
    calculate_distance,
    normalize_position,
    generate_random_speed,
    screen_to_track_position,
    track_to_screen_position,
    interpolate,
    format_time,
    calculate_placement,
    generate_color_gradient,
    is_collision,
    calculate_lap_time,
    calculate_speed_modifier
)

# Define what should be available when using "from utils import *"
__all__ = [
    # Constants
    'WINDOW_WIDTH',
    'WINDOW_HEIGHT',
    'FPS',
    'TRACK_MARGIN',
    'NUM_LANES',
    'NUM_CARS',
    'COLORS',
    'GAME_STATES',
    # Helper functions
    'calculate_distance',
    'normalize_position',
    'generate_random_speed',
    'screen_to_track_position',
    'track_to_screen_position',
    'interpolate',
    'format_time',
    'calculate_placement',
    'generate_color_gradient',
    'is_collision',
    'calculate_lap_time',
    'calculate_speed_modifier'
]

# Version information
__version__ = '1.0.0'

# Utility function to verify all constants are properly defined
def verify_constants():
    """Verify that all required constants are defined and valid."""
    required_constants = [
        'WINDOW_WIDTH',
        'WINDOW_HEIGHT',
        'FPS',
        'TRACK_MARGIN',
        'NUM_LANES',
        'NUM_CARS'
    ]
    
    missing = []
    for const in required_constants:
        if not hasattr(constants, const):
            missing.append(const)
            
    if missing:
        raise ValueError(f"Missing required constants: {', '.join(missing)}")
    
    return True

# Module documentation
"""
Racing Game Utils Module
=======================

This module provides utility functions and constants for the racing game:

Constants:
    - Window dimensions and FPS
    - Track settings
    - Car parameters
    - Colors and UI settings
    - Game states

Helper Functions:
    - Position calculations
    - Time formatting
    - Collision detection
    - Color manipulation
    - Game state helpers

Usage:
    from src.utils import WINDOW_WIDTH, WINDOW_HEIGHT
    from src.utils.helpers import calculate_distance
    
    # Use constants
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    
    # Use helper functions
    distance = calculate_distance(pos1, pos2)
"""