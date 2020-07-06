import pygame
import os
import sys
from bullet import Bullet

class Character(pygame.sprite.Sprite):
	'''
	Character class that handles movement and user input
	'''

	def __init__(self, platforms, bullets):
		pygame.sprite.Sprite.__init__(self)
		image = pygame.image.load(os.path.join('sprite_art','Jungle Asset Pack','Character','sprites','run5.png'))
		self.image = pygame.transform.scale(image, (50,50))
		self.width, self.height = 50, 50
		self.rect = self.image.get_rect()
		self.rect.x += 50
		self.x = 0
		self.y = 0
		self.gravity = 4.9
		self.platforms = platforms
		self.bullets = bullets
		self.clock = pygame.time.Clock()
		self.jumping = False
		self.jump = 10
		self.hit = False
		self.can_jump = False

	def move(self, x, y):
		self.x += x
		self.y += y

	def update(self, tick):
		self.rect.x += self.x
		self.x = 0
		fitness = 0
		if self.jumping:
			if self.jump >= 0:
				self.rect.y -= (self.jump * abs(self.jump)) * 0.5
				self.jump -= 1
			else:
				self.jump = 10
				self.jumping = False

		if not any([pygame.sprite.collide_rect(self, platform) for platform in self.platforms]):
			self.rect.y += self.y + self.gravity
			self.can_jump = False
		else:
			for platform in self.platforms:
				if pygame.sprite.collide_rect(self, platform):
					if self.rect.bottom > platform.rect.bottom:
						self.rect.y += self.y + self.gravity
						self.can_jump = False
					else:
						self.rect.y += self.y
						self.jumping = False
						self.can_jump = True
						fitness += 2
		#self.move_left(tick)
		if any([pygame.sprite.collide_rect(self, bullet) for bullet in self.bullets]):
			self.hit = True
		return fitness


	def move_left(self, tick):
		speed = .0589
		#clock = pygame.time.Clock()
		left = tick*speed
		self.rect.x = self.rect.x - left

	def shoot(self):
		return Bullet(self.rect.x, self.rect.y, 1)



if __name__ == "__main__":
	display = pygame.display.set_mode([400, 400])
	clock = pygame.time.Clock()
	character = Character()
	characters = pygame.sprite.Group()
	characters.add(character)
	while True:
		for e in pygame.event.get():
			if e.type is pygame.KEYDOWN:
				if e.key == ord('a'):
					character.move(-10, 0)
				elif e.key == ord('d'):
					character.move(10, 0)
				elif e.type is pygame.K_SPACE:
					print("space")
			if e.type is pygame.KEYUP:
				if e.key == ord('a'):
					character.move(10, 0)
				elif e.key == ord('d'):
					character.move(-10, 0)
				elif e.type is pygame.K_SPACE:
					print("space")

			if e.type is pygame.QUIT:
				pygame.quit()
				sys.exit(0)

		character.update()
		display.fill((25,25,200))
		characters.draw(display)
		pygame.display.flip()
		clock.tick(30)
