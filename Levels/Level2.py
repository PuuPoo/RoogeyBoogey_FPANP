import pygame
from pytmx.util_pygame import load_pygame
from Character.Player import Player
from Functionality.Tile import Tile
from Functionality.camera import Camera


#Setting the tmx file for the map and background into groups and loading the data
tmxData = load_pygame("Levels/TMX/Level2.tmx")


#Clamping the camera to the map size to not go over
mapWidth = tmxData.width * tmxData.tilewidth
mapHeight = tmxData.height * tmxData.tileheight


#Layers in tmx map 
levelSpriteGroup = Camera(mapWidth, mapHeight)
platformSpriteGroup = Camera(mapWidth, mapHeight)
finishedBlockSpriteGroup = Camera(mapWidth, mapHeight)
decorationsSpriteGroup = Camera(mapWidth, mapHeight)
liquidsSpriteGroup = Camera(mapWidth, mapHeight)
backgroundSpriteGroup = Camera(mapWidth, mapHeight)




playerGroup = Camera(mapWidth, mapHeight)


#Making the empty list for the tiles that will have collision
collisionTiles = []
platformCollisionTiles = []





#Cycling through the layers in the data
for layer in tmxData.layers:

    targetGroup = None


    # Assign tiles to their specific group based on name
    if layer.name == "Level":
        targetGroup = levelSpriteGroup
    elif layer.name == "Platform":
        targetGroup = platformSpriteGroup
    elif layer.name == "FinishedBlock":
        targetGroup = finishedBlockSpriteGroup
    elif layer.name == "Decorations":
        targetGroup = decorationsSpriteGroup
    elif layer.name == "Liquids":
        targetGroup = liquidsSpriteGroup
    elif layer.name == "Background":
        targetGroup = backgroundSpriteGroup


    # Process the tiles for drawing and collision (X and Y are the coordinates, Surface is the image)
    for x, y, surface in layer.tiles():
        if surface:
            position = (x * 32, y * 32)
            
            # Add to collision list if the tile is in the Level layer
            if layer.name == "Level":
                rect = pygame.Rect(x * 32, y * 32, 32, 32)
                collisionTiles.append(rect)

            elif layer.name == "Platform":
                rect = pygame.Rect(x * 32, y * 32, 32, 32)
                platformCollisionTiles.append(rect)



            #Add transparency if the tile is in the Liquids layer
            elif layer.name == "Liquids":
                surface.set_alpha(150) 
                
                position = (x * 32, y * 32)
            




            # Add to the other layer to its own drawing group
            if targetGroup is not None:
                Tile(pos = position, surface = surface, groups = targetGroup)



def Level2(screen):


    #Setting the screen size
    pygame.display.set_caption("Roogey Boogey")


    #Initializing the clock class from pygame library 
    clock = pygame.time.Clock()
    FPS = 60 




    #RUNNING THE LEVEL
    #Setting the variable to be used to check if the game is running
    gameRunning = True


    #Making the character
    Knight = Player(97, 1048)
    playerGroup.add(Knight)





    while gameRunning:
        #Sets the tickrate to the targetted FPS
        clock.tick(FPS)


        #EVENT HANDLER
        #Event handler for exiting the game
        for event in pygame.event.get():
            #If the user just quits from window
            if event.type == pygame.QUIT:
                gameRunning = False

    
        screen.fill((47,203,255))



        #Drawing the layers

        """
        backgroundSpriteGroup.draw(Knight, screen)

        liquidsSpriteGroup.draw(Knight, screen)

        decorationsSpriteGroup.draw(Knight, screen)

        finishedBlockSpriteGroup.draw(Knight, screen)
        """
        platformSpriteGroup.draw(Knight, screen)

        levelSpriteGroup.draw(Knight, screen)



        #Initalizing the Player into the game 
        Knight.update(collisionTiles, platformCollisionTiles)

        playerGroup.draw(Knight, screen)
        
        # updates the frames of the game 
        pygame.display.update()    

    pygame.quit()


