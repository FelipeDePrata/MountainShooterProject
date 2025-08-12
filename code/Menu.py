#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png')
        self.rectangle = self.surf.get_rect(left=0,top=0)

    def run(self, ): #Updating menu background
        self.window.blit(source=self.surf, dest=self.rectangle)
        pygame.display.flip()
        pass
