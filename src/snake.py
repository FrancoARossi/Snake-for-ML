import pygame, random, sys

class snake:
	length = 0
	x = 350
	y = 250
	headPos = (x, y)
	head = pygame.image.load("resources/snake_head.png")
	headHitBox = head.get_rect()
	bodyParts = [
		pygame.image.load("resources/snake_body1.png"),
		pygame.image.load("resources/snake_body2.png")
	]

	def render(self, canvas):
		canvas.blit(self.head, self.headPos)
	
	def move(self): # TERMINAR ESTO
		pressed = pygame.key.get_pressed()
		if pressed[pygame.K_UP]:
			flag = 0
		if pressed[pygame.K_DOWN]:
			flag = 1
		if pressed[pygame.K_RIGHT]:
			flag = 2
		if pressed[pygame.K_LEFT]:
			flag = 3
		if flag == 0:
			self.y -= 50
		if flag == 1:
			self.y += 50
		if flag == 2:
			self.x += 50
		if flag == 3:
			self.x -= 50
		self.headPos = (self.x, self.y)
		pygame.time.delay(200)