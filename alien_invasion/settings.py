class Settings():
    """Class for save all options for game Alien Invasion."""

    def __init__(self):
        """Initilization options game."""
        #Settings screen
        self.screen_width = 1366
        self.screen_height = 768
        self.bg_color = (0, 0, 255)
        #Settings ship
        self.ship_speed_factor = 1.5
        #Settings of bullet
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
