# src/game/track.py
from dataclasses import dataclass
from src.utils.constants import (
    TRACK_LENGTH,
    NUM_LANES,
    TRACK_WIDTH,
    TRACK_HEIGHT,
    TRACK_MARGIN
)

@dataclass
class TrackPoint:
    """Represents a point on the track."""
    x: float
    y: float

class Track:
    def __init__(self):
        """Initialize the race track."""
        self.length = TRACK_LENGTH
        self.num_lanes = NUM_LANES
        self.width = TRACK_WIDTH
        self.height = TRACK_HEIGHT
        self.margin = TRACK_MARGIN
        
        # Track segments for checkpoints and collision detection
        self.segments = self._create_segments(10)  # Divide track into 10 segments
        
        # Define track boundaries
        self.start_line = self.margin + 20
        self.finish_line = self.width - self.margin - 20
        
        # Calculate lane properties
        self.lane_height = (self.height - (2 * self.margin)) / self.num_lanes
        
    def get_car_position(self, lane, progress):
        """
        Convert a car's progress (0.0 to 1.0) to screen coordinates.
        
        Args:
            lane (int): Lane number (0 to NUM_LANES-1)
            progress (float): Race progress (0.0 to 1.0)
            
        Returns:
            TrackPoint: Screen coordinates for the car
        """
        # Calculate x position based on progress
        x = self.start_line + (progress * (self.finish_line - self.start_line))
        
        # Calculate y position based on lane
        y = self.margin + (lane * self.lane_height) + (self.lane_height / 2)
        
        return TrackPoint(x, y)
        
    def get_lane_boundaries(self, lane):
        """
        Get the y-coordinates of lane boundaries.
        
        Args:
            lane (int): Lane number
            
        Returns:
            tuple: (top_y, bottom_y) coordinates
        """
        top = self.margin + (lane * self.lane_height)
        bottom = top + self.lane_height
        return (top, bottom)
        
    def progress_to_segment(self, progress):
        """
        Convert progress to segment number.
        
        Args:
            progress (float): Race progress (0.0 to 1.0)
            
        Returns:
            int: Segment number
        """
        return min(int(progress * len(self.segments)), len(self.segments) - 1)
        
    def _create_segments(self, num_segments):
        """
        Create track segments for more precise position tracking.
        
        Args:
            num_segments (int): Number of segments to create
            
        Returns:
            list: List of segment boundaries
        """
        segment_length = 1.0 / num_segments
        return [(i * segment_length, (i + 1) * segment_length) 
                for i in range(num_segments)]
                
    def is_valid_position(self, lane, progress):
        """
        Check if a position is valid on the track.
        
        Args:
            lane (int): Lane number
            progress (float): Race progress
            
        Returns:
            bool: True if position is valid
        """
        return (0 <= lane < self.num_lanes and 
                0.0 <= progress <= 1.0)
                
    def calculate_distance(self, pos1, pos2):
        """
        Calculate distance between two progress positions.
        
        Args:
            pos1 (float): First position (0.0 to 1.0)
            pos2 (float): Second position (0.0 to 1.0)
            
        Returns:
            float: Distance between positions
        """
        return abs(pos1 - pos2) * (self.finish_line - self.start_line)
        
    def get_checkpoint_positions(self, num_checkpoints):
        """
        Generate evenly spaced checkpoint positions.
        
        Args:
            num_checkpoints (int): Number of checkpoints to create
            
        Returns:
            list: Checkpoint positions (0.0 to 1.0)
        """
        return [i / num_checkpoints for i in range(1, num_checkpoints)]
        
    def get_finish_line_position(self):
        """Get the finish line position in screen coordinates."""
        return TrackPoint(self.finish_line, self.height / 2)
        
    def get_start_line_position(self):
        """Get the start line position in screen coordinates."""
        return TrackPoint(self.start_line, self.height / 2)
        
    def is_collision(self, car1_pos, car2_pos, same_lane):
        """
        Check if two cars are colliding.
        
        Args:
            car1_pos (float): First car's progress
            car2_pos (float): Second car's progress
            same_lane (bool): Whether cars are in the same lane
            
        Returns:
            bool: True if collision detected
        """
        if not same_lane:
            return False
            
        # Define collision threshold based on car size
        collision_threshold = 0.05  # 5% of track length
        return abs(car1_pos - car2_pos) < collision_threshold