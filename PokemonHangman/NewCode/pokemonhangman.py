import welcome
import pygame
import levelshandler

class GameDriver:
	def run(self):
		pygame.init()
		home = welcome.WelcomeScreen()
		mode = home.get_mode()
		game_play = levelshandler.LevelManager(mode)		
		game_play.start_levels()


manager = GameDriver()
manager.run()