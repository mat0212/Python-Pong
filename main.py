import pygame
import sys
import random

pygame.init()

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

	screen.fill((0,0,0))
	ball.update()
	ball.collions()
	pygame.draw.rect(screen, (255,255,255), ball.rect)
	paddle.update()
	pygame.display.update()
	pygame.draw.rect(screen, (32, 123, 29), paddle.rect)
