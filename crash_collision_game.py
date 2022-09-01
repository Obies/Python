import pygame # Imports a game library that lets you use specific functions in your program.
import random # Import to generate random numbers. 

# Initialize the pygame modules to get everything started.

pygame.init() 

# The screen that will be created needs a width and a height.

screen_width = 1040

screen_height = 680

screen = pygame.display.set_mode((screen_width,screen_height)) # This creates the screen and gives it the width and height specified as a 2 item sequence.

# This creates the player and gives it the image found in this folder (similarly with the enemy image). 

player = pygame.image.load("image.png")

enemy = pygame.image.load("enemy.png")

monster = pygame.image.load("monster.jpg")  #monster image was used

enemy_2 = pygame.image.load("enemy.png")    #enemy image was used again

prize = pygame.image.load("prize.jpg")      #prize image was used

# Get the width and height of the images specified in order to do boundary detection using get function in PyGame

image_height = player.get_height()

image_width = player.get_width()

enemy_height = enemy.get_height()

enemy_width = enemy.get_width()

monster_height = monster.get_height()

monster_width = monster.get_width()

enemy_2_height = enemy_2.get_height()     

enemy_2_width = enemy_2.get_width()

prize_height = prize.get_height()          

prize_width = prize.get_width()

##Prints height and width of the images specified
print("\nThis is the height of the player image: " +str(image_height))

print("\nThis is the width of the player image: " +str(image_width))

print("\nThis is the height of the monster image: " + str(monster_height)) 

print("\nThis is the width of the monster image: " + str(monster_width))

print("\nThis is the height of the enemy 2 image: " + str(enemy_2_height))

print("\nThis is the width of the enemy 2 image: " + str(enemy_2_width))

print("\nThis is the height of the prize image: " + str(prize_height))

print("\nThis is the width of the prize image: " + str(prize_width))

# Store the positions of the player and enemy as variables so that you can change them later. 

playerXPosition = 100

playerYPosition = 50

monsterXPosition = 90

monsterYPosition = 60

enemy_2XPosition = 110

enemy_2YPosition = 70

prizeXPosition = 105

prizeYPosition = 70

# Make the enemy and prize start off screen and at a random y position.

enemyXPosition =  screen_width

enemyYPosition =  random.randint(0, screen_height - enemy_height)

monsterXPosition = screen_width

monsterYPosition = random.randint(0, screen_height - monster_height) 

enemy_2XPosition = screen_width

enemy_2YPosition = random.randint(0, screen_height - enemy_2_height)  

prizeXPosition = screen_width

prizeYPosition = random.randint(100, 340)

# This checks if the up or down key is pressed.
#The keys are initially set to False 

keyUp= False

keyDown = False

keyLeft = False

keyRight = False

# This is the game loop.
# In games you will need to run the game logic over and over again.
# You need to refresh/update the screen window and apply changes to 
# represent real time game play. 

#Game loop
while True: # This is a looping structure that will loop the indented code until you tell it to stop(in the event where you exit the program by quitting).  

    screen.fill(0) # Clears the screen.
    
    screen.blit(player, (playerXPosition, playerYPosition))# This draws the player image to the screen at the position specfied. I.e. (100, 50).
    
    screen.blit(enemy, (enemyXPosition, enemyYPosition))
    
    screen.blit(monster, (monsterXPosition, monsterYPosition))
    
    screen.blit(enemy_2, (enemy_2XPosition, enemy_2YPosition))
    
    screen.blit(prize, (prizeXPosition, prizeYPosition))
    
    pygame.display.flip()# This updates the screen. 
    
    # This loops through events in the game.
    #This allows only the player to move left and right
    if keyLeft == True:
        playerXPosition -= 3
        
    if keyRight == True:
        playerXPosition += 3
    
    for event in pygame.event.get():
        
        # This event checks if the user quits the program, then if so it exits the program. 
        
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        # This event checks if the user press a key down.
        
        if event.type == pygame.KEYDOWN:
        
            # Tests if the key pressed is the one we want.
            # pygame.K_variable represent a keyboard key constant.
            if event.key == pygame.K_UP:  
                keyUp = True
                
            if event.key == pygame.K_DOWN:
                keyDown = True
                
            if event.key == pygame.K_LEFT:
                keyLeft = True
                
            if event.key == pygame.K_RIGHT:
                keyRight = True
        
        # This event checks if the key is up(i.e. not pressed by the user).
        
        if event.type == pygame.KEYUP:
        
            # Test if the key released is the one we want.
            
            if event.key == pygame.K_UP:
                keyUp = False
                
            if event.key == pygame.K_DOWN:
                keyDown = False
                
            if event.key == pygame.K_LEFT:
                keyLeft = False
                
            if event.key == pygame.K_RIGHT:
                keyRight = False
            
    # After events are checked for in the for loop above and values are set,
    # check key pressed values and move player accordingly.
    
    # The coordinate system of the game window(screen) is that the top left corner is (0, 0).
    # This means that if you want the player to move down you will have to increase the y position. 
    
    if keyUp == True:
        if playerYPosition > 0 : # This makes sure that the user does not move the player above the window.
            playerYPosition -= 1
            
    if keyDown == True:
        if playerYPosition < screen_height - image_height:# This makes sure that the user does not move the player below the window.
            playerYPosition += 1
    
    # Check for collision of the enemy with the player.
    # To do this we need bounding boxes around the images of the player and enemy.
    # We the need to test if these boxes intersect. If they do then there is a collision.
    
    # Bounding box for the player:
    
    playerBox = pygame.Rect(player.get_rect())
    
    # The following updates the playerBox position to the player's position,
    # in effect making the box stay around the player image. 
    
    playerBox.top = playerYPosition
    
    playerBox.left = playerXPosition
    
    # Bounding box for the enemy objects and prize:
    
    enemyBox = pygame.Rect(enemy.get_rect())
    
    enemyBox.top = enemyYPosition
    
    enemyBox.left = enemyXPosition

    monsterBox = pygame.Rect(monster.get_rect())
    
    monsterBox.top = monsterYPosition
    
    monsterBox.left = monsterXPosition

    enemy_2Box = pygame.Rect(enemy_2.get_rect())
    
    enemy_2Box.top = enemy_2YPosition
    
    enemy_2Box.left = enemy_2XPosition

    prizeBox = pygame.Rect(prize.get_rect())
    
    prizeBox.top = prizeYPosition
    
    prizeBox.left = prizeXPosition
    
    # Test collision of the boxes:
    
    if playerBox.colliderect(enemyBox) or playerBox.colliderect(monsterBox) or playerBox.colliderect(enemy_2Box):
    
        # Display losing status to the user: 
        
            print("You lose!")
 
        # Quite game and exit window: 
        
            pygame.quit()
            exit(0)
        
    # If the player collides with prize the player wins the game:
    if playerBox.colliderect(prizeBox):
    
        # Display wining status to the user: 
        
        print("You win!")
        
        # Quite game and exit window: 
        pygame.quit()
        
        exit(0)
    
 
    
    # Make enemy approach the player.
    
    enemyXPosition -= 0.15
    
    monsterXPosition -= 0.25
    
    enemy_2XPosition -= 0.35
    
    prizeXPosition -=0.10
    
    
    # ================The game loop logic ends here. =============
  
