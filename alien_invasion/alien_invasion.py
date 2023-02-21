import pygame
import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
#Initilizian game and create object of display.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
#Create the ship.
    ship = Ship(ai_settings, screen)
    #Create the group for saving of bullets.
    bullets = Group()

#Choose main color background.
    bg_color = (0, 0, 255)

#Start tne main range of game.
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(ai_settings, screen, ship, bullets)
        gf.update_screen(ai_settings, screen, ship, bullets)
    

#Screen is drawn with each transition of the loop.
        screen.fill(ai_settings.bg_color)
        ship.blitme()


#Display last drawn screen.
        pygame.display.flip()
         
run_game()
