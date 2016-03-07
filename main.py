import pygame
import sys
import random
pygame.init()
# def move(self, x, y):
	# 	if x != 0:
	# 		self.move_single_axis(x, 0)
	# 	if y != 0:
	# 		self.move_single_axis(0, y)
	# def move_single_axis(self, x, y):
	# 	self.rect.x += x
	# 	self.rect.y += y
class Paddle(object):
	def __init__(self):
		self.rect = pygame.Rect(10,0, 10, 100)

		self.speed_x = 0
		self.speed_y = 0

	def update(self):
		self.rect.x += self.speed_x
		self.rect.y += self.speed_y

		key = pygame.key.get_pressed()
		if key[pygame.K_UP]:
			self.speed_y = -2
		else:
			self.speed_y = 0
		if key[pygame.K_DOWN]:
			self.speed_y = 2

class Ball(object):
	def __init__(self):
		self.rect = pygame.Rect(WIDTH/2, HEIGHT/2, 16, 16)

		self.speed_x = -2
		self.speed_y = 0

	def update(self):
		# Update rect position
		self.rect.x += self.speed_x
		self.rect.y += self.speed_y


	def collions(self):
		if self.rect.colliderect(paddle.rect):
			# When ball hits paddle, need to reverse the direction
			# it's travelling in
			self.speed_x = -self.speed_x
			self.speed_y = -self.speed_y


WIDTH = 640
HEIGHT = 320
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

clock = pygame.time.Clock()
ball = Ball()
paddle = Paddle()
running = True

while running:
	clock.tick(60)
	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			running = False
	# key = pygame.key.get_pressed()
	# if key[pygame.K_UP]:
	# 	paddle.move(0, -2)
	# if key[pygame.K_DOWN]:
	# 	paddle.move(0, 2)

	screen.fill((0,0,0))
	pygame.draw.rect(screen, (255,255,255), ball.rect)
	ball.update()
	ball.collions()
	pygame.draw.rect(screen, (32, 123, 29), paddle.rect)
	paddle.update()
	pygame.display.update()
