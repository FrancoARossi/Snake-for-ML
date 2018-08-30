import pygame, random
pygame.init()

class Apple(pygame.sprite.Sprite):
	apple = pygame.image.load("sprites/food.png")
	rect = apple.get_rect()
	foodXnY = (random.randrange(60, 720), random.randrange(60, 520))

	def render(self, canvas):
		canvas.blit(self.apple, self.foodXnY)
	
	def reset(self):
		self.foodXnY = (random.randrange(60, 720), random.randrange(60, 520))