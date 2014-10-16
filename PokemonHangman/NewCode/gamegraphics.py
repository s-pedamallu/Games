from commonvariables import *
import pygame
import commonvariables

class GraphicsManager:
	def display_text(self, canvas, text, rel_loc, size, color):
		abs_loc = self.get_absolute_location(rel_loc)
		pygame.font.init()
		game_font = pygame.font.SysFont(game_font_name,size)
		canvas.blit(game_font.render(text,True,color),abs_loc)

	def get_absolute_location(self, relative_location):
		x = SCREEN_SIZE[0]*((relative_location[0]*1.0)/100)
		y = SCREEN_SIZE[1]*((relative_location[1]*1.0)/100)
		return (x,y)

	def get_relative_location(self, absolute_location):
		x = ((absolute_location[0]*1.0) / SCREEN_SIZE[0])*100
		y = ((absolute_location[1]*1.0) / SCREEN_SIZE[1])*100
		return (x,y)

	def is_clicked_inside(self, abs_clicked_at, rel_top_left, rel_bottom_right):
		rel_clicked_at = self.get_relative_location(abs_clicked_at)	
		return ((rel_clicked_at[0] > rel_top_left[0] and rel_clicked_at[0] < rel_bottom_right[0])
			and (rel_clicked_at[1] > rel_top_left[1] and rel_clicked_at[1] < rel_bottom_right[1]))

	def display_image(self, canvas, img, relative_location):
		abs_location = self.get_absolute_location(relative_location)
		canvas.blit(img,abs_location)