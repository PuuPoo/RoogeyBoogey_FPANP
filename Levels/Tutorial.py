import pygame
from Character.Player import Player

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
    Knight = Player(200, 200)


    while gameRunning:
        #Sets the tickrate to the targetted FPS
        clock.tick(FPS)


        #EVENT HANDLER
        #Event handler for exiting the game
        for event in pygame.event.get():
            #If the user just quits from window
            if event.type == pygame.QUIT:
                gameRunning = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    Knight.attack()

    
        screen.fill((255, 255, 255))


        #Initalizing the Player into the game 
        Knight.update()
        


        # updates the frames of the game 
        pygame.display.update()    

    pygame.quit()