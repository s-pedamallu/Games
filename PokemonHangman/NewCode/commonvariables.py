import pygame

background_image = pygame.image.load("./game_images/background3.jpg")
SCREEN_SIZE = background_image.get_size()
game_modes = ['Trainer','Challenger','Master']
game_font_name = "Pokemon Solid Normal,Tempus Sans ITC"
game_colors = {'yellow':pygame.Color(255,255,0), 'green':pygame.Color(0,102,0),'orange':pygame.Color(255,102,0),'red':pygame.Color(204,0,0)}