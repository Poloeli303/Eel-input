import pygame
pygame.init()  
pygame.display.set_caption("platformer")  # sets the window title
screen = pygame.display.set_mode((800, 800))  # creates game screen
screen.fill((0,0,0))
clock = pygame.time.Clock() #set up clock
gameover = False #variable to run our game loop

#Link = pygame.image.load('ash1.png') #load your spritesheet
#Link.set_colorkey((255, 0, 255)) #this makes bright pink (255, 0, 255) transparent (sort of)
red = (255,0,0)
purple = (200,0,200)

#CONSTANTS
LEFT=0
RIGHT=1
UP = 2
DOWN = 3

#platform class

class Rectangular:
    def __init__ (self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
    def draw(self):
        pygame.draw.rect(screen, (red),(self.xpos, self.ypos, 100, 20))
    def collide(self, x, y):
        if x>self.xpos and x<self.xpos+100 and y+40> self.ypos and y +20 < self.ypos + 20:
            return self.ypos
        else:
            return False
class Square:
    def __init__ (self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
    def draw(self):
        pygame.draw.rect(screen, (red),(self.xpos, self.ypos, 20, 20))
    def collide(self, x, y):
        if x>self.xpos and x<self.xpos+100 and y+40> self.ypos and y+40 < self.ypos + 20:
            return self.ypos
        else:
            return False

#player variables
Px= 600 #xpos of player
Py= 700 #ypos of player
vx = 0 #x velocity of player
vy = 0 #y velocity of player
keys = [False, False, False, False] #this list holds whether each key has been pressed
isOnGround = False #this variable stops gravity from pulling you down more when on a platform

#animation variables variables
frameWidth = 47
frameHeight = 52
RowNum = 0 #for left animation, this will need to change for other animations
frameNum = 0
ticker = 0

while not gameover: #GAME LOOP############################################################
    clock.tick(60) #FPS
  
    #Input Section------------------------------------------------------------
    for event in pygame.event.get(): #quit game if x is pressed in top corner
        if event.type == pygame.QUIT:
            gameover = True
      
        if event.type == pygame.KEYDOWN: #keyboard input
            if event.key == pygame.K_a:
                keys[LEFT]=True
            elif event.key == pygame.K_d:
                keys[RIGHT]=True
            elif event.key == pygame.K_w:
                keys[UP]=True
            elif event.key == pygame.K_s:
                keys[DOWN]=True
           
        if event.type == pygame.KEYUP: #keyboard input
            if event.key == pygame.K_a:
                keys[LEFT]=False
            elif event.key == pygame.K_d:
                keys[RIGHT]=False
            elif event.key == pygame.K_w:
                keys[UP]=False
            elif event.key == pygame.K_s:
                keys[DOWN]=False

                
    
       
          
    #physics section--------------------------------------------------------------------
    
    #LEFT MOVEMENT
    if keys[LEFT]==True:
        vx=-3
        vy=0
        direction = LEFT
    elif keys[RIGHT]==True:
        vx=3
        vy=0
        direction = RIGHT
    

        
      #JUMPING  
    if keys[UP]==True:
        vy=-3
        vx=0
        direction = UP
        
      #DOWN
    if keys[DOWN]==True:
        vy=+3
        vy=0
        direction = DOWN
    

    #update player position
    Px+=vx 
    Py+=vy
      
    # RENDER Section--------------------------------------------------------------------------------
            
    screen.fill((0,0,0)) #wipe screen so it doesn't smear
    pygame.draw.rect(screen, (purple), (Px, Py, 25, 25))
    #screen.blit(Link, (Px, Py), (frameWidth*frameNum, RowNum*frameHeight, frameWidth, frameHeight))

    
    #class platforms
    
    
    pygame.display.flip()#this actually puts the pixel on the screen
    
#end game loop------------------------------------------------------------------------------
pygame.quit()
