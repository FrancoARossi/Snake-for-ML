import pygame, random, sys # TO DO: Import only the needed modules
pygame.init()

class Player(pygame.sprite.Sprite):
	def __init__(self, x = 380, y = 280, speed = 0.50):
		self.speed = speed
		self.movement = (0, 0)
		self.head = pygame.image.load("sprites/snake_head.png")
		self.rotatedHead = pygame.transform.rotate(self.head, 0)
		self.headXnY = (x, y)
		self.bodySprites = [
			pygame.image.load("sprites/snake_body1.png"),
			pygame.image.load("sprites/snake_body2.png")
		]
		self.snakeXnY = [self.headXnY]
		self.i = 0


	def render(self, canvas):
		canvas.blit(self.rotatedHead, self.snakeXnY[0])
		#for self.i in range(len(self.snakeXnY)):
		#	canvas.blit(self.bodySprites[random.randrange(0,2)], self.snakeXnY[self.i])
	
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
		self.snakeXnY[0] = (int(self.snakeXnY[0][0] + self.movement[0]), int(self.snakeXnY[0][1] + self.movement[1]))
	
	def reset(self):
		self.snakeXnY = [self.headXnY]
		self.snakeXnY[0] = (380, 280)