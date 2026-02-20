import sys, pygame, Player

pygame.init()
size = width, height = 1280, 960
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
black = 0, 0, 0

player_run = [pygame.image.load(f"Sprites/Player/{i}.png") for i in range(1, 4)]

i = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            if pygame.K_d:
                pass
        screen.fill(black)
        screen.blit(player_run[i // 6], (1000, 200))
        i += 1
        if i == 60:
            i = 0
        pygame.display.flip()
        clock.tick(60)