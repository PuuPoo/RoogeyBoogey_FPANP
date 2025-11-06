import pygame
from Character.Player import Player

class Camera(pygame.sprite.Group):

    def __init__(self):
        super().__init__()


    #Takes the player and the display that will be rendered
    def draw(self, target: Player, display: pygame.Surface):

        #creates a 2d vector to store how much the camera will shift
        offset = pygame.math.Vector2()

        #Calculate horizontal and vertical offset  (Center of the screen - Players x and Y position in the world)
        offset.x = display.get_width() / 2 - target.rect.centerx
        offset.y = display.get_height() / 2 - target.rect.centery



        #Loops through every sprite in the camera group
        for sprite in self.sprites():
            
            #creates a 2d vector to store the shifted sprite position 
            spriteOffset = pygame.math.Vector2()

            #Add the camera offset to the sprite's world position
            spriteOffset.x = offset.x + sprite.rect.x
            spriteOffset.y = offset.y + sprite.rect.y


            #Draw the sprite with the new offset position
            display.blit(sprite.image, spriteOffset)
