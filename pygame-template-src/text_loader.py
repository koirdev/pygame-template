import pygame
from config import *

pygame.init()

# Fonts
menu_font = pygame.font.Font('assets/fonts/42dotSans-Bold.ttf', 35)
main_font = pygame.font.Font('assets/fonts/opensans.ttf', 35)

# Text
MainMenuText = main_font.render("Main Menu - " + VERSION, False, (252,250,250))
FirstSceneText = main_font.render("First Scene (Press BACKSPACE to return to the main menu)", False, (252,250,250))
SecondSceneText = main_font.render("Second Scene (Press BACKSPACE to return to the main menu)",False, (252,250,250))
