import welcome
import game
import finish
import pygame

class GameDriver:
	def run(self):
		pygame.init()
		home = welcome.WelcomeScreen()
		mode = home.get_mode()

manager = GameDriver()
manager.run()