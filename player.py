import pygame
BLACK = (0,0,0)
 
class Player(pygame.sprite.Sprite):
    #This class represents a paddle. It derives from the "Sprite" class in Pygame.
    
    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()
        
        # Pass in the color of the Player, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
 
        # Draw the player (a rectangle!)
        pygame.draw.polygon(self.image, color, [[100, 100], [0, 200], [200, 200]], 5)
        
        # Fetch the polygon object that has the dimensions of the image.
        self.polygon = self.image.get_polygon()
        
    def moveUp(self, pixels):
        self.polygon.y -= pixels
		#Check that you are not going too far (off the screen)
        if self.polygon.y < 0:
            self.polygon.y = 0
          
    def moveDown(self, pixels):
        self.polygon.y += pixels
	#Check that you are not going too far (off the screen)
        if self.polygon.y > 400:
            self.polygon.y = 400

    def moveRight(self, pixels):
        self.polygon.x += pixels
	#Check that you are not going too far (off the screen)
        if self.polygon.x > 400:
            self.polygon.x = 400

    def moveLeft(self, pixels):
        self.polygon.x -= pixels
	#Check that you are not going too far (off the screen)
        if self.polygon.x < 0:
            self.polygon.x = 0
