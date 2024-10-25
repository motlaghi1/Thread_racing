# src/ui/__init__.py

# Import main classes from their respective modules
from .game_window import GameWindow
from .renderer import GameRenderer
from .utils import Button, draw_text, create_button

# Define what should be available when using "from ui import *"
__all__ = [
    'GameWindow',
    'GameRenderer',
    'Button',
    'draw_text',
    'create_button',
    'initialize_ui',
    'create_game_window'
]

# Version information
__version__ = '1.0.0'

# Module level constants (these can be imported directly from constants.py instead)
DEFAULT_BUTTON_SIZE = (100, 30)
DEFAULT_FONT_SIZE = 36

def initialize_ui():
    """
    Initialize UI requirements and pygame.
    Returns initialization status and screen object.
    """
    import pygame
    from src.utils.constants import WINDOW_WIDTH, WINDOW_HEIGHT
    
    # Initialize pygame
    pygame.init()
    
    # Set up the display
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Racing Game")
    
    return {
        'screen': screen,
        'initialized': True,
        'pygame_version': pygame.version.ver
    }

def create_game_window(screen=None):
    """
    Factory function to create a game window instance.
    If screen is not provided, creates a new one.
    """
    if screen is None:
        init_data = initialize_ui()
        screen = init_data['screen']
    
    return GameWindow(screen)

# Type hints for better IDE support
GameWindowType = GameWindow
GameRendererType = GameRenderer
ButtonType = Button

# Optional: Clean up function
def cleanup_ui():
    """Clean up UI resources."""
    import pygame
    pygame.quit()

# Module documentation
"""
Racing Game UI Module
====================

This module provides the user interface components for the racing game:

Classes:
    - GameWindow: Main window management and rendering
    - GameRenderer: Handles all game rendering
    - Button: UI button implementation

Functions:
    - draw_text: Utility function for rendering text
    - create_button: Factory function for creating buttons
    - initialize_ui: Set up UI system
    - create_game_window: Create main game window
    - cleanup_ui: Clean up resources

Usage:
    from src.ui import initialize_ui, create_game_window
    
    # Initialize UI
    ui_data = initialize_ui()
    
    # Create game window
    game_window = create_game_window(ui_data['screen'])
    
    # Create UI elements
    button = create_button("Start", (100, 100))
    
    # Clean up
    cleanup_ui()
"""

# Example usage function
def example_usage():
    """Example of how to use the UI module."""
    # Initialize UI
    ui_data = initialize_ui()
    
    # Create game window
    game_window = create_game_window(ui_data['screen'])
    
    # Create some buttons
    start_button = create_button("Start", (100, 100))
    reset_button = create_button("Reset", (200, 100))
    
    # Main loop example
    import pygame
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        # Update and render
        game_window.render()
        
    # Clean up
    cleanup_ui()