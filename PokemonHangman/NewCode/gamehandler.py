from commonvariables import *
import pygame
import game

class GameStatus:
    def __init__(self, score, is_level_finished):
        self.current_score = score
        self.proceed_forward = is_level_finished

class GameProperties:
    def __init__(self, lp, pokemon_details, pokemon_img, hidden_img, hints, score):
        self.bg = lp.bg
        self.pokemon_details = pokemon_details
        self.current_score = lp.total_score
        self.pokemon_image = pokemon_img
        self.hidden_image = hidden_img
        self.hints = hints
        self.current_score = score

class GameManager:
    def __init__(self, lp):
        self.level_properties = lp

    """
    1. Keep track of the score, hints used, progress made in the level, etc
    2. Iterate for every pokemon of the level py passing control to game.py
    """
    def play_level(self):
        hints_available = self.level_properties.hints
        score = self.level_properties.total_score
        is_game_ended = False
        idx = 0
        while idx < len(self.level_properties.pokelist) and not is_game_ended:
            pokemon_details = self.level_properties.pokelist[idx]            
            img_number = int(pokemon_details.split()[1][1:])
            pokemon_img = self.get_pokemon_image(img_number, False)
            hidden_img = self.get_pokemon_image(img_number, True)
            game_props = GameProperties(self.level_properties, pokemon_details, pokemon_img, hidden_img, hints_available, score)
            game_screen = game.GameScreen(game_props)
            game_response = game_screen.play_on_game_screen()
            hints_available = game_response.remaining_hints
            score = game_response.score
            is_game_ended = game_response.pass_status == 0
            idx += 1
        return GameStatus(score, not is_game_ended)

    def get_pokemon_image(self, image_number, get_hidden):
        if get_hidden:
            return pygame.image.load('./game_images/hidden_pokemon/'+str(image_number)+'.png')
        else:
            return pygame.image.load('./game_images/pokemon/'+str(image_number)+'.png')