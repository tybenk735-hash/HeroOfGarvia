import sys, pygame, Player

pygame.init()
size = width, height = 1280, 960
screen = pygame.display.set_mode(size)
black = 0, 0, 0

player = pygame.image.load("Sprites/player.gif")
playerrect = player.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            if pygame.K_d:
                pass

    screen.fill(black)
    screen.blit(player, )
    pygame.display.flip()