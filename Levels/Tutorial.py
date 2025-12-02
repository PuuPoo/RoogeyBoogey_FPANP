import pygame
from pytmx.util_pygame import load_pygame
from Character.Player import Player
from Functionality.Tile import Tile
from Functionality.camera import Camera



#Setting the tmx file for the map and background into groups and loading the data
tmxData = load_pygame("Levels/TMX/Tutorial.tmx")

#Clamping the camera to the map size to not go over
mapWidth = tmxData.width * tmxData.tilewidth
mapHeight = tmxData.height * tmxData.tileheight

#Initialized to camera class for scrolling purpose
backgroundSpriteGroup = Camera(mapWidth, mapHeight)
background2SpriteGroup = Camera(mapWidth, mapHeight)
decorationSpriteGroup = Camera(mapWidth, mapHeight)
cloudsSpriteGroup = Camera(mapWidth, mapHeight)
liquidsSpriteGroup = Camera(mapWidth, mapHeight)
levelSpriteGroup = Camera(mapWidth, mapHeight)
finishedBlockSpriteGroup = Camera(mapWidth, mapHeight)

playerGroup = Camera(mapWidth, mapHeight)

#Making the empty list for the tiles that will have collision
collisionTiles = []

#Cycling through the layers in the data
for layer in tmxData.layers:

    targetGroup = None


    # Assign tiles to their specific group based on name
    if layer.name == "Background for background":
        targetGroup = background2SpriteGroup
    elif layer.name == "Background":
        targetGroup = backgroundSpriteGroup
    elif layer.name == "Level":
        targetGroup = levelSpriteGroup
    elif layer.name == "Decorations":
        targetGroup = decorationSpriteGroup
    elif layer.name == "Clouds":
        targetGroup = cloudsSpriteGroup
    elif layer.name == "Liquids":
        targetGroup = liquidsSpriteGroup
    elif layer.name == "FinishedBlock":
        targetGroup = finishedBlockSpriteGroup
        


    # Process the tiles for drawing and collision (X and Y are the coordinates, Surface is the image)
    for x, y, surface in layer.tiles():
        if surface:
            position = (x * 32, y * 32)
            
            # Add to collision list if the tile is in the Level layer
            if layer.name == "Level":
                rect = pygame.Rect(x * 32, y * 32, 32, 32)
                collisionTiles.append(rect)



            #Add transparency if the tile is in the Liquids layer
            elif layer.name == "Liquids":
                surface.set_alpha(150) 
                
                position = (x * 32, y * 32)
            




            # Add to the other layer to its own drawing group
            if targetGroup is not None:
                Tile(pos = position, surface = surface, groups = targetGroup)



def Tutorial(screen):

    #Setting the screen size
    pygame.display.set_caption("Roogey Boogey")



    #Initializing the clock class from pygame library 
    clock = pygame.time.Clock()
    FPS = 60 






    #RUNNING THE TUTORIAL
    #Setting the variable to be used to check if the game is running
    gameRunning = True


    #Making the character
    Knight = Player(400, 400)
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


        #Drawing the backgrounds to the game
        
        background2SpriteGroup.draw(Knight, screen)

        liquidsSpriteGroup.draw(Knight, screen)

        cloudsSpriteGroup.draw(Knight, screen)



        backgroundSpriteGroup.draw(Knight, screen)

        decorationSpriteGroup.draw(Knight, screen)


        
        
        levelSpriteGroup.draw(Knight, screen)
        
        
        finishedBlockSpriteGroup.draw(Knight, screen)



        #Initalizing the Player into the game 
        Knight.update(collisionTiles)

        playerGroup.draw(Knight, screen)
        




        #Checking for collision with the finishedBlockSpriteGroup
        for sprite in finishedBlockSpriteGroup.sprites():
            if Knight.rect.colliderect(sprite.rect):
                from Levels.Level1 import Level1
                Level1(screen)
                return
        



        # updates the frames of the game 
        pygame.display.update()    

    pygame.quit()