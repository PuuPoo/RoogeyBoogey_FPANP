import pygame
class animationSheet():

    def __init__(self, animation):
        self.assetPath = animation

    def loadAnimation(self, startX, startY, frameWidth, frameHeight, frameGap, scale, numFrames):

        frames = []

        for i in range(numFrames):
            animationFrame = pygame.Surface((frameWidth, frameHeight), pygame.SRCALPHA).convert_alpha()
            animationFrame.blit(self.assetPath, (0, 0), ((startX + i * (frameWidth + frameGap), startY, frameWidth, frameHeight))) 
            print((startX + i * (frameWidth + frameGap)))
            animationFrame = pygame.transform.scale(animationFrame, (frameWidth * scale, frameHeight * scale))
            frames.append(animationFrame)


        return frames
