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

		# Not using FREEX anymore, instead using speed_x and speed_y
		self.speed_x = -2
		self.speed_y = 0

	def update(self):
		# Now, instead of checking the values of FREEX and FREEY
		# We can just add the speed of the ball onto its position
		self.rect.x += self.speed_x
		self.rect.y += self.speed_y
		# Remember, that happens every frame, so if speed_x = 1 then
		# the ball will move right by 1 every frame!
		
		# Move the rectangle
		#self.rect.x = self.speed_x
		#self.rect.y = self.speed_y


	def collions(self):
		if self.rect.colliderect(paddle.rect):
			# Now, here, instead of doing anything with FREEX
			# we can just reverse the speed of the ball, to make it
			# go the other way.
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
