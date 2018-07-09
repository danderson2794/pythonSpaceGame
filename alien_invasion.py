import pygame

from settings import Settings
from ship import Ship
from pygame.sprite import Group 
import game_functions as gf

def run_game():
        
    
    ai_settings = Settings()
    pygame.display.set_caption("Alien Invasion")
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    #This sets the background color
    bg_color = (230, 230, 230)

    # Make a ship
    ship = Ship(ai_settings, screen)

    # Make a group to store bullets in
    bullets = Group()

    #start the main loop for the game.
    while True:
        #screen.fill(ai_settings.bg_color)
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_screen(ai_settings, screen, ship, bullets)

       

run_game() 