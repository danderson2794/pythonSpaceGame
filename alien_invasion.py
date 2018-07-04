import pygame

from settings import Settings


def run_game():
    # Initialize pygame, settings, and screen object.
    pygame.init()
    #below is screen resolution
    ai_settings = Settings()
    
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    
    pygame.display.set_caption("Alien Invasion")


    #This sets the background color
    bg_color = (230, 230, 230)

        #start the main loop for the game.
    while True:

        # Redraw the screen during each pass through the loop
        screen.fill(ai_settings.bg_color)
        
        #make the most recently drawn screen visible.
        pygame.display.flip()

run_game()


        