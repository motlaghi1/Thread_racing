import pytest
import pygame
from src.utils.constants import WINDOW_WIDTH, WINDOW_HEIGHT

@pytest.fixture(scope="session")
def pygame_instance():
    """Initialize pygame for tests that require it."""
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    yield screen
    pygame.quit()

@pytest.fixture
def mock_track():
    """Create a mock track for testing."""
    from src.game.track import Track
    return Track()

@pytest.fixture
def mock_car():
    """Create a mock car for testing."""
    from src.game.car import Car
    import threading
    return Car(car_id=0, position=0.0, race_condition=threading.Condition())
