import pygame

class Ship():

    def __init__(self, ai_settings, screen):
        """Initialiez the ship and creates its initial position."""
        self.screen = screen
        self.ai_settings = ai_settings

        # Load image ship and receiving rectangle.
        self.image = pygame.image.load('ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Each new ship appears at the bottom of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # Saving the real coordinate of the center of the ship.
        self.center = float(self.rect.centerx)
        # Movement flag.
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """ Update position ship based on the flag."""
        # Update atribute center but not rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # Update atribute rect based self.center.
        self.rect.centerx = self.center
        
    def blitme(self):
        """Draw the ship in current position."""
        self.screen.blit(self.image, self.rect)
        
    def center_ship(self):
        '''Center the ship on the screen.'''
        self.center = self.screen_rect.centerx
