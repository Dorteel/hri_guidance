import sys, pygame
pygame.init()

size = width, height = 320, 240
speed = [2, 2]
black = 0, 0, 0
screen = pygame.display.set_mode(size)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("Left DOWN")
            if event.key == pygame.K_RIGHT:
                print("Right DOWN")

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                print("Left UP")
            if event.key == pygame.K_RIGHT:
                print("Right UP")          


pygame.display.quit()
    
#screen = pygame.display.set_mode(size)
