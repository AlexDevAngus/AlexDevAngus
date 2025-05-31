import pygame
pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Moving Circle!")
RED = (255, 0, 0)
circle_x, circle_y = 250, 250
running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				circle_x -= 10
			elif event.key == pygame.K_RIGHT:
				circle_x += 10
			elif event.key == pygame.K_UP:
				circle_y -= 10
			elif event.key == pygame.K_DOWN:
				circle_y += 10
	screen.fill((0, 0, 0))
	pygame.draw.circle(screen, RED, (circle_x, circle_y), 50)
	pygame.display.flip()
pygame.quit()
