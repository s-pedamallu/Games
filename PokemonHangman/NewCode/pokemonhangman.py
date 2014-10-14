import welcome
import pygame
import levelshandler
import acknowledgements

class GameDriver:
	def run(self):
		pygame.init()
		home = welcome.WelcomeScreen()
		mode = home.get_mode()
		game_play = levelshandler.LevelManager(mode)		
		final_score = game_play.start_levels()
		last_screen = acknowledgements.GameOver(final_score)
		last_screen.show()

manager = GameDriver()
manager.run()