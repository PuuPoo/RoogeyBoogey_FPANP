import pygame
from Character.Player import Player

class Camera(pygame.sprite.Group):

    def __init__(self, mapWidth = 0, mapHeight = 0):
        super().__init__()
        self.mapWidth = mapWidth
        self.mapHeight = mapHeight


    #Takes the player and the display that will be rendered
    def draw(self, target: Player, display: pygame.Surface):

        #creates a 2d vector to store how much the camera will shift
        offset = pygame.math.Vector2()

        #Calculate horizontal and vertical offset  (Center of the screen - Players x and Y position in the world)
        offset.x = display.get_width() / 2 - target.rect.centerx
        offset.y = display.get_height() / 2 - target.rect.centery


        #Clamping the camera to never go beyond map size
        #Setting the maximum limit for top and left edge of the map
        maxX = 0
        maxY = 0

        #Setting the limit for the bottom and right edge of the map
        minX = display.get_width() - self.mapWidth
        minY = display.get_height() - self.mapHeight

        if offset.x > maxX:
            offset.x = maxX
        elif offset.x < minX:
            offset.x = minX

        if offset.y > maxY:
            offset.y = maxY
        elif offset.y < minY:
            offset.y = minY





        #Loops through every sprite in the camera group
        for sprite in self.sprites():
            
            #creates a 2d vector to store the shifted sprite position 
            spriteOffset = pygame.math.Vector2()

            #Add the camera offset to the sprite's world position
            spriteOffset.x = offset.x + sprite.rect.x
            spriteOffset.y = offset.y + sprite.rect.y


            #Draw the sprite with the new offset position
            display.blit(sprite.image, spriteOffset)
