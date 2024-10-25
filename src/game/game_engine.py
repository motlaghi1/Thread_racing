# src/game/game_engine.py
import threading
from src.utils.constants import NUM_CARS

class GameEngine:
    def __init__(self, race_manager, game_window):
        """Initialize the game engine."""
        self.race_manager = race_manager
        self.game_window = game_window
        self.running = False
        self.paused = False
        self.lock = threading.Lock()
        
    def start_race(self):
        """Start a new race."""
        with self.lock:
            if not self.running:
                self.running = True
                self.paused = False
                # Initialize cars and their threads
                self.race_manager.create_cars(NUM_CARS)
                # Start car threads
                self.race_manager.start_race()
                
    def reset_race(self):
        """Reset the race state."""
        with self.lock:
            self.running = False
            self.paused = False
            # Stop all car threads and reset positions
            self.race_manager.stop_race()
            self.race_manager.reset_cars()
            
    def toggle_pause(self):
        """Toggle the pause state of the race."""
        with self.lock:
            if self.running:
                self.paused = not self.paused
                if self.paused:
                    self.race_manager.pause_race()
                else:
                    self.race_manager.resume_race()
                    
    def update(self):
        """Update game state and render."""
        # Update car positions if race is running and not paused
        if self.running and not self.paused:
            self.race_manager.update_cars()
            
            # Check for race completion
            if self.race_manager.is_race_finished():
                self.running = False
        
        # Render current game state
        self.game_window.render(
            cars=self.race_manager.get_cars(),
            race_active=self.running,
            paused=self.paused
        )
        
    def cleanup(self):
        """Clean up resources and stop threads."""
        with self.lock:
            self.running = False
            self.race_manager.stop_race()

class GameEvent:
    """Event types for game state changes."""
    RACE_START = "race_start"
    RACE_END = "race_end"
    RACE_PAUSE = "race_pause"
    RACE_RESUME = "race_resume"
    RACE_RESET = "race_reset"

class GameState:
    """Game state constants."""
    IDLE = "idle"
    RUNNING = "running"
    PAUSED = "paused"
    FINISHED = "finished"