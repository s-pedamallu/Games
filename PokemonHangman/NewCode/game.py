from commonvariables import *
import pygame
import random
import gamegraphics
import sys

class BackgroundProperties:
	def __init__(self, bg):
		self.img = bg
		self.img.set_alpha(50)

class PokemonImageProperties:
	def __init__(self, color, hidden):
		self.exposed_img = color
		self.hidden_img = hidden
		self.hidden_img.set_colorkey((150,150,150))
		self.loc = (40,30)
		self.exposed = False

class NameDisplayProperties:
	def __init__(self, name):
		self.actual_word = name
		self.display_word = ""
		for i in range(len(name)):
			self.display_word+='?'
		self.loc = (40,45)
		self.color = game_colors['blue']
		self.size = 60

class AttemptedLettersProperties:
	def __init__(self):
		self.label = "You've already Tried"
		self.value = ""
		self.label_loc = (40,70)
		self.value_loc = (40,75)
		self.size = 35
		self.label_color = game_colors['pink']
		self.value_color = game_colors['green']

class TitleProperties:
	def __init__(self):
		self.text = "Who's that Pokemon?"
		self.loc = (20,10)
		self.color = game_colors['red']
		self.size = 60

class GameScreen:	
	def __init__(self, properties):	
		display_properties = properties
		self.bg_properties = BackgroundProperties(properties.bg)
		self.pokemon_image_properties = PokemonImageProperties(properties.pokemon_image, properties.hidden_image)
		self.pokemon_name_properties = NameDisplayProperties(properties.pokemon_name)
		self.attempted_letter_properties = AttemptedLettersProperties()
		self.canvas = pygame.display.set_mode(SCREEN_SIZE,pygame.FULLSCREEN)
		self.graphics = gamegraphics.GraphicsManager()
		self.lives = 5

	def show_game_screen(self):
		self.show_background()
		self.show_title()
		self.show_pokemon_image()
		self.show_pokemon_name()
		self.show_letters_tried()
		#show_hangman_image()
		#show_hints()
		#show_score()		
	
	def show_background(self):
		self.canvas.fill((255,255,255))
		self.canvas.blit(self.bg_properties.img,self.bg_properties.img.get_rect())

	def show_title(self):	
		title = TitleProperties()
		self.graphics.display_text(self.canvas,title.text,title.loc,title.size,title.color)

	def show_pokemon_image(self):
		if self.pokemon_image_properties.exposed:
			self.graphics.display_image(self.canvas, self.pokemon_image_properties.exposed_img, self.pokemon_image_properties.loc)
		else:
			self.graphics.display_image(self.canvas, self.pokemon_image_properties.hidden_img, self.pokemon_image_properties.loc)

	def show_pokemon_name(self):
		self.graphics.display_text(self.canvas, self.pokemon_name_properties.display_word, self.pokemon_name_properties.loc, 
			self.pokemon_name_properties.size, self.pokemon_name_properties.color)

	def show_letters_tried(self):
		self.graphics.display_text(self.canvas, self.attempted_letter_properties.label, self.attempted_letter_properties.label_loc, 
			self.attempted_letter_properties.size, self.attempted_letter_properties.label_color)
		self.graphics.display_text(self.canvas, self.attempted_letter_properties.value, self.attempted_letter_properties.value_loc, 
			self.attempted_letter_properties.size, self.attempted_letter_properties.value_color)

	def play_on_game_screen(self):
		is_done = False
		clock = pygame.time.Clock()
		while not is_done:
			self.show_game_screen()
			pygame.display.update()
			for event in pygame.event.get():				
				if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
					return 0
#				elif self.done and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
#					self.running = False
#					self.start_game()
				elif (not is_done) and (event.type == pygame.KEYDOWN):					
					is_done = self.evaluate_key_press(event.key)
			clock.tick(100)
		return 2

	def evaluate_key_press(self, key):
		# check if the key pressed is a valid alphabet between A-Z
		if not ((key>96 and key<123) or key==39):
			return False

		# check if the key was already used
		elif (str(unichr(key)) in self.attempted_letter_properties.value.lower()):
			return False

		# add the current pressed key into attempted letters
		self.attempted_letter_properties.value += str(unichr(key))
		self.attempted_letter_properties.value = self.attempted_letter_properties.value.upper()

		# for every charachter of the actual word check if it matches the current pressed key
		for i in range(len(self.pokemon_name_properties.actual_word)):			
			pykey = ord(self.pokemon_name_properties.actual_word.lower()[i])			
			if (key == pykey):
				# if it does, expose those characters from the actual word
				self.pokemon_name_properties.display_word = (self.pokemon_name_properties.display_word[:i]+
					self.pokemon_name_properties.actual_word[i]+self.pokemon_name_properties.display_word[(i+1):])
				self.pokemon_name_properties.display_word = self.pokemon_name_properties.display_word.upper()
				if self.pokemon_name_properties.actual_word == self.pokemon_name_properties.display_word:
					return True
		return False