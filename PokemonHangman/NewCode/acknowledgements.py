from commonvariables import *
import pygame
import gamegraphics

class ScoreDisplayProperties:
	def __init__(self, score):
		self.value = str(score)
		self.label = "Final Score"
		self.label_loc = (40,5)
		self.label_size = 48
		self.label_color = game_colors['white']
		self.value_loc = (45,13)
		self.value_size = 60
		self.value_color = game_colors['yellow']

class AcknowledgementProperties:
	def __init__(self):
		self.label = "Acknowledgements"
		self.values = ["Inspired by the course: 'An Introduction to Interactive Programming in Python'",
						"By","Scott Rixner","Joe Warren","John Greiner","from Rice University"]
		self.label_loc = (43,40)
		self.label_size = 18
		self.label_color = game_colors['white']
		self.value_loc = [(15,44),(35,47),(40,47),(40,50),(40,53),(35,56)]
		self.value_size = 18
		self.value_color = game_colors['yellow']


class DoneByProperties:
	def __init__(self):
		self.label = "Developed By"
		self.value = "SHASHANK PEDAMALLU"
		self.label_loc = (45,90)
		self.label_size = 18
		self.label_color = game_colors['white']
		self.value_loc = (37,93)
		self.value_size = 32
		self.value_color = game_colors['yellow']

class GameOver:
	def __init__(self, score):
		self.score_properties = ScoreDisplayProperties(score)
		self.publish_developer_properties = DoneByProperties()
		self.acknowledgement_properties = AcknowledgementProperties()
		self.canvas = pygame.display.set_mode(SCREEN_SIZE,pygame.FULLSCREEN)
		self.graphics = gamegraphics.GraphicsManager()

	def show(self):
		self.canvas.fill((0,0,0))
		self.show_score()
		self.show_developer()
		self.show_acknowledgements()
		pygame.display.update()
		clock = pygame.time.Clock()
		while True:			
			for event in pygame.event.get():
				if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
						return
			clock.tick(60)			

	def show_score(self):
		self.graphics.display_text(self.canvas, self.score_properties.label, self.score_properties.label_loc,
			self.score_properties.label_size, self.score_properties.label_color)
		self.graphics.display_text(self.canvas, self.score_properties.value, self.score_properties.value_loc,
			self.score_properties.value_size, self.score_properties.value_color)

	def show_developer(self):
		self.graphics.display_text(self.canvas, self.publish_developer_properties.label, self.publish_developer_properties.label_loc,
			self.publish_developer_properties.label_size, self.publish_developer_properties.label_color)
		self.graphics.display_text(self.canvas, self.publish_developer_properties.value, self.publish_developer_properties.value_loc,
			self.publish_developer_properties.value_size, self.publish_developer_properties.value_color)

	def show_acknowledgements(self):
		self.graphics.display_text(self.canvas, self.acknowledgement_properties.label, self.acknowledgement_properties.label_loc,
			self.acknowledgement_properties.label_size, self.acknowledgement_properties.label_color)		
		for i in range(len(self.acknowledgement_properties.values)):
			self.graphics.display_text(self.canvas, self.acknowledgement_properties.values[i], self.acknowledgement_properties.value_loc[i],
				self.acknowledgement_properties.value_size, self.acknowledgement_properties.value_color)