import pygame
from src.utils.constants import WINDOW_WIDTH, WINDOW_HEIGHT, FPS
from .renderer import GameRenderer
from .utils import draw_text, create_button, Button

class GameWindow:
    def __init__(self, screen):
        """Initialize the game window."""
        self.screen = screen
        self.renderer = GameRenderer(screen)
        self.clock = pygame.time.Clock()
        
        # UI elements
        self.buttons = {
            'start': Button(
                text="Start",
                position=(WINDOW_WIDTH - 100, WINDOW_HEIGHT - 50),
                size=(80, 30)
            ),
            'reset': Button(
                text="Reset",
                position=(WINDOW_WIDTH - 200, WINDOW_HEIGHT - 50),
                size=(80, 30)
            )
        }
        
        # Game state
        self.paused = False
        self.show_fps = True
        self.fps_counter = 0
        self.last_time = pygame.time.get_ticks()
        
    def render(self, cars=None, race_active=False, paused=False):
        """Render the game state."""
        # Clear screen
        self.screen.fill((255, 255, 255))  # White background
        
        # Draw track
        self.renderer.draw_track()
        
        # Draw cars
        if cars:
            self.renderer.draw_cars(cars)
        
        # Draw UI elements
        self._draw_ui(race_active, paused)
        
        # Update display
        pygame.display.flip()
        self.clock.tick(FPS)
        
    def _draw_ui(self, race_active, paused):
        """Draw UI elements."""
        # Draw buttons
        for button in self.buttons.values():
            button.draw(self.screen)
            
        # Draw game state
        if paused:
            draw_text(
                self.screen,
                "PAUSED",
                (WINDOW_WIDTH // 2, 30),
                color=(255, 0, 0)
            )
            
        # Draw FPS counter
        if self.show_fps:
            current_time = pygame.time.get_ticks()
            if current_time - self.last_time > 1000:
                self.fps_counter = self.clock.get_fps()
                self.last_time = current_time
            draw_text(
                self.screen,
                f"FPS: {int(self.fps_counter)}",
                (50, 30),
                color=(0, 0, 0)
            )
            
    def show_winner(self, winner):
        """Display the winner message."""
        draw_text(
            self.screen,
            f"Player {winner + 1} Wins!",
            (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2),
            color=(0, 255, 0),
            size=48
        )
        pygame.display.flip()