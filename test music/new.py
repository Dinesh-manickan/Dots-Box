from button import Button
import os , sys
import pygame
from pygame import mixer


pygame.init()
mixer.init()
mixer.music.set_volume(0.2)

def Get_Path(DB_DOCS_NAME):
    dir = os.path.dirname(__file__)
    abs_path = os.path.join(dir, DB_DOCS_NAME)
    return abs_path 

width=500
height=500

BG = pygame.image.load(Get_Path("assets/Background.png"))

SCREEN = pygame.display.set_mode((width, height))

def get_font(size): 
    return pygame.font.Font(Get_Path("assets/font.ttf"), size)

pygame.display.set_caption("Stack Tower")


def main_menu():
    try:
        mixer.music.load(Get_Path('assets/main.mp3'))
        mixer.music.play()
    except:
        print("Music error")
    while True:
       
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        GAME_TITLE = get_font(33).render("STACK TOWER", True, "#DF6589FF")
        GAME_RECT = GAME_TITLE.get_rect(center=(width/2, height/2 - 100))

        MENU_TEXT = get_font(25).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(width/2, height/2 - 50))

        PLAY_BUTTON = Button(image=None, pos=(width/2, height/2 ), 
                            text_input="PLAY", font=get_font(20), base_color="#d7fcd4", hovering_color="White")
        
        QUIT_BUTTON = Button(image=None, pos=(width/2, height/2 + 50), 
                            text_input="QUIT", font=get_font(20), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(GAME_TITLE, GAME_RECT)
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    mixer.music.stop()
                    mixer.music.load(Get_Path('assets/play.mp3'))
                    mixer.music.play()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
        
main_menu()
