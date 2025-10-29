import pygame
from Functionality import animations

screen = pygame.display.set_mode((928, 793))

#Player Class
class Player():
    

    #Player Constructor
    def __init__(self, x, y):


        #PLAYER ANIMATION
        
        #Main list to store all the animation frames 
        self.allCharacterAnimation = []

        #Counter to hold which type of animation should be played
        self.action = 0
        #Counter to track the previous action state
        self.previousAction = 0

        #Attacking state check
        self.isAttacking = False

        self.offsetx = 0


        #Creating the path to the Animation sheets
        characterIdleAnimation = pygame.image.load("Assets/Character/PlayerIdle.png").convert_alpha()
        characterWalkAnimation = pygame.image.load("Assets/Character/PlayerWalk.png").convert_alpha()
        characterAttkAnimation = pygame.image.load("Assets/Character/PlayerAttk.png").convert_alpha()



        #Making the animation class and sending the folder path
        idleSheet = animations.animationSheet(characterIdleAnimation)
        walkSheet = animations.animationSheet(characterWalkAnimation)
        attkSheet = animations.animationSheet(characterAttkAnimation)
        

        idle_y_list = [38, 38, 38, 38, 38, 38] 
        walk_y_list = [38, 38, 38, 38, 38, 38, 38, 38] # Example, you'll need actual values
        attk_y_list = [38, 31, 32, 35, 41, 40] # Example, using the lowest point (31) for attack


        #Calling the method to construct the animation sheet
        self.idleFrames = idleSheet.loadAnimation(41, idle_y_list, 16, 18, 84, 7, 6)
        self.walkFrames = walkSheet.loadAnimation(41, walk_y_list, 16, 18, 84, 7, 8)
        self.attkFrames = attkSheet.loadAnimation(41, attk_y_list, 32, 23, 68, 7, 6)

        #Storing all the animation into 1 list
        self.allCharacterAnimation.append(self.idleFrames)
        self.allCharacterAnimation.append(self.walkFrames)
        self.allCharacterAnimation.append(self.attkFrames)



        #Starting frame, each frame's speed before it changes, and the timer before it resets to first frame
        self.currentFrame = 0
        self.animationSpeed = 0.1
        self.frameTimer = 0
        self.flip = False




        #Sets the initial image that will be on screen
        self.characterAsset = self.idleFrames[self.currentFrame]




        

        self.rect = self.characterAsset.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocityY = 0 #Y velocity to go up 
        self.isJumping = False #Checks if player jumps


    #Player Attack Animation --------------------------------------------------------------------------------------
    def attack(self):
        if self.isAttacking == False:
            self.isAttacking = True
            self.currentFrame = 0
            self.frameTimer = 0


    #Player updater (draws the player on the screen) ---------------------------------------------------------------------------
    def update(self):
        



        #Getting controls for the player   
        #Used to check if the change in the coordinates will be viable if there is a obstacle or not
        dx = 0
        dy = 0
        key = pygame.key.get_pressed()

        #Controls --------------------------------------------------------------------------------------------
        if key[pygame.K_a]:
            dx -= 5
            self.flip = True

        if key[pygame.K_d]:
            dx += 5
            self.flip = False

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
        if self.rect.bottom > 690:
            self.rect.bottom = 690
            dy = 0








        #ANIMATION LOGIC ----------------------------------------------------------------------------------------
        #Changing animation based on movement
        if self.isAttacking:
            self.action = 2
        elif dx != 0:
            self.action = 1
        else:
            self.action = 0


        #Checks if there is change in player action. If there is resets all frame back to 0 along with the timer
        if self.action != self.previousAction:
            self.currentFrame = 0
            self.frameTimer = 0
            self.previousAction = self.action 






        #Gets the animation frames from the main list and puts the needed one in the current animation list
        currentAnimationList = self.allCharacterAnimation[self.action]


        #Increases the frame timer with the animation speed timer 
        self.frameTimer += self.animationSpeed

        # When timer reaches 1, switch frames to the one after it, when it reaches its length resets back to 0
        if self.frameTimer >= 1:
            self.currentFrame += 1
            self.frameTimer = 0

            #Checks if the attack animation is over
            if self.action == 2 and self.currentFrame >= len(currentAnimationList):
                self.isAttacking = False  # Resets the attack back to false
                self.action = 0           # Return to idle animation
                self.currentFrame = 0     # Start the idle animation from frame 0

            # For all other animations, loop normally
            elif self.currentFrame >= len(currentAnimationList):
                self.currentFrame = 0




        #Gets the wanted frame from the current list to be drawned
        frameDrawn = currentAnimationList[self.currentFrame]


        #The updated frame is shown to the screen
        self.characterAsset = pygame.transform.flip(frameDrawn, self.flip, False)


        



        #Drawing player into the screen
        screen.blit(self.characterAsset, self.rect)
    