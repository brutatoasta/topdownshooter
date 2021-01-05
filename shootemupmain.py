# Import the pygame library and initialise the game engine
import pygame
from player import Player
from bullet import Bullet
 
pygame.init()
 
# Define some colors
BLACK = (0,0,0)
WHITE = (255,255,255)
 
# Open a new window
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("shoot 'em up")
 
player1 = Player(WHITE, 10, 50)
player1.rect.x = 20
player1.rect.y = 200

player2 = Player(WHITE, 15, 50)
player2.rect.x = 670
player2.rect.y = 200

"""
bullet = Bullet(WHITE,10,10)
bullet.rect.x = 350
bullet.rect.y = 250
"""
 
#This will be a list that will contain all the sprites we intend to use in our game.
all_sprites_list = pygame.sprite.Group()
 
# Add the paddles and the ball to the list of objects
all_sprites_list.add(player1)
all_sprites_list.add(player2)
#all_sprites_list.add(bullet)
 
# The loop will carry on until the user exit the game (e.g. clicks the close button).
carryOn = True
 
# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while carryOn:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
              carryOn = False # Flag that we are done so we exit this loop
        elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_x: #Pressing the x Key will quit the game
                     carryOn=False
 
    #Moving the paddles when the use uses the arrow keys (player A) or "W/S" keys (player B) 
    keys = pygame.key.get_pressed()

    #player 1
    if keys[pygame.K_w]:
        player1.moveUp(5)
    if keys[pygame.K_s]:
        player1.moveDown(5)
    if keys[pygame.K_d]:
        player1.moveRight(5)
    if keys[pygame.K_a]:
        player1.moveLeft(5)

    if keys[pygame.K_UP]:
        player2.moveUp(5)
    if keys[pygame.K_DOWN]:
        player2.moveDown(5)    
    if keys[pygame.K_RIGHT]:
        player2.moveRight(5)
    if keys[pygame.K_LEFT]:
        player2.moveLeft(5)
 
    # --- Game logic should go here
    all_sprites_list.update()

    
    """
    #Check if the ball is bouncing against any of the 4 walls:
    if ball.rect.x>=690:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x<=0:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y>490:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y<0:
        ball.velocity[1] = -ball.velocity[1] 
 
    #Detect collisions between the ball and the paddles
    if pygame.sprite.collide_mask(ball, player) or pygame.sprite.collide_mask(ball, player12):
        ball.bounce()
    """
    # --- Drawing code should go here
    # First, clear the screen to black. 
    screen.fill(BLACK)
    #Draw the net
    pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)
    
    #Now let's draw all the sprites in one go. (For now we only have 2 sprites!)
    all_sprites_list.draw(screen) 
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
     
    # --- Limit to 60 frames per second
    clock.tick(60)
 
#Once we have exited the main program loop we can stop the game engine:
pygame.quit()