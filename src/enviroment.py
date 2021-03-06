import pygame
pygame.init()

backgroundSprites = [
	pygame.image.load("sprites/background_tile1.png"), 
	pygame.image.load("sprites/background_tile2.png"),
	pygame.image.load("sprites/background_tile3.png"),
	]

class Limits(pygame.sprite.Sprite):
	def __init__(self, limitSprite, x, y):
		self.limitSprite = limitSprite
		self.limitXnY = (x, y)

	def render_limit(self, canvas):
		canvas.blit(self.limitSprite, self.limitXnY)

def render_background(canvas, seed):
	i = 0
	for x in range(0, 800, 100):
		for y in range(0, 600, 100):
			i += 1
			canvas.blit(backgroundSprites[seed[i]], (x, y))