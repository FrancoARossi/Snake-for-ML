import pygame, random, sys # TO DO: Import only the things that I use instead of the complete module

class Player:
	def __init__(self, x = 350, y = 250, speed = 0.45):
		self.x = x
		self.y = y
		self.speed = speed
		self.movement = (0, 0)
		self.head = pygame.image.load("resources/snake_head.png")
		self.headHitBox = self.head.get_rect(center = (self.x, self.y))
		self.bodyParts = [
			pygame.image.load("resources/snake_body1.png"),
			pygame.image.load("resources/snake_body2.png")
		]

	def render(self, canvas):
		canvas.blit(self.head, self.headHitBox)
	
	def move(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					self.movement = (0, -25*self.speed)
				if event.key == pygame.K_DOWN:
					self.movement = (0, 25*self.speed)
				if event.key == pygame.K_RIGHT:
					self.movement = (25*self.speed, 0)
				if event.key == pygame.K_LEFT:
					self.movement = (-25*self.speed, 0)
		self.headHitBox = self.headHitBox.move(self.movement)
		pygame.time.delay(30)
	
	def rotate(lastKey, newKey):
		pass