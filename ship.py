import pygame

class Ship:
    """Manage the ship in this game"""

    def __init__(self, ai_game):
        """Initialize the ship, and set up ship position"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # load ship image and get it's rectangle shape
        self.image = pygame.image.load('images/ship.bmp')
        
        self.rect = self.image.get_rect()

        #put every ship on the middle bottom of screen
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        #Moving flag
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        """moving ship by judge moing_right"""
        if self.moving_right == True and self.rect.right < self.screen_rect.right :
            self.x += self.settings.ship_speed
        if self.moving_left == True  and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        #update by use self.x 
        self.rect.x = self.x


    def blitme(self):
        """draw the ship in specified position"""
        self.screen.blit(self.image,self.rect)
