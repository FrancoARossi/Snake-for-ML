import pygame, random, snake
pygame.init()
random.seed()
size = 800, 600
player = snake.Player()
r = []

for i in range(49):
	r.append(random.randrange(0,3))

# TO DO?: put generate_background on a separated file
def generate_background(canvas, tilesArray, r):
	i = 0
	for x in range(0, 800, 100):
		for y in range(0, 600, 100):
			i += 1
			canvas.blit(tilesArray[r[i]], (x, y))

screen = pygame.display.set_mode(size)
backgroundTiles = [
	pygame.image.load("resources/background_tile1.png").convert(), 
	pygame.image.load("resources/background_tile2.png").convert(),
	pygame.image.load("resources/background_tile3.png").convert()
	]


while True:
	generate_background(screen, backgroundTiles, r)

	player.render(screen)
	player.move()

	pygame.display.flip()