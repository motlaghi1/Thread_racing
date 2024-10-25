# src/game/car.py
import threading
import random
from src.utils.constants import MIN_SPEED, MAX_SPEED, ACCELERATION_RATE, MAX_BOOST_SPEED

class Car:
    def __init__(self, car_id, position, race_condition):
        """
        Initialize a car with its properties.
        
        Args:
            car_id (int): Unique identifier for the car
            position (float): Starting position (0.0 to 1.0)
            race_condition (threading.Condition): Condition variable for synchronization
        """
        # Basic properties
        self.car_id = car_id
        self.position = position
        self.race_condition = race_condition
        
        # State flags
        self.paused = False
        self.crashed = False
        
        # Movement properties
        self.current_speed = 0.0
        self.acceleration = ACCELERATION_RATE
        self.state_lock = threading.Lock()
        
        # Power-up states
        self.boost_active = False
        self.boost_duration = 0
        
    def move(self):
        """
        Update the car's position based on current speed and conditions.
        Returns True if movement was successful, False if car is paused or crashed.
        """
        with self.state_lock:
            if self.paused or self.crashed:
                return False
                
            # Calculate base speed
            if self.current_speed < MAX_SPEED:
                self.current_speed += self.acceleration
                self.current_speed = min(self.current_speed, MAX_SPEED)
            
            # Apply random variations to simulate realistic racing
            speed_variation = random.uniform(-0.0001, 0.0001)
            effective_speed = self.current_speed + speed_variation
            
            # Apply boost if active
            if self.boost_active:
                effective_speed = min(effective_speed * 1.5, MAX_BOOST_SPEED)
                self.boost_duration -= 1
                if self.boost_duration <= 0:
                    self.boost_active = False
            
            # Update position
            self.position += effective_speed
            
            # Ensure position stays within bounds
            self.position = min(max(self.position, 0.0), 1.0)
            
            return True
            
    def apply_boost(self, duration=60):  # 60 frames = 1 second at 60 FPS
        """Apply a speed boost to the car."""
        with self.state_lock:
            if not self.crashed and not self.paused:
                self.boost_active = True
                self.boost_duration = duration
                
    def crash(self):
        """Handle car crash event."""
        with self.state_lock:
            self.crashed = True
            self.current_speed = 0.0
            
    def recover(self):
        """Recover from crash."""
        with self.state_lock:
            self.crashed = False
            self.current_speed = 0.0
            
    def reset(self):
        """Reset car to starting state."""
        with self.state_lock:
            self.position = 0.0
            self.current_speed = 0.0
            self.crashed = False
            self.paused = False
            self.boost_active = False
            self.boost_duration = 0
            
    def get_state(self):
        """
        Get current car state in a thread-safe manner.
        Returns dict with current car state.
        """
        with self.state_lock:
            return {
                'car_id': self.car_id,
                'position': self.position,
                'speed': self.current_speed,
                'crashed': self.crashed,
                'paused': self.paused,
                'boosting': self.boost_active
            }
            
    def set_position(self, position):
        """Set car position in a thread-safe manner."""
        with self.state_lock:
            self.position = min(max(position, 0.0), 1.0)
            
    def toggle_pause(self):
        """Toggle pause state in a thread-safe manner."""
        with self.state_lock:
            self.paused = not self.paused
            if self.paused:
                self.current_speed = 0.0