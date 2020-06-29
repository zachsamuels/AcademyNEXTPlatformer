import pygame
import os
import sys

class Character(pygame.sprite.Sprite):
	'''
	Character class that handles movement and user input
	'''

	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		image = pygame.image.load(os.path.join('images', 'character.png'))
		self.image = pygame.transform.scale(image, (50,50))
		self.rect = self.image.get_rect()
		self.x = 0
		self.y = 0
		self.gravity = 9.8

	def move(self, x, y):
		self.x += x
		self.y += y

	def update(self):
		self.rect.x += self.x
		self.rect.y += self.y + self.gravity



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