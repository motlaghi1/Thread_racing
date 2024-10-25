# src/game/race_manager.py
import threading
import random
import time
from src.utils.constants import TRACK_LENGTH, MIN_SPEED, MAX_SPEED
from src.game.car import Car

class RaceManager:
    def __init__(self, num_cars):
        """Initialize the race manager."""
        self.num_cars = num_cars
        self.cars = []
        self.car_threads = []
        self.race_condition = threading.Condition()
        self.race_active = False
        self.winner = None
        
        # Shared state protection
        self.state_lock = threading.Lock()
        
    def create_cars(self, num_cars):
        """Create specified number of cars."""
        self.cars = []
        self.car_threads = []
        
        for i in range(num_cars):
            car = Car(
                car_id=i,
                position=0.0,
                race_condition=self.race_condition
            )
            self.cars.append(car)
            
            # Create thread for each car
            thread = threading.Thread(
                target=self._car_thread_function,
                args=(car,),
                daemon=True
            )
            self.car_threads.append(thread)
            
    def start_race(self):
        """Start all car threads."""
        with self.state_lock:
            self.race_active = True
            self.winner = None
            # Start all car threads
            for thread in self.car_threads:
                thread.start()
                
    def stop_race(self):
        """Stop all car threads."""
        with self.state_lock:
            self.race_active = False
            # Notify all waiting threads
            with self.race_condition:
                self.race_condition.notify_all()
            
            # Wait for all threads to finish
            for thread in self.car_threads:
                if thread.is_alive():
                    thread.join(timeout=1.0)
                    
    def pause_race(self):
        """Pause all cars."""
        with self.state_lock:
            for car in self.cars:
                car.paused = True
                
    def resume_race(self):
        """Resume all cars."""
        with self.state_lock:
            for car in self.cars:
                car.paused = False
            # Notify all waiting threads
            with self.race_condition:
                self.race_condition.notify_all()
                
    def reset_cars(self):
        """Reset all cars to starting position."""
        with self.state_lock:
            for car in self.cars:
                car.position = 0.0
                car.paused = False
            self.winner = None
            
    def update_cars(self):
        """Update positions of all cars."""
        # No need to update positions here as cars update themselves in their threads
        # This method could be used for additional state updates if needed
        pass
                
    def is_race_finished(self):
        """Check if any car has finished."""
        return self.winner is not None
        
    def get_cars(self):
        """Get list of all cars."""
        return self.cars
        
    def get_winner(self):
        """Get the winner's car ID."""
        return self.winner
        
    def _car_thread_function(self, car):
        """Thread function for controlling car movement."""
        while self.race_active and car.position < 1.0:
            with self.race_condition:
                while car.paused and self.race_active:
                    # Wait while paused
                    self.race_condition.wait()
                    
                if not self.race_active:
                    break
                    
                # Move car
                speed = random.uniform(MIN_SPEED, MAX_SPEED)
                car.position += speed
                
                # Ensure position doesn't exceed finish line
                car.position = min(car.position, 1.0)
                
                # Check for winner
                if car.position >= 1.0 and self.winner is None:
                    with self.state_lock:
                        if self.winner is None:  # Double-check under lock
                            self.winner = car.car_id
                            self.race_active = False
                            
            # Sleep to control update rate
            time.sleep(0.016)  # Approximately 60 FPS
            
    def check_collision(self, car):
        """Check for collisions with other cars."""
        for other_car in self.cars:
            if car != other_car:
                # Simple collision detection based on position
                if abs(car.position - other_car.position) < 0.05:  # Collision threshold
                    return True
        return False