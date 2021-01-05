import pygame
BLACK = (0,0,0)
GREEN = (0,128,0)
 
class Zombie(pygame.sprite.Sprite):
    #This class represents a Zombie. It derives from the "Sprite" class in Pygame.
    
    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()
        
        # Pass in the color of the Player, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(GREEN)
        self.image.set_colorkey(GREEN)
 
        # Draw the player (a rectangle!)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        
        # Fetch the rect object that has the dimensions of the image.
        self.rect = self.image.get_rect()
        
    def moveUp(self, pixels):
        self.rect.y -= pixels
		#Check that you are not going too far (off the screen)
        if self.rect.y < 0:
            self.rect.y = 0
          
    def moveDown(self, pixels):
        self.rect.y += pixels
	#Check that you are not going too far (off the screen)
        if self.rect.y > 600:
            self.rect.y = 600

    def moveRight(self, pixels):
        self.rect.x += pixels
	#Check that you are not going too far (off the screen)
        if self.rect.x > 800:
            self.rect.x = 800

    def moveLeft(self, pixels):
        self.rect.x -= pixels
	#Check that you are not going too far (off the screen)
        if self.rect.x < 0:
            self.rect.x = 0

    def 