from config import * 
from sound_loader import *
from image_loader import *
from text_loader import *
import pygame, sys

# Checking init error
game_init = pygame.init()
if(game_init[1]>0):
    print("Game initialization failed")

# Window options
if WINDOW_MODE == 2: # fullscreen
    window = pygame.display.set_mode((WIDTH,HEIGHT),pygame.FULLSCREEN + pygame.SCALED)
else:

    if WINDOW_MODE == 0: # default window
        window = pygame.display.set_mode((WIDTH, HEIGHT))
    else:

        if WINDOW_MODE == 1: # resizable window
            window = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

        else:
            if WINDOW_MODE == 3: # hardware render
                window = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN + pygame.HWSURFACE + pygame.SCALED)
            else:
                WindowModeError()
                exit()
                sys.exit()

# Window title and icon
pygame.display.set_caption("Your title")
icon = pygame.image.load('assets/images/icon.png')
pygame.display.set_icon(icon)
clock = pygame.time.Clock()

# Menu Sections
items = ['First scene','Second scene','Quit']

selected_section = 0

# Section colors
CYAN = (91, 207, 252)
DARK_CYAN = (38, 109, 135)


# Scene switcher
current_scene = None
def switch_scene(scene):
    global current_scene
    current_scene = scene

def MainMenu():
    global running, selected_section
    running = True
    while running:
        
        # Quit Event
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    exit()
                    sys.exit()


            # Menu Controls
                elif e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_UP:
                        selected_section -= 1
                    elif e.key == pygame.K_DOWN:
                        selected_section += 1
                    elif e.key in [pygame.K_RETURN, pygame.K_SPACE]:
             # Menu tabs
                        if items[selected_section] == 'Quit': running = False, pygame.quit(), exit()
                        if items[selected_section] == 'First scene': running = False, Scene1()
                        if items[selected_section] == 'Second scene': running = False, Scene2()
                    selected_section = selected_section % len(items)

       # 'Q' Key to quit
            if e.type == pygame.KEYUP:
                if e.key == pygame.K_q:
                    running = False
                    pygame.quit()
                    exit()
                    sys.exit()

        # Render objects
            window.fill((140, 140, 139))
            fps_text = menu_font.render("FPS: " + str(clock.get_fps()), True, (255,255,255))
            window.blit(fps_text, (0,50))
            window.blit(MainMenuText,(0,0))    

        # Render Menu
            for i in range(len(items)):
                if i == selected_section:
                    menu_text = menu_font.render(items[i],0, CYAN)
                else:
                    menu_text = menu_font.render(items[i],0, DARK_CYAN)
                menu_text_rect = menu_text.get_rect(center = (WIDTH // 1.21, 250+ 50 * i))
                window.blit(menu_text, menu_text_rect)

        # Update screen
            pygame.display.update()
            clock.tick(FPS)


def Scene1():
    global running
    while running:

       # Quit Event
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
                pygame.quit()
                exit()
                sys.exit()

        # 'Backspace' Key back to the main menu
            if e.type == pygame.KEYUP:
                if e.key == pygame.K_BACKSPACE:
                    switch_scene(MainMenu)
                    running = False 

        # 'Q' Key to quit
            if e.type == pygame.KEYUP:
                if e.key == pygame.K_q:
                    running = False
                    pygame.quit()
                    exit()
                    sys.exit()

        # Render objects
        fps_text = menu_font.render("FPS: " + str(clock.get_fps()), True, (255,255,255))
        window.fill((125, 250, 135))
        window.blit(fps_text, (0,50))
        window.blit(FirstSceneText,(0,0))

        # Update screen
        pygame.display.update()
        clock.tick(FPS)

def Scene2():
    global running
    while running:

       # Quit Event
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
                pygame.quit()
                exit()
                sys.exit()

        # 'Backspace' Key back to the main menu
            if e.type == pygame.KEYUP:
                if e.key == pygame.K_BACKSPACE:
                    switch_scene(MainMenu)
                    running = False 

        # 'Q' Key to quit
            if e.type == pygame.KEYUP:
                if e.key == pygame.K_q:
                    running = False
                    pygame.quit()
                    exit()
                    sys.exit()

        # Render objects
        window.fill((250, 125, 190))
        window.blit(SecondSceneText,(0,0))
        fps_text = menu_font.render("FPS: " + str(clock.get_fps()), True, (255,255,255))
        window.blit(fps_text, (0,50))

        # Update screen
        pygame.display.update()
        clock.tick(FPS)
# Switch scene
switch_scene(MainMenu)
while current_scene is not None:
    current_scene()

