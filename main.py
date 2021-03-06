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
		
class Ball(object):
	def __init__(self):
		self.rect = pygame.Rect(WIDTH/2, HEIGHT/2, 16, 16)
		self.P1_score = 0
		self.P2_score = 0

		self.speed_x = -2
		self.speed_y = 2

	def update(self):
		self.rect.x += self.speed_x
		self.rect.y += self.speed_y
		

	def collions(self):
		# Check BOTH paddles for a collision!
		# if self.rect.colliderect(paddle1.rect) or self.rect.colliderect(paddle2.rect):
		# 	self.speed_x = -self.speed_x
		# 	self.speed_y = -self.speed_y
		if self.rect.colliderect(paddle1.rect):
			self.speed_x -= 1
			self.speed_y -= 1
			self.speed_x = -self.speed_x
			self.speed_y = -self.speed_y
			print(self.speed_x)
			print(self.speed_y)
		if self.rect.colliderect(paddle2.rect):	
			self.speed_x += 1
			self.speed_y += 1
			self.speed_y = -self.speed_y
			self.speed_x = -self.speed_x
			print(self.speed_x)
			print(self.speed_y)
		elif self.rect.y > HEIGHT:
			self.speed_y = -self.speed_y
		elif self.rect.y < 0:
			self.speed_y = -self.speed_y
		elif self.rect.x < 0:
			self.speed_x = 2
			self.speed_x = -2
			self.speed_y = 2
			self.P2_score += 1
			self.rect.x = WIDTH/2
			self.rect.y = HEIGHT/2
		elif self.rect.x > 640:
			self.speed_x = -2
			self.speed_y = 2
			self.P1_score += 1
			self.rect.x = WIDTH/2
			self.rect.y = HEIGHT/2
	def score(self):
		self.myfont = pygame.font.SysFont("monospace", 15)
		self.label = self.myfont.render("         P1Score = " + str(self.P1_score), 1, (18,15,210))
		self.label2 = self.myfont.render("                                           P2Score = " + str(self.P2_score), 1, (92,19,189))
		screen.blit(self.label, (0, 0))
		screen.blit(self.label2, (0,0))



WIDTH = 640
HEIGHT = 320
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

clock = pygame.time.Clock()
ball = Ball()

# :::::::NOTICE:::::::
# Here I create 2 paddles! But only using 1 class!
paddle1 = Paddle()
paddle2 = Paddle()

# Set the paddle positions
paddle1.rect.x = 10
paddle1.rect.y = 0
paddle2.rect.x = WIDTH - 20
paddle2.rect.y = 0

running = True

while running:
	clock.tick(60)
	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			running = False

	# This is the code for paddle movement!
	key = pygame.key.get_pressed()

	# The paddle 1 movement (Left side)
	# We use W and S to control the left hand side
	if key[pygame.K_w]:
		paddle1.speed_y = -2
	elif key[pygame.K_s]:
		paddle1.speed_y = 2
	else:
		paddle1.speed_y = 0

	# The paddle 2 movement (Right side)
	# We use Up and Down to control the right hand side
	if key[pygame.K_UP]:
		paddle2.speed_y = -2
	elif key[pygame.K_DOWN]:
		paddle2.speed_y = 2
	else:
		paddle2.speed_y = 0

	screen.fill((0,0,0))
	# Separated the render code from the update code
	ball.update()
	ball.collions()
	ball.score()
	# Remember to update and draw both paddles!
	paddle1.update()
	paddle2.update()

	# This is the rendering code!
	pygame.draw.rect(screen, (255,255,255), ball.rect)
	pygame.draw.rect(screen, (32, 123, 29), paddle1.rect)
	pygame.draw.rect(screen, (32, 123, 29), paddle2.rect)

	pygame.display.update()
