import pygame
from Functionality.button import Button
from Levels.Tutorial import Tutorial

def menu():
    #Initializing pygame
    pygame.init()





    #Initializing the clock class from pygame library 
    clock = pygame.time.Clock()
    FPS = 60 







    #Sets the display screen
    screen = pygame.display.set_mode((928, 793))
    pygame.display.set_caption("Roogey Boogey")







    #-----
    #Setting the directory for the font 
    def getFont():
        return("Assets/Fonts/pixelFont.ttf")







    #Setting the font for title 
    menuFont = pygame.font.Font(getFont(), 144)
    menuFontShadow = pygame.font.Font(getFont(), 144)





    #Making the background scroll and autoscroll
    scroll = 5
    autoScroll = 0.5





    #Menu Backgrounds
    #Putting the BG pictures into a list and ensuring it loads as transparent 
    menuBGs = []
    for i in range(0, 12):
        menuBG = pygame.image.load(f"Assets/BGLayers/MenuBGLayers/menuBG-{i}.png").convert_alpha()
        menuBGs.append(menuBG)
    menuBGWidth = menuBGs[0].get_width() #gets the width of one of the images for the scrolling
            








    #To showcase the background and scrolling speed of the background
    def drawMenuBG():
        for x in range(5):
            speed = 1
            for i in menuBGs:
                screen.blit(i, ((x * menuBGWidth) - scroll * speed,0))
                speed += 0.2







    #Title display
    def showTitle():
        #Title display
        gameTitle = menuFont.render("Roogey Boogey", True, "black")
        screen.blit(gameTitle, (33, 50))

        gameTitleShadow = menuFontShadow.render("Roogey Boogey", True, "white")
        screen.blit(gameTitleShadow, (43, 40))








    #RUNNING THE MENU TITLE
    #Setting the variable to be used to check if the game is running
    gameRunning = True


    #Setting the checker to see if the next transition
    nextScreen = None



    #BGM loading and playing
    pygame.mixer.init()
    pygame.mixer.music.load("Assets/BGM/TutorialBGM.ogg")
    pygame.mixer.music.play(-1, 0.0) # -1 = looping continously, 0.0 the timestamp


    #SFX loading and playing
    buttonSound = pygame.mixer.Sound("Assets/SFX/ButtonPress.mp3")


    while gameRunning:


        #Sets the tickrate to the targetted FPS
        clock.tick(FPS)


        #Drawing the background to the window
        drawMenuBG()


        #Title display
        showTitle()


        #Makes the background dynamicly scrolling
        scroll += autoScroll


        #Event handler for mouse position
        mousePos = pygame.mouse.get_pos()





        #BUTTONS TO BE CLICKED BY USER
        #Play button
        playButton = Button(image=pygame.image.load("Assets/BGLayers/MenuBGLayers/menuButtons/ButtonBG.png"), pos =(50, 580), textInput= "PLAY", font = pygame.font.Font(getFont(), 40), baseColor= "black", hoveringColor= "White")

        #Quit button
        quitButton = Button(image=pygame.image.load("Assets/BGLayers/MenuBGLayers/menuButtons/ButtonBG.png"), pos =(50, 730), textInput= "QUIT", font = pygame.font.Font(getFont(), 40), baseColor= "black", hoveringColor= "White")





        #changes the color if the user's mouse is hovering hovering over the button
        for button in [playButton, quitButton]:
            button.changeColor(mousePos)
            button.update(screen)





        #EVENT HANDLER
        #Event handler for exiting the game
        for event in pygame.event.get():
            #If the user just quits from window
            if event.type == pygame.QUIT:
                gameRunning = False

                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if playButton.checkForInput(mousePos):
                    buttonSound.play()
                    nextScreen = "Tutorial"
                    gameRunning = False


            #If user presses the button QUIT
            if event.type == pygame.MOUSEBUTTONDOWN:
                if quitButton.checkForInput(mousePos):
                    gameRunning = False

                    




        # updates the frames of the game 
        pygame.display.update()    

    if nextScreen == "Tutorial":
        Tutorial(screen)



#Only runs if open menu.py directly
if __name__ == "__main__":
    menu()