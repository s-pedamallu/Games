from commonvariables import *
import pygame
import random
import gamegraphics
import finish

class BackgroundProperties:
	def __init__(self, bg):
		self.img = bg
		self.img.set_alpha(50)

class PokemonImageProperties:
	def __init__(self, color_img, hidden):
		original_size = color_img.get_size()
		scale = 2
		self.exposed_img = pygame.transform.scale(color_img,(original_size[0]*scale,original_size[1]*3))
		self.hidden_img = pygame.transform.scale(hidden,(original_size[0]*scale,original_size[1]*3))
		self.hidden_img.set_colorkey((150,150,150))
		self.loc = (30,30)
		self.exposed = False

class HangmanImageProperties:
	def __init__(self, lives):
		self.img = pygame.image.load('./game_images/hangman/'+str(lives)+'.bmp')
		self.img.set_colorkey((255,255,255))
		self.loc = (2,35)

class NameDisplayProperties:
	def __init__(self, details):
		self.actual_word = details.split()[2].upper()
		self.display_word = ""
		for i in range(len(self.actual_word)):
			self.display_word+='?'
		self.loc = (50,45)
		self.color = game_colors['blue']
		self.size = 60

class AttemptedLettersProperties:
	def __init__(self):
		self.label = "You've already Tried"
		self.value = ""
		self.label_loc = (50,55)
		self.value_loc = (50,60)
		self.size = 30
		self.label_color = game_colors['pink']
		self.value_color = game_colors['green']

class ScoreProperties:
	def __init__(self,score):
		self.label = "Score:"
		self.value = str(score)
		self.label_loc = (2,95)
		self.label_color = game_colors['black']
		self.value_loc = (10,95)
		self.value_color = game_colors['yellow']
		self.size = 25

class TitleProperties:
	def __init__(self):
		self.text = "Who's that Pokemon?"
		self.loc = (20,10)
		self.color = game_colors['red']
		self.size = 60

class ForwardProperties:
	def __init__(self, bg, pokemon_image, pokemon_details):
		self.pokemon_img = pokemon_image
		self.bg_img = bg
		# The third word is the Pokemon Name
		self.name = pokemon_details.split()[2].upper()
		self.types = pokemon_details.split()[4:]

class ReturnValueProperties:
	def __init__(self, before_score):
		self.score = before_score
		self.pass_status = 0

class HintProperties:
	def __init__(self, h):
		self.text = "Get Hint"
		self.text_boundary = [(35,65),(45,69)]
		self.label = "Hints available:"
		self.value = h
		self.is_used = False
		self.text_loc = (35,65)
		self.label_loc = (70,95)
		self. value_loc = (93,95)
		self.text_size = 25
		self.label_size = 30
		self. text_color = game_colors['orange']
		self.label_color = game_colors['black']
		self.value_color = game_colors['yellow']

class GameScreen:	
	def __init__(self, properties):	
		display_properties = properties
		self.bg_properties = BackgroundProperties(properties.bg)
		self.pokemon_image_properties = PokemonImageProperties(properties.pokemon_image, properties.hidden_image)
		self.pokemon_name_properties = NameDisplayProperties(properties.pokemon_details)
		self.attempted_letter_properties = AttemptedLettersProperties()
		self.hint_properties = HintProperties(properties.hints)
		self.return_value = ReturnValueProperties(properties.current_score)
		self.score_properties = ScoreProperties(properties.current_score)
		self.canvas = pygame.display.set_mode(SCREEN_SIZE,pygame.FULLSCREEN)
		self.graphics = gamegraphics.GraphicsManager()
		forward_properties = ForwardProperties(properties.bg, properties.pokemon_image, properties.pokemon_details)
		self.finish_screen = finish.FinishScreen(forward_properties)
		self.lives = 5
		self.score = 0
		self.hangman_image_properties = HangmanImageProperties(self.lives)		

	def show_game_screen(self):
		self.show_background()
		self.show_title()
		self.show_pokemon_image()
		self.show_pokemon_name()
		self.show_letters_tried()
		self.show_hints()
		self.show_hangman_image()
		self.show_score()
		
	
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

	def show_hangman_image(self):
		self.graphics.display_image(self.canvas, self.hangman_image_properties.img, self.hangman_image_properties.loc)		

	def show_pokemon_name(self):
		self.graphics.display_text(self.canvas, self.pokemon_name_properties.display_word, self.pokemon_name_properties.loc, 
			self.pokemon_name_properties.size, self.pokemon_name_properties.color)

	def show_letters_tried(self):
		self.graphics.display_text(self.canvas, self.attempted_letter_properties.label, self.attempted_letter_properties.label_loc, 
			self.attempted_letter_properties.size, self.attempted_letter_properties.label_color)
		self.graphics.display_text(self.canvas, self.attempted_letter_properties.value, self.attempted_letter_properties.value_loc, 
			self.attempted_letter_properties.size, self.attempted_letter_properties.value_color)

	def show_hints(self):
		if (self.hint_properties.value > 0 and not self.hint_properties.is_used):
			self.graphics.display_text(self.canvas, self.hint_properties.text, self.hint_properties.text_loc, 
				self.hint_properties.text_size, self.hint_properties.text_color)
		self.graphics.display_text(self.canvas, self.hint_properties.label, self.hint_properties.label_loc, 
			self.hint_properties.label_size, self.hint_properties.label_color)
		self.graphics.display_text(self.canvas, str(self.hint_properties.value), self.hint_properties.value_loc,
			self.hint_properties.label_size, self.hint_properties.value_color)

	def show_score(self):
		self.graphics.display_text(self.canvas, self.score_properties.label, self.score_properties.label_loc,
			self.score_properties.size, self.score_properties.label_color)
		self.graphics.display_text(self.canvas, self.score_properties.value, self.score_properties.value_loc,
			self.score_properties.size, self.score_properties.value_color)

	def play_on_game_screen(self):		
		clock = pygame.time.Clock()		
		is_done = False
		while not is_done and self.lives>=0:
			self.show_game_screen()
			pygame.display.update()
			for event in pygame.event.get():				
				if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
					self.return_value.pass_status = 0
					is_done = True
				elif event.type == pygame.KEYDOWN:					
					self.return_value.pass_status = self.evaluate_key_press(event.key)
					if self.return_value.pass_status == 2:
						is_done = True
				elif (event.type == pygame.MOUSEBUTTONDOWN and not self.hint_properties.is_used):
					self.return_value.pass_status = self.evaluate_mouse_click(event.pos)					
			clock.tick(100)
		self.return_value.pass_status = self.finish_screen.reveal(self.return_value.pass_status)
		return self.return_value

	def evaluate_mouse_click(self, pos):
		if (self.graphics.is_clicked_inside(pos, self.hint_properties.text_boundary[0],
						self.hint_properties.text_boundary[1])):
			self.pokemon_image_properties.exposed = True
			self.hint_properties.is_used = True
			self.hint_properties.value -= 1
			self.score-=10
			return 1

	def evaluate_key_press(self, key):
		# ignore if the key pressed is NOT a valid alphabet between A-Z or ' or .
		if not ((key>96 and key<123) or key==39 or key==46):
			return 0

		# ignore if the key was already used
		elif (str(unichr(key)) in self.attempted_letter_properties.value.lower()):
			return 0

		# add the current pressed key into attempted letters
		self.attempted_letter_properties.value += str(unichr(key))
		self.attempted_letter_properties.value = self.attempted_letter_properties.value.upper()

		has_changed = False
		# for every charachter of the actual word check if it matches the current pressed key
		for i in range(len(self.pokemon_name_properties.actual_word)):			
			pykey = ord(self.pokemon_name_properties.actual_word.lower()[i])			
			if (key == pykey):
				# if it does, expose those characters from the actual word
				has_changed = True				
				self.pokemon_name_properties.display_word = (self.pokemon_name_properties.display_word[:i]+
					self.pokemon_name_properties.actual_word[i]+self.pokemon_name_properties.display_word[(i+1):])
				self.pokemon_name_properties.display_word = self.pokemon_name_properties.display_word.upper()
				if self.pokemon_name_properties.actual_word == self.pokemon_name_properties.display_word:
					self.score+=20
					self.return_value.score+=self.score
					return 2
		if not has_changed:
			self.lives-=1
			self.score-=1
			if self.lives > 0:
				self.hangman_image_properties = HangmanImageProperties(self.lives)
		return 0