"""Helper functions for the racing game."""
import math
import random
from .constants import COLORS, WINDOW_WIDTH, WINDOW_HEIGHT

def calculate_distance(pos1, pos2):
    """Calculate distance between two positions."""
    return abs(pos1 - pos2)

def normalize_position(position):
    """Normalize a position to be between 0 and 1."""
    return max(0.0, min(1.0, position))

def generate_random_speed(min_speed, max_speed):
    """Generate a random speed within bounds."""
    return random.uniform(min_speed, max_speed)

def screen_to_track_position(x, y, track_margin):
    """Convert screen coordinates to track position."""
    track_x = (x - track_margin) / (WINDOW_WIDTH - 2 * track_margin)
    track_y = (y - track_margin) / (WINDOW_HEIGHT - 2 * track_margin)
    return normalize_position(track_x), normalize_position(track_y)

def track_to_screen_position(track_x, track_y, track_margin):
    """Convert track position to screen coordinates."""
    screen_x = track_x * (WINDOW_WIDTH - 2 * track_margin) + track_margin
    screen_y = track_y * (WINDOW_HEIGHT - 2 * track_margin) + track_margin
    return screen_x, screen_y

def interpolate(start, end, progress):
    """Interpolate between two values."""
    return start + (end - start) * progress

def format_time(milliseconds):
    """Format time in milliseconds to MM:SS:mmm."""
    minutes = int(milliseconds / 60000)
    seconds = int((milliseconds % 60000) / 1000)
    ms = milliseconds % 1000
    return f"{minutes:02d}:{seconds:02d}:{ms:03d}"

def calculate_placement(positions):
    """Calculate race positions based on car progress."""
    sorted_positions = sorted(enumerate(positions), key=lambda x: x[1], reverse=True)
    placements = [0] * len(positions)
    for place, (car_id, _) in enumerate(sorted_positions, 1):
        placements[car_id] = place
    return placements

def generate_color_gradient(start_color, end_color, steps):
    """Generate a gradient between two colors."""
    gradients = []
    for i in range(steps):
        ratio = i / (steps - 1)
        r = int(start_color[0] * (1 - ratio) + end_color[0] * ratio)
        g = int(start_color[1] * (1 - ratio) + end_color[1] * ratio)
        b = int(start_color[2] * (1 - ratio) + end_color[2] * ratio)
        gradients.append((r, g, b))
    return gradients

# Game state helpers
def is_collision(pos1, pos2, threshold):
    """Check if two positions represent a collision."""
    return calculate_distance(pos1, pos2) < threshold

def calculate_lap_time(start_time, current_time):
    """Calculate lap time in milliseconds."""
    return current_time - start_time

def calculate_speed_modifier(boost_active, drafting):
    """Calculate speed modifier based on conditions."""
    modifier = 1.0
    if boost_active:
        modifier *= 1.5
    if drafting:
        modifier *= 1.2
    return modifier

