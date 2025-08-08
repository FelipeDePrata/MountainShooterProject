import pygame

print('start')
pygame.init()
screen = pygame.display.set_mode(size=(600, 480))
print('end')

print('loop')
while True:
    #Check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() #Close screen
            quit()