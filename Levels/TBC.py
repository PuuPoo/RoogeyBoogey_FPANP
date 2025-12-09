import pygame
from pytmx.util_pygame import load_pygame
from Character.Player import Player
from Functionality.Tile import Tile
from Functionality.camera import Camera


def TBC(screen):


    #Setting the screen size
    pygame.display.set_caption("Roogey Boogey")


    #Initializing the clock class from pygame library 
    clock = pygame.time.Clock()
    FPS = 60 




    #RUNNING THE LEVEL
    #Setting the variable to be used to check if the game is running
    gameRunning = True



    #Setting the directory for the font 
    def getFont():
        return("Assets/Fonts/pixelFont.ttf")


    #Setting the font for title 

    menuFont = pygame.font.Font(getFont(), 100)


    #Title display
    def showTBC():
        #Title display

        tbcText = menuFont.render("To Be Continued...", True, "white")
        screen.blit(tbcText, (120, 380))


    while gameRunning:
        #Sets the tickrate to the targetted FPS
        clock.tick(FPS)


        #EVENT HANDLER
        #Event handler for exiting the game
        for event in pygame.event.get():
            #If the user just quits from window
            if event.type == pygame.QUIT:
                gameRunning = False

    
        screen.fill((0, 0, 0))

        #Title display
        showTBC()

        
        # updates the frames of the game 
        pygame.display.update()    

    pygame.quit()


