import pygame

print('Código Iniciado')
pygame.init()
screen = pygame.display.set_mode(size = (800, 600))
print('Código Encerrado')

print('Looping Iniciado')
while True:
    # Checagem de todos os eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # Fechar janela
            quit() # Finalizar o Pygame