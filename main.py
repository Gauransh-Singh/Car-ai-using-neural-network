import pygame

pygame.init()

WIDTH,HEIGHT = 1080, 720 

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lets Race")

RED = (255, 0, 0)

x, y = 10, 10

running = True
while running:
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if keys[pygame.K_a]:
        x -= 0.5
    if keys[pygame.K_d]:
        x += 0.5
    if keys[pygame.K_w]:
        y -= 0.5
    if keys[pygame.K_s]:
        y += 0.5

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, RED, (x, y, 40, 20))
    pygame.display.flip()

pygame.quit()