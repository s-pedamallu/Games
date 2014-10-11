from commonvariables import *
import pygame
import gamegraphics
import random


class LevelDisplayPropertties:
	def __init__(self, l, name):
		self.level = 'Level '+str(l)
		self.loc = (40,7)
		self.size = 60
		self.color = game_colors['green']
		self.level_name = name
		self.name_loc = (43,88)

class LevelProperties:
	def __init__(self, data, h, img):
		self.bg = img
		self.transperancy = 50
		self.pokelist = data
		self.hints = h
		random.shuffle(self.pokelist)

class LevelManager:
	def __init__(self, mode):
		self.levels={1:'Kanto',2:'Johto',3:'Hoenn',4:'Sinnoh',5:'Unova'}
		if mode==0:
			self.hints = float('inf')
		elif mode==1:
			self.hints = 10
		else:
			self.hints = 0

	def start_levels(self):
		is_running = True
		level = 1
		while is_running and level<=5:
			self.show_level(level)
			data = self.get_data_from_file(level)
			level_properties = LevelProperties(data,self.hints)	
			core_game = gameshandler.GameManager(level_properties)
			if core_game.play_level()==False:
				is_running = False
			level+=1

	def show_level(self,l):
		prop = LevelDisplayPropertties(l,self.levels[l])
		bg = get_level_image(l)
		graphics = gamegraphics.GraphicsManager()
		canvas = pygame.display.set_mode(SCREEN_SIZE,pygame.FULLSCREEN)
		canvas.fill((0,0,0))
		canvas.blit(bg,bg.get_rect())
		graphics.display_text(canvas,prop.level,prop.loc,prop.size,prop.color)
		graphics.display_text(canvas,prop.level_name, prop.name_loc, prop.size, prop.color)
		pygame.display.update()
		pygame.time.delay(2500)	

	def get_data_from_file(self, l):		
		with open('./data/'+self.levels[l]+'.dat') as poke_file:
			data = poke_file.read().splitlines()
		return data

	def get_level_image(self, l):
		return pygame.image.load('./game_images/background/'+self.levels[l]+'.jpg')