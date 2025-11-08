import pygame
from Functionality import animations

screen = pygame.display.set_mode((928, 793))

#Player Class
class Player(pygame.sprite.Sprite):
    

    #Player Constructor
    def __init__(self, x, y):
        super().__init__()


        #PLAYER ANIMATION
        
        #Main list to store all the animation frames 
        self.allCharacterAnimation = []

        #Counter to hold which type of animation should be played
        self.action = 0
        #Counter to track the previous action state
        self.previousAction = 0

        #Attacking state check
        self.isAttacking = False



        #Creating the path to the Animation sheets
        characterIdleAnimation = pygame.image.load("Assets/Character/PlayerIdle.png").convert_alpha()
        characterWalkAnimation = pygame.image.load("Assets/Character/PlayerWalk.png").convert_alpha()
        characterAttkAnimation = pygame.image.load("Assets/Character/PlayerAttk.png").convert_alpha()



        #Making the animation class and sending the folder path
        idleSheet = animations.animationSheet(characterIdleAnimation)
        walkSheet = animations.animationSheet(characterWalkAnimation)
        attkSheet = animations.animationSheet(characterAttkAnimation)
        

        #Made the list of the frames starting y coordinates cuz cant find logic to do it well
        idleYList = [38, 38, 38, 38, 38, 38] 
        walkYList = [38, 38, 38, 38, 38, 38, 38, 38] 
        attkYList = [38, 31, 32, 35, 41, 40] 


        #Calling the method to construct the animation sheet
        self.idleFrames = idleSheet.loadAnimation(41, idleYList, 16, 18, 84, 2.4, 6)
        self.walkFrames = walkSheet.loadAnimation(41, walkYList, 16, 18, 84, 2.4, 8)
        self.attkFrames = attkSheet.loadAnimation(41, attkYList, 32, 23, 68, 2.4, 6)

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
        self.image = self.idleFrames[self.currentFrame]




        

        self.rect = self.image.get_rect()
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
    def update(self, collisionTiles):
        



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
        if ((key[pygame.K_w] or key[pygame.K_SPACE]) and self.isJumping == False and self.velocityY == 0) :
            self.velocityY = -11
            self.isJumping = True





        #Gravity and jump
        self.velocityY += 1

        #Maximum velocity / gravity
        if self.velocityY > 10:
            self.velocityY = 10

        #Adding the delta y with the velocity to ensure player will go down after jumping and up when jumping
        dy += self.velocityY
    


        #Checking for collision
        self.rect.x += dx

        

        #Checking horizontal movement
        for tile in collisionTiles:
                if self.rect.colliderect(tile): #Checking for collition of tile
                    if dx > 0: 
                        self.rect.right = tile.left # Stop player at the left side of the tile
                        dx = 0 # Stop horizontal movement




                    elif dx < 0: 
                        self.rect.left = tile.right # Stop player at the right side of the tile
                        dx = 0 # Stop horizontal movement






        #Check and apply vertical movement (Y-axis)
        self.rect.y += dy
            
        self.on_ground = False # Assume not on ground until a collision says otherwise
            
        for tile in collisionTiles:
            if self.rect.colliderect(tile):
                if dy > 0:
                    self.rect.bottom = tile.top # Land player on top of the tile
                    self.velocityY = 0 # Velocity = 0, stops gravity

                    self.isJumping = False 
                    self.on_ground = True


                elif dy < 0:
                    self.rect.top = tile.bottom # Stop player at the bottom of the tile
                    self.velocityY = 0 #Stops player velocity going up 











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
        self.image = pygame.transform.flip(frameDrawn, self.flip, False)


        


    