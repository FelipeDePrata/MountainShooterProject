#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image
from pygame.font import Font

from code.Const import WIN_WIDTH, WIN_HEIGHT, COLOR_MAX_BLUE, COLOR_MAX_BLACK, MENU_OPTION, COLOR_YELLOW


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png')
        self.rectangle = self.surf.get_rect(left=0,top=0)

    def run(self, ): # Updating menu background, texts and music
        menu_option = 0
        pygame.mixer_music.load('./asset/Menu.mp3')
        pygame.mixer_music.play(-1)

        while True:
            self.window.blit(source=self.surf, dest=self.rectangle)
            self.menu_text(50, "Mountain", COLOR_MAX_BLUE, ((WIN_WIDTH / 2), 70))
            self.menu_text(50, "Shooter", COLOR_MAX_BLUE, ((WIN_WIDTH / 2), 120))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(20, MENU_OPTION[i], COLOR_YELLOW, ((WIN_WIDTH / 2), 200 + 25 * i))
                else:
                    self.menu_text(20, MENU_OPTION[i] , COLOR_MAX_BLACK, ((WIN_WIDTH / 2), 200 + 25 * i))

            # Check for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() # Close screen
                    quit()
                if event.type == pygame.KEYDOWN: # DOWN KEY
                    if event.key == pygame.K_DOWN:
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.KEYUP: # UP KEY
                        if event.key == pygame.K_UP:
                            if menu_option > 0:
                                menu_option -= 1
                            else:
                                menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN: # ENTER
                        return MENU_OPTION(menu_option)

            pygame.display.flip()

    # Configurating menu text
    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf = Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
