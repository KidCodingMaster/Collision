import pygame

pygame.init()

screen = pygame.display.set_mode((1280, 720))

font = pygame.font.SysFont("cosmicsans", 60)

you_win_text = font.render("You Win!", True, (255, 255, 255))

bg = pygame.image.load("bg.jpg")
bg = pygame.transform.scale(bg, (1280, 720))

rect = pygame.Rect(0, 720 // 2, 50, 50)

player = pygame.Rect(1220, 720 // 2, 50, 50)

win = False
hits = 0

sound = pygame.mixer.Sound('./win.mp3')

while True:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        rect.x -= 1
    if keys[pygame.K_RIGHT]:
        rect.x += 1
    if keys[pygame.K_UP]:
        rect.y -= 1
    if keys[pygame.K_DOWN]:
        rect.y += 1

    screen.blit(bg, (0, 0))

    if player.colliderect(rect):
        win = True
        hits += 1

    if hits == 1:
        sound.play()


    if not win:
        pygame.draw.rect(screen, (255, 255, 255), rect)
        pygame.draw.rect(screen, (255, 255, 0), player)

    if win:
        screen.blit(you_win_text, (1280 // 2, 720 // 2))

    pygame.display.update()
