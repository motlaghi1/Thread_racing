import pygame
from dataclasses import dataclass

@dataclass
class Button:
    """Button class for UI elements."""
    text: str
    position: tuple
    size: tuple
    color: tuple = (100, 100, 100)
    hover_color: tuple = (150, 150, 150)
    text_color: tuple = (255, 255, 255)
    
    def __post_init__(self):
        """Initialize button rect after creation."""
        self.rect = pygame.Rect(
            self.position[0],
            self.position[1],
            self.size[0],
            self.size[1]
        )
        self.font = pygame.font.Font(None, 32)
        self.hovered = False
        
    def draw(self, screen):
        """Draw the button."""
        color = self.hover_color if self.hovered else self.color
        pygame.draw.rect(screen, color, self.rect)
        
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)
        
    def handle_event(self, event):
        """Handle mouse events for the button."""
        if event.type == pygame.MOUSEMOTION:
            self.hovered = self.rect.collidepoint(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.hovered:
                return True
        return False

def draw_text(screen, text, position, color=(0, 0, 0), size=36):
    """Utility function to draw text on screen."""
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=position)
    screen.blit(text_surface, text_rect)

def create_button(text, position, size=(100, 30)):
    """Factory function to create buttons."""
    return Button(text=text, position=position, size=size)