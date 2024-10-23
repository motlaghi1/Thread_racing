# main.py
import pygame
import sys
from src.game.game_engine import GameEngine
from src.game.race_manager import RaceManager
from src.ui.game_window import GameWindow
from src.utils.constants import WINDOW_WIDTH, WINDOW_HEIGHT, FPS, NUM_CARS

def main():
    """Main entry point of the racing game."""
    # Initialize Pygame
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Racing Game")
    clock = pygame.time.Clock()
    
    # Create game components
    race_manager = RaceManager(NUM_CARS)
    game_window = GameWindow(screen)
    game_engine = GameEngine(race_manager, game_window)
    
    # Game state
    running = True
    game_started = False
    
    # Main game loop
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not game_started:
                        game_engine.start_race()
                        game_started = True
                    else:
                        game_engine.toggle_pause()
                elif event.key == pygame.K_r:
                    game_engine.reset_race()
                    game_started = False
                elif event.key == pygame.K_ESCAPE:
                    running = False
        
        # Update and render
        game_engine.update()
        game_window.render()
        
        # Check race completion
        if game_started and race_manager.is_race_finished():
            winner = race_manager.get_winner()
            game_window.show_winner(winner)
            game_started = False
        
        # Maintain frame rate
        clock.tick(FPS)
        pygame.display.flip()
    
    # Cleanup
    game_engine.cleanup()
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()