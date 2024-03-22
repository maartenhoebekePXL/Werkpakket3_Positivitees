import pygame
import sys
import settings

# Define virtual viewport size (base resolution)

def main():
    pygame.init()
    screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
    clock = pygame.time.Clock()
    pygame.display.set_caption("Game")
    
    # Load your game assets and set up your game objects
    character = pygame.image.load("game/assets/head.svg").convert_alpha() # Load image with alpha transparency support

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Calculate scale factor
        scale_factor_x = screen.get_width() / settings.WIDTH
        scale_factor_y = screen.get_height() / settings.HEIGHT
        
        # Clear the screen
        screen.fill((0, 0, 0))  # Fill with black
        
        # Draw your game content (scaled)
        
        # pygame.draw.rect(screen, (255, 255, 255), (100 * scale_factor_x, 100 * scale_factor_y, 50 * scale_factor_x, 50 * scale_factor_y))
        screen.blit(character, (100 * scale_factor_x, 100 * scale_factor_y))
        
        # Update the display
        pygame.display.flip()
        
        clock.tick(settings.FPS)  # Cap the frame rate
        
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
