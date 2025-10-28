class Button():
	
    #Initialize the button class
	def __init__(self, image, pos, textInput, font, baseColor, hoveringColor):
		self.image = image 
		self.xPos = pos[0] #Position of the button in terms of width
		self.yPos = pos[1] #Position of the button in terms of height
		self.font = font    #Font of the button
		self.baseColor, self.hoveringColor = baseColor, hoveringColor 
		self.textInput = textInput
		self.text = self.font.render(self.textInput, True, self.baseColor)
		if self.image is None:
			self.image = self.text
		self.rect = self.image.get_rect(center=(self.xPos, self.yPos))
		self.textRect = self.text.get_rect(center=(self.xPos, self.yPos))


    #Displays the button on the screen
	def update(self, screen):
		if self.image is not None:
			screen.blit(self.image, self.rect)
		screen.blit(self.text, self.textRect)


    #Checks if the button is being pressed
	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False


    #If the mouse is hovering over the button changes colors/hues
	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.textInput, True, self.hoveringColor)
		else:
			self.text = self.font.render(self.textInput, True, self.baseColor)