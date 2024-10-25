"""Unit tests for the RaceManager class."""

import pytest
import threading
from src.game.race_manager import RaceManager
from src.utils.constants import NUM_CARS

class TestRaceManager:
    @pytest.fixture
    def race_manager(self):
        """Create a fresh RaceManager instance for each test."""
        return RaceManager(NUM_CARS)

    def test_race_manager_initialization(self, race_manager):
        """Test race manager initialization."""
        assert len(race_manager.cars) == 0
        assert len(race_manager.car_threads) == 0
        assert not race_manager.race_active
        assert race_manager.winner is None
        
    def test_create_cars(self, race_manager):
        """Test car creation."""
        race_manager.create_cars(NUM_CARS)
        assert len(race_manager.cars) == NUM_CARS
        assert len(race_manager.car_threads) == NUM_CARS
        
    def test_race_start_stop(self, race_manager):
        """Test race start and stop."""
        race_manager.create_cars(NUM_CARS)
        race_manager.start_race()
        assert race_manager.race_active
        
        race_manager.stop_race()
        assert not race_manager.race_active
        
    def test_pause_resume(self, race_manager):
        """Test race pause and resume."""
        race_manager.create_cars(NUM_CARS)
        race_manager.start_race()
        
        race_manager.pause_race()
        assert all(car.paused for car in race_manager.cars)
        
        race_manager.resume_race()
        assert all(not car.paused for car in race_manager.cars)
        
    def test_reset_race(self, race_manager):
        """Test race reset."""
        race_manager.create_cars(NUM_CARS)
        race_manager.start_race()
        
        # Move cars forward
        for car in race_manager.cars:
            car.position = 0.5
            
        race_manager.reset_cars()
        assert all(car.position == 0.0 for car in race_manager.cars)
        assert race_manager.winner is None