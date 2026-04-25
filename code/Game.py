#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

class Game:
    def __init__(self):
        self.window = None

    def run(self, ):
        print('Código Iniciado')
        pygame.init()
        screen = pygame.display.set_mode(size = (600, 480))
        print('Código Encerrado')

        print('Looping Iniciado')
        while True:
            # Checagem de todos os eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() # Fechar janela
                    quit() # Finalizar o Pygame