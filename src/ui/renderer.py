import pygame
from src.utils.constants import (
    WINDOW_WIDTH, WINDOW_HEIGHT, TRACK_MARGIN,
    TRACK_WIDTH, TRACK_HEIGHT, NUM_LANES
)

class GameRenderer:
    def __init__(self, screen):
        """Initialize the renderer."""
        self.screen = screen
        
        # Colors
        self.COLORS = {
            'track': (200, 200, 200),
            'lines': (100, 100, 100),
            'start': (255, 0, 0),
            'finish': (0, 255, 0),
            'car_colors': [
                (255, 0, 0),    # Red
                (0, 0, 255),    # Blue
                (0, 255, 0),    # Green
                (255, 165, 0)   # Orange
            ]
        }
        
    def draw_track(self):
        """Draw the racing track."""
        # Draw track background
        pygame.draw.rect(
            self.screen,
            self.COLORS['track'],
            (
                TRACK_MARGIN,
                TRACK_MARGIN,
                TRACK_WIDTH - (2 * TRACK_MARGIN),
                TRACK_HEIGHT - (2 * TRACK_MARGIN)
            )
        )
        
        # Draw lane lines
        lane_height = (TRACK_HEIGHT - (2 * TRACK_MARGIN)) / NUM_LANES
        for i in range(1, NUM_LANES):
            y = TRACK_MARGIN + (i * lane_height)
            pygame.draw.line(
                self.screen,
                self.COLORS['lines'],
                (TRACK_MARGIN, y),
                (WINDOW_WIDTH - TRACK_MARGIN, y),
                2
            )
            
        # Draw start line
        self._draw_vertical_line(
            TRACK_MARGIN + 20,
            self.COLORS['start'],
            5
        )
        
        # Draw finish line
        self._draw_vertical_line(
            WINDOW_WIDTH - TRACK_MARGIN - 20,
            self.COLORS['finish'],
            5
        )
        
    def draw_cars(self, cars):
        """Draw all cars on the track."""
        for i, car in enumerate(cars):
            # Calculate car position
            x = TRACK_MARGIN + (car.position * (TRACK_WIDTH - 2 * TRACK_MARGIN))
            lane_height = (TRACK_HEIGHT - (2 * TRACK_MARGIN)) / NUM_LANES
            y = TRACK_MARGIN + (i * lane_height) + (lane_height / 2)
            
            # Draw car
            self._draw_car(
                (int(x), int(y)),
                self.COLORS['car_colors'][i % len(self.COLORS['car_colors'])],
                car.boost_active
            )
            
    def _draw_vertical_line(self, x, color, width):
        """Draw a vertical line on the track."""
        pygame.draw.line(
            self.screen,
            color,
            (x, TRACK_MARGIN),
            (x, WINDOW_HEIGHT - TRACK_MARGIN),
            width
        )
        
    def _draw_car(self, position, color, boosting=False):
        """Draw a single car."""
        x, y = position
        # Draw car body
        pygame.draw.circle(self.screen, color, (x, y), 10)
        
        # Draw boost effect if active
        if boosting:
            pygame.draw.circle(self.screen, (255, 255, 0), (x - 15, y), 5)