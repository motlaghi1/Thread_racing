"""Unit tests for the Track class."""

import pytest
from src.game.track import Track, TrackPoint
from src.utils.constants import NUM_LANES

class TestTrack:
    @pytest.fixture
    def track(self):
        """Create a fresh Track instance for each test."""
        return Track()

    def test_track_initialization(self, track):
        """Test track initialization."""
        assert track.num_lanes == NUM_LANES
        assert track.length == 1.0
        assert len(track.segments) == 10  # Default number of segments
        
    def test_car_position_calculation(self, track):
        """Test conversion between progress and screen coordinates."""
        # Test start position
        point = track.get_car_position(0, 0.0)
        assert isinstance(point, TrackPoint)
        assert point.x == track.start_line
        
        # Test finish position
        point = track.get_car_position(0, 1.0)
        assert point.x == track.finish_line
        
    def test_lane_boundaries(self, track):
        """Test lane boundary calculations."""
        for lane in range(NUM_LANES):
            top, bottom = track.get_lane_boundaries(lane)
            assert top < bottom
            if lane > 0:
                # Check that lanes don't overlap
                prev_top, prev_bottom = track.get_lane_boundaries(lane - 1)
                assert prev_bottom == top
                
    def test_progress_to_segment(self, track):
        """Test progress to segment conversion."""
        assert track.progress_to_segment(0.0) == 0
        assert track.progress_to_segment(0.5) == 5
        assert track.progress_to_segment(1.0) == 9  # Last segment
        
    def test_collision_detection(self, track):
        """Test collision detection between cars."""
        # Same lane, close positions
        assert track.is_collision(0.5, 0.51, True)
        
        # Same lane, far positions
        assert not track.is_collision(0.1, 0.9, True)
        
        # Different lanes
        assert not track.is_collision(0.5, 0.51, False)