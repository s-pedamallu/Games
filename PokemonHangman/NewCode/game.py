from commonvariables import *
import pygame
import random

class TitleProperties:
	def __init__(self):
		self.text = "Who's that Pokemon?"
		self.loc = (20,10)
		self.color = game_colors['red']
		self.size = 60

class GameScreen:	
	def initialize(self):
		with open('./data/Kanto.dat','r') as source_file:
			self.pokemon_list = source_file.readlines()
		random.shuffle(self.pokemon_list)

	def game_screen(self):
		show_title()
		show_pokemon_image()
		show_pokemon_name()
		show_letters_tried()
		show_hangman_image()
		show_score()		
		
	def show_title(self):	
		title = TitleProperties()
		self.graphics.display_text(self.canvas,title.text,title.loc,title.size,title.color)