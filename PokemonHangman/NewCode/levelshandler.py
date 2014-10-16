from commonvariables import *
import pygame
import gamegraphics
import random
import gamehandler

class LevelDisplayPropertties:
	def __init__(self, l, name):
		self.level = 'Level '+str(l)
		self.loc = (40,7)
		self.size = 60
		self.color = game_colors['green']
		self.level_name = name
		self.name_loc = (43,88)		

class LevelProperties:
	def __init__(self, data, h, img, m, score):
		self.bg = img		
		self.pokelist = data
		self.hints = h
		self.mode = m
		self.total_score = score
		random.shuffle(self.pokelist)

class LevelManager:
	def __init__(self, m):
		self.levels = {1:'Kanto',2:'Johto',3:'Hoenn',4:'Sinnoh',5:'Unova'}
		self.mode = m
		self.hints = self.build_hints()
		self.score = 0

	def build_hints(self):
		if self.mode==0:
			return float('inf')
		elif self.mode==1:
			return 10
		else:
			return 0

	def start_levels(self):
		is_running = True
		level = 1
		while is_running and level<=5:
			self.show_level(level)
			data = self.get_data_from_file(level)
			level_properties = LevelProperties(data,self.hints, self.get_level_image(level), self.mode, self.score)	
			core_game = gamehandler.GameManager(level_properties)
			reply = core_game.play_level()
			self.score = reply.current_score
			is_running = reply.proceed_forward
			level+=1
		return self.score

	def show_level(self,l):
		prop = LevelDisplayPropertties(l,self.levels[l])
		bg = self.get_level_image(l)
		graphics = gamegraphics.GraphicsManager()
		canvas = pygame.display.set_mode(SCREEN_SIZE,pygame.FULLSCREEN)
		canvas.fill((0,0,0))
		canvas.blit(bg,bg.get_rect())
		graphics.display_text(canvas,prop.level,prop.loc,prop.size,prop.color)
		graphics.display_text(canvas,prop.level_name, prop.name_loc, prop.size, prop.color)
		pygame.display.update()
		pygame.time.delay(2000)	

	def get_data_from_file(self, l):		
		with open('./data/'+self.levels[l]+'.dat') as poke_file:
			data = poke_file.read().splitlines()
		return data

	def get_level_image(self, l):
		return pygame.image.load('./game_images/background/'+self.levels[l]+'.jpg')