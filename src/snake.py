import pygame, random, sys # TO DO: Import only the things that I use instead of the complete module
pygame.init()

class Player(pygame.sprite.Sprite):
	def __init__(self, x = 380, y = 280, speed = 0.50):
		self.speed = speed
		self.movement = (0, 0)
		self.head = pygame.image.load("resources/snake_head.png")
		self.rect = self.head.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.rotatedHead = pygame.transform.rotate(self.head, 0)
		self.bodyParts = [
			pygame.image.load("resources/snake_body1.png"),
			pygame.image.load("resources/snake_body2.png")
		]

	def render(self, canvas):
		canvas.blit(self.rotatedHead, self.rect)
	
	def move(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					self.movement = (0, -10*self.speed)
					self.rotatedHead = pygame.transform.rotate(self.head, 90)
				if event.key == pygame.K_DOWN:
					self.movement = (0, 10*self.speed)
					self.rotatedHead = pygame.transform.rotate(self.head, 270)
				if event.key == pygame.K_RIGHT:
					self.movement = (10*self.speed, 0)
					self.rotatedHead = pygame.transform.rotate(self.head, 0)
				if event.key == pygame.K_LEFT:
					self.movement = (-10*self.speed, 0)
					self.rotatedHead = pygame.transform.rotate(self.head, 180)
		self.rect = self.rect.move(self.movement)
	
	def reset(self):
		self.rect.x = 380
		self.rect.y = 280