
"""Unit tests for the Car class."""

import pytest
import threading
from src.game.car import Car
from src.utils.constants import MIN_SPEED, MAX_SPEED

class TestCar:
    @pytest.fixture
    def car(self):
        """Create a fresh car instance for each test."""
        return Car(
            car_id=0,
            position=0.0,
            race_condition=threading.Condition()
        )

    def test_car_initialization(self, car):
        """Test car initialization."""
        assert car.car_id == 0
        assert car.position == 0.0
        assert not car.paused
        assert not car.crashed
        assert not car.boost_active
        
    def test_car_movement(self, car):
        """Test basic car movement."""
        initial_position = car.position
        car.move()
        assert car.position > initial_position
        assert car.position <= 1.0
        
    def test_car_boost(self, car):
        """Test car boost functionality."""
        car.apply_boost(duration=60)
        assert car.boost_active
        assert car.boost_duration == 60
        
        # Move car with boost
        initial_position = car.position
        car.move()
        boosted_movement = car.position - initial_position
        
        # Reset and move without boost
        car.boost_active = False
        car.position = 0.0
        car.move()
        normal_movement = car.position
        
        assert boosted_movement > normal_movement
        
    def test_car_crash(self, car):
        """Test car crash handling."""
        car.crash()
        assert car.crashed
        assert car.current_speed == 0.0
        
        # Try to move while crashed
        initial_position = car.position
        car.move()
        assert car.position == initial_position
        
    def test_car_reset(self, car):
        """Test car reset functionality."""
        car.position = 0.5
        car.crashed = True
        car.boost_active = True
        
        car.reset()
        assert car.position == 0.0
        assert not car.crashed
        assert not car.boost_active
        
    def test_car_pause(self, car):
        """Test car pause functionality."""
        car.toggle_pause()
        assert car.paused
        
        # Try to move while paused
        initial_position = car.position
        car.move()
        assert car.position == initial_position