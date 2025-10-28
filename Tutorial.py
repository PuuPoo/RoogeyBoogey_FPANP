import pygame

def Tutorial(screen):

    #Setting the screen size
    screen = pygame.display.set_mode((928, 793))
    pygame.display.set_caption("Roogey Boogey")



    #Initializing the clock class from pygame library 
    clock = pygame.time.Clock()
    FPS = 60 






    #RUNNING THE TUTORIAL
    #Setting the variable to be used to check if the game is running
    gameRunning = True





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


        # updates the frames of the game 
        pygame.display.update()    

    pygame.quit()