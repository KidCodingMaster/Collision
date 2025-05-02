import pygame

pygame.init()

screen = pygame.display.set_mode((1280, 720))

rect1 = pygame.Rect(10, 10, 10, 10)
rect2 = pygame.Rect(50, 50, 10, 10)

CHANGE_COLOR = pygame.USEREVENT + 1

pygame.time.set_timer(CHANGE_COLOR, 1000)

color = False

while True:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == CHANGE_COLOR:
            color = not color

    if color:
        pygame.draw.rect(screen, (255, 0, 0), rect1)
        pygame.draw.rect(screen, (255, 0, 0), rect2)
    else:
        pygame.draw.rect(screen, (0, 255, 0), rect1)
        pygame.draw.rect(screen, (0, 255, 0), rect2)

    pygame.display.update()
