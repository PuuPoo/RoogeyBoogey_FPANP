import pygame
from Functionality import animations

screen = pygame.display.set_mode((928, 793))

#Player Class
class Player():
    

    #Player Constructor
    def __init__(self, x, y):


        #PLAYER ANIMATION
        #Creating the path to the idleAnimation sheet
        characterIdleAnimation = pygame.image.load("Assets/Character/Player.png").convert_alpha()




        #Making the animation class and sending the folder path
        idleSheet = animations.animationSheet(characterIdleAnimation)




        #Calling the method to construct the animation sheet
        self.idleFrames = idleSheet.loadAnimation(41, 38, 16, 18, 84, 7, 6)




        #Starting frame, each frame's speed before it changes, and the timer before it resets to first frame
        self.currentFrame = 0
        self.animationSpeed = 0.1
        self.frameTimer = 0




        #Sets the initial image that will be on screen
        self.characterAsset = self.idleFrames[self.currentFrame]




        

        self.rect = self.characterAsset.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocityY = 0 #Y velocity to go up 
        self.isJumping = False #Checks if player jumps


    


    #Player updater (draws the player on the screen)
    def update(self):
        



        #Getting controls for the player   
        #Used to check if the change in the coordinates will be viable if there is a obstacle or not
        dx = 0
        dy = 0
        key = pygame.key.get_pressed()

        #Controls
        if key[pygame.K_a]:
            dx -= 5

        if key[pygame.K_d]:
            dx += 5

        #Check for player input to jump 
        if (key[pygame.K_w] or key[pygame.K_SPACE]) and self.isJumping == False:
            self.velocityY = -15
            self.isJumping = True

        #Give back the ability for the player to jump again
        if (key[pygame.K_w] or key[pygame.K_SPACE]) == False:
            self.isJumping = False
    
        #Gravity and jump
        self.velocityY += 1

        #Maximum velocity / gravity
        if self.velocityY > 10:
            self.velocityY = 10

        #Adding the delta y with the velocity to ensure player will go down after jumping and up when jumping
        dy += self.velocityY
    
        #Checking for collision
        self.rect.x += dx
        self.rect.y += dy







        #TEMP WILL CHANGE (TO ENSURE THEY DONT FALL OFF SCREEN)
        if self.rect.bottom > 793:
            self.rect.bottom = 793
            dy = 0








        #ANIMATION LOGIC

        #Increases the frame timer with the animation speed timer 
        self.frameTimer += self.animationSpeed

        #When timer reaches 1, switch frames to the one after it, when it reaches its length resets back to 0
        if self.frameTimer >= 1:
            self.currentFrame = (self.currentFrame + 1) % len(self.idleFrames)
            self.frameTimer = 0


        #The updated frame is shown to the screen
        self.characterAsset = self.idleFrames[self.currentFrame]



        #Drawing player into the screen
        screen.blit(self.characterAsset, self.rect)
    