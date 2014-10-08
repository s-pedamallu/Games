from commonvariables import *
import gamegraphics
import pygame
import sys

class TitleProperties:
	def __init__(self):
		self.text = "Pokemon Hangman"
		self.loc = (27,10)
		self.color = game_colors['yellow']
		self.size = 60

class BackgroundProperties:
	def __init__(self):
		self.img = pygame.image.load("./game_images/background3.jpg")
		self.transperancy = 100

class ModeProperties:
	def __init__(self):
		self.texts = game_modes
		self.locs = [(15,40),(15,50),(15,60)]
		self.boundaries = [(14,40),(28,45),(14,49),(32,56),(14,60),(28,65)]
		self.colors = [game_colors['green'],game_colors['orange'],game_colors['red']]
		self.size = 35

class WelcomeScreen:
	def __init__(self):
		self.canvas = pygame.display.set_mode(SCREEN_SIZE,pygame.FULLSCREEN)
		self.graphics = gamegraphics.GraphicsManager()

	def show_welcome_screen(self):
		self.show_background()
		self.show_title()
		self.show_modes()
		pygame.display.update()

	def show_background(self):
		bg = BackgroundProperties()		
		bg.img.set_alpha(bg.transperancy)
		self.canvas.fill((0,0,0))
		self.canvas.blit(bg.img,bg.img.get_rect())		

	def show_modes(self):
		modes = ModeProperties()
		for index in range(len(modes.texts)):
			self.graphics.display_text(self.canvas,modes.texts[index],modes.locs[index],modes.size,modes.colors[index])

	def show_title(self):
		title = TitleProperties()
		self.graphics.display_text(self.canvas,title.text,title.loc,title.size,title.color)

	def get_mode(self):
		ans = 0
		clock = pygame.time.Clock()
		self.show_welcome_screen()
		is_running = True		
		while is_running:			
			for event in pygame.event.get():
				if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
						is_running = False
						sys.exit(0)
				elif event.type == pygame.MOUSEBUTTONDOWN:					
					modes = ModeProperties()
					for i in range(0,5,2):
						if self.graphics.is_clicked_inside(event.pos, modes.boundaries[i],modes.boundaries[i+1]):
							is_running = False
							ans = i/2
							break
			clock.tick(60)
		print "Selected",ModeProperties().texts[ans]
		return ans