# src/game/__init__.py

# Import main classes from their respective modules
from .game_engine import GameEngine, GameState, GameEvent
from .race_manager import RaceManager
from .car import Car
from .track import Track, TrackPoint

# Define what should be available when using "from game import *"
__all__ = [
    'GameEngine',
    'GameState',
    'GameEvent',
    'RaceManager',
    'Car',
    'Track',
    'TrackPoint'
]

# Version information
__version__ = '1.0.0'

# Module level constants and configurations
DEFAULT_NUM_CARS = 4
DEFAULT_NUM_LANES = 4

# Optional: Module initialization code
def initialize_game():
    """Initialize any game module requirements."""
    return {
        'num_cars': DEFAULT_NUM_CARS,
        'num_lanes': DEFAULT_NUM_LANES,
    }

# Optional: Helper functions that work across multiple classes
def create_game_instance(num_cars=DEFAULT_NUM_CARS):
    """
    Create and initialize all necessary game components.
    
    Returns:
        tuple: (GameEngine, RaceManager, Track) instances
    """
    track = Track()
    race_manager = RaceManager(num_cars)
    game_window = None  # This would come from the UI module
    game_engine = GameEngine(race_manager, game_window)
    
    return game_engine, race_manager, track

# Type hints for better IDE support and type checking
GameEngineType = GameEngine
RaceManagerType = RaceManager
CarType = Car
TrackType = Track

# Optional: Module documentation
"""
Racing Game Module
=================

This module provides the core game components for the racing game:

Classes:
    - GameEngine: Main game logic and thread management
    - RaceManager: Manages race state and car coordination
    - Car: Individual car behavior and properties
    - Track: Track layout and position management

Usage:
    from src.game import GameEngine, RaceManager, Car, Track
    
    # Create game components
    track = Track()
    race_manager = RaceManager(num_cars=4)
    game_engine = GameEngine(race_manager, game_window)
    
    # Start game
    game_engine.start_race()
"""