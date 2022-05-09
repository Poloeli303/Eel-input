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
w = 4
a = 5
d = 6
s = 7

#player variables
Px= 600 #xpos of player
Py= 700 #ypos of player
Px2= 500
Py2= 700 
vx = 0 #x velocity of player
vy = 0 #y velocity of player
vx2 = 0
vy2 = 0
keys = [False, False, False, False] #this list holds whether each key has been pressed
second = [False, False, False, False]


#animation variables variables
frameWidth = 47
frameHeight = 52
frameWidth2 = 47
frameHeight2 = 52
RowNum = 0 #for left animation, this will need to change for other animations
RowNum2 = 0
frameNum = 0
frameNum2 = 0
ticker = 0
ticker2 = 0
direction = DOWN
direction2 = DOWN

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
            if event.key == pygame.K_LEFT:
                second[LEFT]=False
            elif event.key == pygame.K_RIGHT:
                second[RIGHT]=False
            elif event.key == pygame.K_UP:
                second[UP]=False
           
        if event.type == pygame.KEYUP: #keyboard input
            if event.key == pygame.K_a:
                keys[LEFT]=False
            elif event.key == pygame.K_d:
                keys[RIGHT]=False
            elif event.key == pygame.K_w:
                keys[UP]=False
            elif event.key == pygame.K_s:
                keys[DOWN]=False
            if event.key == pygame.K_LEFT:
                second[LEFT]=False
            elif event.key == pygame.K_RIGHT:
                second[RIGHT]=False
            elif event.key == pygame.K_UP:
                second[UP]=False
                
    
       
          
    #physics section--------------------------------------------------------------------
    
    #LEFT MOVEMENT
    if keys[LEFT]==True:
        vx=-3
        vy=0
        direction = LEFT
        
    #Right Movement
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
        vx=0
        direction = DOWN
    
    #LEFT MOVEMENT
    if second[LEFT]==True:
        vx2=-3
        vy2=0
        direction2 = LEFT
        
    #Right Movement
    elif second[RIGHT]==True:
        vx2=3
        vy2=0
        direction2 = RIGHT
    
      #JUMPING  
    if second[UP]==True:
        vy2=-3
        vx2=0
        direction2 = UP
        
      #DOWN
    if second[DOWN]==True:
        vy2=+3
        vx2=0
        direction2 = DOWN
    #update player position
    Px+=vx 
    Py+=vy
    Px2+=vx2
    Py2+=vy2
      
    # RENDER Section--------------------------------------------------------------------------------
            
    screen.fill((0,0,0)) #wipe screen so it doesn't smear
    pygame.draw.rect(screen, (purple), (Px, Py, 25, 25))
    pygame.draw.rect(screen, (red), (Px2, Py2, 25, 25))
    
    
    pygame.display.flip()#this actually puts the pixel on the screen
    
#end game loop------------------------------------------------------------------------------
pygame.quit()
