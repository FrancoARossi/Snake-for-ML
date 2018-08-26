import pygame, random, snake, enviroment
pygame.init()
pygame.display.set_caption("Snake for ML")
size = 800, 600
screen = pygame.display.set_mode(size)

random.seed()
seed = []
player = snake.Player()
leftLimit = enviroment.Limits(pygame.image.load("resources/left_right_limit.png"), 0, 0)
rightLimit = enviroment.Limits(pygame.image.load("resources/left_right_limit.png"), 760, 0)
upLimit = enviroment.Limits(pygame.image.load("resources/up_down_limit.png"), 0, 0)
downLimit = enviroment.Limits(pygame.image.load("resources/up_down_limit.png"), 0, 560)

for i in range(49):
	seed.append(random.randrange(0,3))

while True:
	enviroment.render_background(screen, seed)
	leftLimit.render_limit(screen)
	rightLimit.render_limit(screen)
	upLimit.render_limit(screen)
	downLimit.render_limit(screen)

	player.render(screen)
	player.move()

	if pygame.sprite.collide_rect(player, leftLimit) or pygame.sprite.collide_rect(player, rightLimit) or pygame.sprite.collide_rect(player, upLimit) or pygame.sprite.collide_rect(player, downLimit):
		player.reset()

	pygame.display.flip()