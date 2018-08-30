import pygame, random, snake, enviroment, food
pygame.init()
pygame.display.set_caption("Snake for ML")
size = 800, 600
screen = pygame.display.set_mode(size)

random.seed()
seed = []
player = snake.Player()
food = food.Apple()
leftLimit = enviroment.Limits(pygame.image.load("sprites/left_right_limit.png"), 0, 0)
rightLimit = enviroment.Limits(pygame.image.load("sprites/left_right_limit.png"), 760, 0)
upLimit = enviroment.Limits(pygame.image.load("sprites/up_down_limit.png"), 0, 0)
downLimit = enviroment.Limits(pygame.image.load("sprites/up_down_limit.png"), 0, 560)

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

	food.render(screen)

	snakeHead = player.snakeXnY[0]

	#TO DO: fix apple and snake colission
	if (food.foodXnY[0] - 20) <= snakeHead[0] <= food.foodXnY[0] and food.foodXnY[1] <= snakeHead[1] <= (food.foodXnY[1] + 20):
		food.reset()

	if snakeHead[0] <= 40 or snakeHead[0] >= 720 or snakeHead[1] <= 40 or snakeHead[1] >= 520:
		player.reset()

	pygame.display.flip()