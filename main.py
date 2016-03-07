import pygame
import sys
import random
pygame.init()

class Paddle(object):
	def __init__(self):
		self.rect = pygame.Rect(10,0, 10, 100)

	def move(self, x, y):
		if x != 0:
			self.move_single_axis(x, 0)
		if y != 0:
			self.move_single_axis(0, y)
	def move_single_axis(self, x, y):
		self.rect.x += x
		self.rect.y += y

class Ball(object):
	def __init__(self):
		self.rect = pygame.Rect(WIDTH/2, HEIGHT/2, 16, 16)
		self.ball_x = WIDTH/2
		self.ball_y = HEIGHT/2


	def update(self):
		self.rect.x = self.ball_x
		self.rect.y = self.ball_y
		FREEX = True
		FREEY = True
		if FREEX == True:
			self.ball_x -= 1

		self.ball_y += 0
		print(self.ball_y)
	def collions(self):
		# if self.ball_y > HEIGHT:
		# 	self.ball_y -=10
		# 	print(self.ball_y)

		if self.rect.colliderect(paddle.rect):
			FREEX = False
			self.ball_x += 1
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
	key = pygame.key.get_pressed()
	if key[pygame.K_UP]:
		paddle.move(0, -2)
	if key[pygame.K_DOWN]:
		paddle.move(0, 2)

	screen.fill((0,0,0))
	pygame.draw.rect(screen, (255,255,255), ball.rect)
	ball.update()
	ball.collions()
	pygame.draw.rect(screen, (32, 123, 29), paddle.rect)
	pygame.display.update()