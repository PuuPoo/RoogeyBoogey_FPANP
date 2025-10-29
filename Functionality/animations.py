import pygame
class animationSheet():

    def __init__(self, animation):

        #Setting the assetPath for the animation
        self.assetPath = animation





    #constructor for animation 
    #startX and startY is basically the asset starting coordinates on the animation sheet
    #frameWidth and frameHeight is the frame window of the animation 
    #frameGap is the gap between frames
    #scale is the scaling of the image
    #numFrames is the number of frames in the image sheet
    def loadAnimation(self, startX, startY, frameWidth, frameHeight, frameGap, scale, numFrames):

        #Empty list to store animation
        frames = []

        #Inputting the animation into the list
        for i in range(numFrames):

            current_startY = startY[i]

            #Creates a blank surface or frame window for the animation frame
            animationFrame = pygame.Surface((frameWidth, frameHeight), pygame.SRCALPHA).convert_alpha()
            #SRCALPHA is used to create the transparent background for the asset

            #Extracting the frame from the animation sheet
            animationFrame.blit(self.assetPath, (0, 0), ((startX + i * (frameWidth + frameGap), current_startY, frameWidth, frameHeight))) 

            #Scaling the frame to the desired scale given
            animationFrame = pygame.transform.scale(animationFrame, (frameWidth * scale, frameHeight * scale))


            #adding the animation frame to the frame list
            frames.append(animationFrame)


        return frames
