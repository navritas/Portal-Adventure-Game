import pygame

pygame.init()

#Use the default WIDTH and HEIGHT below for the pygame window,
#or you can change to pygame.FULLSCREEN and use screen.get_size() to get the WIDTH and HEIGHT
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#Loading all of the images and scaling them to proper size
blackTileImg = pygame.transform.scale(pygame.image.load("black tile.png"), (50, 50))
dirtImg = pygame.transform.scale(pygame.image.load("dirt.png"), (50, 50))
lavaImg = pygame.transform.scale(pygame.image.load("lava.png"), (50, 50))
rockImg = pygame.transform.scale(pygame.image.load("rock.png"), (50, 50))
characterImg = pygame.transform.scale(pygame.image.load("character.png"), (50, 50))
portalImg = pygame.transform.scale(pygame.image.load("portal.png"), (50, 50))
portal2Img = pygame.transform.scale(pygame.image.load("portal2.png"), (50, 50))
openBarrelImg = pygame.transform.scale(pygame.image.load("openBarrel.png"), (50, 50))
closedBarrelImg = pygame.transform.scale(pygame.image.load("closedBarrel.png"), (50, 50))
boxImg = pygame.transform.scale(pygame.image.load("box.png"), (50, 50))

#Modify the world 2D list to have at least 12 rows and at least 16 columns
#2D list for the game world
world = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2],
    [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

#2D list for obstacles
obstacles = [[7, 4, 4, 4, 4, 4, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4],
             [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
             [4, 4, 2, 4, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
             [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
             [4, 4, 4, 4, 4, 4, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4],
             [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
             [4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 4, 4, 4, 4, 4, 4],
             [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
             [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 6, 4, 4, 4, 4, 4],
             [4, 4, 8, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
             [3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
             [4, 4, 4, 4, 4, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]]
   
#Defining variables 
characterX = 4
characterY = 4
player = [2, 3]
portalPos1 = (5, 2)
portalPos2 = (11, 8)
currentPortalPos = portalPos1
characterSpeed = 50

#Function to draw the game board on the screen
def drawPieces():
    for row in range(12):
        for col in range(16):
            if world[row][col] == 0:
                screen.blit(blackTileImg, (col*50, row*50))
            elif world[row][col] == 1:
                screen.blit(dirtImg, (col*50, row*50))
            if world[row][col] == 2:
                screen.blit(lavaImg, (col*50, row*50))
            if obstacles[row][col] == 3:
                screen.blit(rockImg, (col*50, row*50))
            if obstacles[row][col] == 5:
                screen.blit(portalImg, (col*50, row*50))
            if obstacles[row][col] == 6:
                screen.blit(portal2Img, (col*50, row*50))
            if obstacles[row][col] == 7:
                screen.blit(closedBarrelImg, (col*50, row*50))
            if obstacles[row][col] == 8:
                screen.blit(boxImg, (col*50, row*50))
            if obstacles[row][col] == 9:  # Assuming 9 represents the open, walkable barrel
                screen.blit(openBarrelImg, (col*50, row*50))

#Function to black out most of the screen but only show the tiles around the character
def blackedOut():
    for row in range(16):
        for col in range(12):
            if ((row < player[0] - 2 or row > player[0] + 2) or (col < player[1] - 2 or col > player[1] + 2) or
            ((row == player[0] - 2 or row == player[0] + 2) and (col == player[1] - 2 or col == player[1] + 2))):
               pygame.draw.rect(screen, (0, 0, 0), (row * 50, col * 50, 50, 50))


            
#Booleans for tracking user input
up = False
done = False
down = False
right = False
left = False
running = True

#Game loop
while running:
    # ===================== HANDLE EVENTS (EDIT FOR KEYPRESSES) =============== #
    # Inside the game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            done = True
            running = False
            break

        # Keys pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if player[1] > 0 and obstacles[player[1] - 1][player[0]] != 3:
                    if obstacles[player[1] - 1][player[0]] != 7:  
                        player[1] -= 1
                    up = True
            elif event.key == pygame.K_DOWN:
                if player[1] < len(world) - 1 and obstacles[player[1] + 1][player[0]] != 3:
                    if obstacles[player[1] + 1][player[0]] != 7:  
                        player[1] += 1
                    down = True
            elif event.key == pygame.K_LEFT:
                if player[0] > 0 and obstacles[player[1]][player[0] - 1] != 3:
                    if obstacles[player[1]][player[0] - 1] != 7: 
                        player[0] -= 1
                    left = True
            elif event.key == pygame.K_RIGHT:
                if player[0] < len(world[0]) - 1 and obstacles[player[1]][player[0] + 1] != 3:
                    if obstacles[player[1]][player[0] + 1] != 7:
                        player[0] += 1
                    right = True
                    
                if obstacles[player[1]][player[0]] == 8:
                    if (player[0] < len(world[0]) - 1 and obstacles[player[1]][player[0] + 1] != 8):
                        obstacles[player[1]][player[0] + 1] = 8
                        obstacles[player[1]][player[0]] = 0
            
            #If the spacebar is pressed
            if event.key == pygame.K_SPACE:
                if (player[0], player[1]) == (0, 1):
                    closedBarrelImg = openBarrelImg
                    
            #If nothing is pressed
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    up = False
                if event.key == pygame.K_DOWN:
                    down = False
                if event.key == pygame.K_RIGHT:
                    right = False
                if event.key == pygame.K_LEFT:
                    left = False
                    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Check all adjacent tiles to see if there's a closed barrel
                    adjacent_positions = [(player[0], player[1]-1), (player[0], player[1]+1), 
                                          (player[0]-1, player[1]), (player[0]+1, player[1])]
                    for pos in adjacent_positions:
                        if 0 <= pos[0] < len(obstacles[0]) and 0 <= pos[1] < len(obstacles):
                            if obstacles[pos[1]][pos[0]] == 7:  # 7 represents a closed barrel
                                obstacles[pos[1]][pos[0]] = 4  # Change 4 to the value representing an open barrel or walkable path
                                break
                    
    if done == True:
        break           

    # ============================== MOVE STUFF ============================= #
    

    
    # ============================== COLLISION ============================== #

    #If the character touches lava, the game breaks 
    if world[player[1]][player[0]] == 2:
        running = False 

    #Character transport between two portals
    if obstacles[player[1]][player[0]] == 5 or obstacles[player[1]][player[0]] == 6:
        if currentPortalPos == portalPos1:
            player[0], player[1] = portalPos2
            currentPortalPos = portalPos2
        elif currentPortalPos == portalPos2:
            player[0], player[1] = portalPos1
            currentPortalPos = portalPos1

    
    # ============================== DRAW STUFF ============================= #
    screen.fill ((255,255,255))
    
    #Calling drawPieces function
    drawPieces()
    
    #Allowing character to move
    characterPosX = player[0] * characterSpeed
    characterPosY = player[1] * characterSpeed
    
    screen.blit(characterImg, (characterPosX, characterPosY))

    #Calling blackedOut function
    blackedOut()
   
    # ====================== PYGAME STUFF (DO NOT EDIT) ===================== #
    pygame.display.flip()
    pygame.time.delay(20)
pygame.quit()