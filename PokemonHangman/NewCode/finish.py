from commonvariables import *
import pygame
import gamegraphics
import sys

class BackgroundProperties:
	def __init__(self, img):
		self.bg = img
		self.bg.set_alpha(50)

class TitleProperties:
	def __init__(self):
		self.title = ['Better Luck Next Time!', 'You Nailed It!']
		self.loc = [(15,10),(30,10)]
		self.size = 60
		self.color = game_colors['red']

class ImageProperties:
	def __init__(self, pokemon_img):
		original_size = pokemon_img.get_size()
		scale = 2
		self.exposed_img = pygame.transform.scale(pokemon_img,(original_size[0]*scale,original_size[1]*3))
		self.loc = (30,30)

class PokemonProperties:
	def __init__(self, pokemonname, pokemon_type):
		self.name = pokemonname
		self.types = pokemon_type
		self.label = "Type(s)"
		self.name_loc = (50,45)
		self.label_loc = (50,55)
		self.label_color = game_colors['pink']
		self.name_color = game_colors['blue']
		self.type_color = game_colors['green']
		self.name_size = 60
		self.label_size = 30

class FooterProperties:
	def __init__(self):
		self.msg = "Press SPACE to continue"
		self.color = game_colors['black']
		self.size = 30
		self.loc = (35,95)

class FinishScreen:
	def __init__(self, properties):
		self.title_properties = TitleProperties()
		self.bg_properties = BackgroundProperties(properties.bg_img)
		self.image_properties = ImageProperties(properties.pokemon_img)
		self.pokemon_properties = PokemonProperties(properties.name, properties.types)
		self.footer_properties = FooterProperties()
		self.canvas = pygame.display.set_mode(SCREEN_SIZE,pygame.FULLSCREEN)
		self.graphics = gamegraphics.GraphicsManager()

	def reveal(self, status):
		self.show_background()
		self.show_title(status)
		self.show_image()
		self.show_pokemon_details()
		self.show_footer()
		pygame.display.update()
		is_running = True		
		while is_running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
					is_running = False
					status = 0
				elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
					is_running = False
		return status


	def show_background(self):
		self.canvas.fill((255,255,255))
		self.canvas.blit(self.bg_properties.bg,self.bg_properties.bg.get_rect())

	def show_title(self, status):	
		if status == 0:
			self.graphics.display_text(self.canvas,self.title_properties.title[0],self.title_properties.loc[0],
				self.title_properties.size,self.title_properties.color)
		else:
			self.graphics.display_text(self.canvas,self.title_properties.title[1],self.title_properties.loc[1],
				self.title_properties.size,self.title_properties.color)

	def show_image(self):
		self.graphics.display_image(self.canvas, self.image_properties.exposed_img, self.image_properties.loc)

	def show_pokemon_details(self):
		self.graphics.display_text(self.canvas, self.pokemon_properties.name, self.pokemon_properties.name_loc,
			self.pokemon_properties.name_size, self.pokemon_properties.name_color)
		self.graphics.display_text(self.canvas, self.pokemon_properties.label, self.pokemon_properties.label_loc,
			self.pokemon_properties.label_size, self.pokemon_properties.label_color)
		for i in range(len(self.pokemon_properties.types)):
			loc = (self.pokemon_properties.label_loc[0], self.pokemon_properties.label_loc[1]+((i+1)*6))
			self.graphics.display_text(self.canvas, self.pokemon_properties.types[i], loc,
				self.pokemon_properties.label_size, self.pokemon_properties.type_color)

	def show_footer(self):
		self.graphics.display_text(self.canvas, self.footer_properties.msg, self.footer_properties.loc,
			self.footer_properties.size, self.footer_properties.color)