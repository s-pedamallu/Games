import random
import pygame
import os
import sys

class GameConstants:
	def __init__(self,gm):		
		if gm<0 or gm>2:
			gm = 1		
		if gm == 0:
			self.hints = float('inf')
		elif gm == 1:
			self.hints = 3
		else:
			self.hints = 0

	def get_hints(self):
		return self.hints		

class GameColors:
	def __init__(self):
		self.RED = pygame.Color(204,0,0)
		self.BLACK = pygame.Color(0,0,0)
		self.WHITE = pygame.Color(255,255,255)
		self.ORANGE = pygame.Color(255,102,0)
		self.PINK = pygame.Color(255,0,102)
		self.VIOLET = pygame.Color(102,0,102)
		self.BLUE = pygame.Color(51,0,204)
		self.YELLOW = pygame.Color(255,255,0)
		self.GREEN = pygame.Color(0,102,0)		
		self.palette = {1:self.RED,2:self.BLACK,3:self.WHITE,4:self.ORANGE,
						5:self.PINK,6:self.VIOLET,7:self.BLUE,8:self.YELLOW,
						9:self.GREEN}

	def get_color(self,key):		
		return	self.palette[key]							

class GameManager:
	def __init__(self):
		pygame.init()
		#canvas = pygame.display.set_mode((1024,768),pygame.FULLSCREEN)
		pygame.display.set_caption("Pokemon Hangman")
		self.modes = ('TRAINER', 'CHALLENGER', 'MASTER')		
		self.game_constants = None	
		self.running = True
		start = False
		self.game_colors = GameColors()
		clock = pygame.time.Clock()

		# Setting background properties
		self.bg = pygame.image.load("../game_images/background3.jpg")
		self.bg_size = self.bg.get_size()
		self.bg_rect = self.bg.get_rect()
		self.bg.set_alpha(100)
		self.screen = pygame.display.set_mode(self.bg_size,pygame.FULLSCREEN)

		self.welcome_sound = pygame.mixer.Sound("../audio_clips/poke-who.wav")
		self.build_header("Pokemon Hangman")

		self.refresh_background()
		while self.running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
					self.running = False
					sys.exit(0)
				elif event.type == pygame.MOUSEBUTTONDOWN:					
					self.mouse_handler(event.pos)
					if (self.game_constants != None):
						self.running = False
						start = True
						self.hints = self.game_constants.get_hints()
			self.choose_mode()
			clock.tick(60)
		if start:
			self.score = 0		
			self.start_game()

	# Draw available modes
	def choose_mode(self):
		font_obj = pygame.font.Font(pygame.font.match_font('TempusSansITC'),48)
		
		#canvas.fill(self.game_colors.BACKGROUND)
		#self.screen.fill((0,0,0))
		#self.screen.blit(self.bg, self.bg_rect)
		#pygame.display.update()
		
		mode1 = font_obj.render(self.modes[0],True,self.game_colors.get_color(9))
		mode2 = font_obj.render(self.modes[1],True,self.game_colors.get_color(4))
		mode3 = font_obj.render(self.modes[2],True,self.game_colors.get_color(1))	

		self.display_header()

		self.screen.blit(mode1,(480-(len(self.modes[0])/2),324))
		self.screen.blit(mode2,(480-(len(self.modes[1])/2),384))
		self.screen.blit(mode3,(480-(len(self.modes[2])/2),444))
		pygame.display.update()

	# Draw Heading
	def display_header(self):
		font_obj_heading = pygame.font.Font(pygame.font.match_font('Jokerman'),72)
		for i in range(0,len(self.heading)):
			x = 200 +(i*40)	#(300 - (len(self.heading)/2))+(i*40)
			self.screen.blit(font_obj_heading.render(self.heading[i],True,self.heading_colors[i]),(x,50))

	def mouse_handler(self, pos):
		if ((pos[0]>=455 and pos[0]<=663) and (pos[1]>319 and pos[1]<376)):
			self.game_constants = GameConstants(0)			
		elif ((pos[0]>=455 and pos[0]<=761) and (pos[1]>385 and pos[1]<435)):
			self.game_constants = GameConstants(1)
		elif ((pos[0]>=455 and pos[0]<=656) and (pos[1]>448 and pos[1]<492)):
			self.game_constants = GameConstants(2)

	def build_header(self, header):
		self.heading = []
		self.heading_colors = []
		for i in range(0,len(header)):
			color = GameColors()
			self.heading.append(header[i])
			self.heading_colors.append(color.get_color(random.randint(1,9)))

	def display_word(self, word, pos, font, color, size):
		pokemon_font = pygame.font.Font(pygame.font.match_font(font),size)
		self.screen.blit(pokemon_font.render(word,True,color),pos)

	def start_game(self):
		self.chances = 5
		self.build_header("Who's that Pokemon?")
		self.welcome_sound.play()
		self.get_pokemon()
		self.hangman = pygame.image.load(os.path.join('../game_images/hangman',str(self.chances)+'.bmp'))
		self.done = False
		self.expose = False
		self.tried = ''
		self.show_game()
		self.build_header("Game Over")
		self.show_game_over()

	def get_pokemon(self):
		data_file = open('../data/clean_data.dat','r')
		for i in range(random.randint(0,648)):
			data_file.readline()
		line = data_file.readline()
		details = line.split()
		self.img_file = pygame.image.load(os.path.join('../game_images/pokemon',str(int(details[0]))+'.png'))
		self.hidden_img = pygame.image.load(os.path.join('../game_images/hidden_pokemon',str(int(details[0]))+'.png'))
		self.hidden_img.set_colorkey((150,150,150))
		self.pokemon = details[1]
		data_file.close()
		self.current_word = ""
		self.pokemon_color = self.game_colors.get_color(random.randint(1,9))
		for i in range(len(self.pokemon)):
			self.current_word += "?"
		self.pokemon = self.pokemon.lower()			

	def show_game(self):
		self.running = True
		clock = pygame.time.Clock()		
		self.refresh_background()
		while self.running:
			#canvas.fill(self.game_colors.BACKGROUND)			
			self.display_header()
			self.hangman.set_colorkey((255,255,255))
			self.display_word(self.current_word,(400,450),'Chiller',self.pokemon_color,60)
			self.display_word('Hints Available:',(50,700),'Arial',self.game_colors.BLACK,32)
			self.display_word(str(self.hints),(250,700),'Arial',self.game_colors.ORANGE,32)
			self.display_word('Score:',(800,700),'Arial',self.game_colors.BLACK,32)
			self.display_word('Letters tried so far: ',(400,250),'TempusSansITC',self.game_colors.BLACK,24)
			self.display_word(self.tried,(400,280),'TempusSansITC',self.game_colors.BLUE,24)
			
			if not (self.done or self.expose):
				self.screen.blit(self.hidden_img,(400,350))
				self.display_word('Get Hint',(425,550),'TempusSansITC',self.game_colors.GREEN,24)
			else:				
				self.screen.blit(self.img_file,(400,350))	

			self.screen.blit(self.hangman,(50,250))			

			for event in pygame.event.get():				
				if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
					self.running = False					
				elif self.done and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
					self.running = False
					self.start_game()
				elif (not self.done) and (event.type == pygame.KEYDOWN):
					self.refresh_background()
					self.done = self.key_pressed(event.key)
				elif (not (self.done or self.expose)) and event.type == pygame.MOUSEBUTTONDOWN:
					self.hint_handler(event.pos)

			self.display_word(str(self.score),(900,700),'Arial',self.game_colors.GREEN,32)			
			if self.done:
				self.display_word('Press space to continue', (350,550),'TempusSansITC',self.game_colors.ORANGE,24)						

			pygame.display.update()

			if self.chances<=0:
				self.running = False
			clock.tick(100)
		self.running = True
		
	def key_pressed(self,key):
		flag = True
		for i in range(0,len(self.current_word)):
			pykey = ord(self.pokemon[i])
			if (key == pykey):
				self.current_word = self.current_word[:i]+self.pokemon[i]+self.current_word[(i+1):]
				self.current_word = self.current_word.upper()
				if (not str(unichr(key)) in self.tried):
					self.tried += str(unichr(key))
				flag = False
				if self.current_word == self.pokemon.upper():
					self.score += (10 + (self.chances)*2)
					return True
		if flag and ((key>96 and key<123) or key==39) and (not str(unichr(key)) in self.tried):
			self.chances -= 1
			self.hangman = pygame.image.load(os.path.join('../game_images/hangman',str(self.chances)+'.bmp'))
			if (not str(unichr(key)) in self.tried):
					self.tried += str(unichr(key))
		return False

	def show_game_over(self):
		enter_count = 0
		restart = False
		clock = pygame.time.Clock()
		self.refresh_background()
		while self.running:			
			self.display_header()
			self.hangman.set_colorkey((255,255,255))
			if enter_count == 0:
				self.screen.blit(self.img_file,(400,350))
				self.display_word(self.pokemon.upper(),(400,450),'Chiller',self.pokemon_color,60)
				self.display_word("Press Esc to Quit / Press Enter to view final score",(300,700),'TempusSansITC',self.game_colors.GREEN,24)
			else:
				self.display_word("Final Score",(400,250),'ComicSansMS',self.game_colors.RED,36)
				self.display_word(str(self.score),(400,300),'ComicSansMS',self.game_colors.RED,36)
				self.display_word("Press Esc to Quit / Press Enter to Restart",(300,700),'TempusSansITC',self.game_colors.GREEN,24)
			self.screen.blit(self.hangman,(50,250))

			for event in pygame.event.get():
				if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
					self.running = False
					sys.exit(0)
				elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
					self.refresh_background()
					enter_count+=1
					if enter_count>1:
						self.running = False
						restart = True

			pygame.display.update()

		if restart:
			GameManager()

	def hint_handler(self,pos):		 
		if (pos[0] > 415 and pos[0] < 515) and (pos[1] > 550 and pos[1] < 580):
			if self.hints > 0:				
				self.expose = True
				self.hints -= 1
				self.score -= 10
				self.refresh_background()

	def refresh_background(self):
		self.screen.fill((0,0,0))
		self.screen.blit(self.bg,self.bg_rect)
		pygame.display.update()

GameManager()
