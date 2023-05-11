import pygame
import pygame as pg
from player import Player
from network import Network

width = 500
height = 500
win = pg.display.set_mode((width, height))
pg.display.set_caption("Client")
pg.init()


def redrawWindow(win, player, player2):
    win.fill('white')
    player.draw(win)
    player2.draw(win)
    pg.display.update()


def main():
    run = True
    n = Network()
    p = n.get_p()
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        p2 = n.send(p)

        # Event handler
        for event in pg.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        # Display update
        p.move()
        redrawWindow(win, p, p2)

def menu_screen():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        win.fill((128, 128, 128))
        font = pygame.font.SysFont("comicsans", 60)
        text = font.render(f"Click to Play!", 1, (255,0,0))
        font = pygame.font.SysFont("comicsans", 15)
        txt = font.render(f"You can change your to blue with b, red with r and yellow with y", 1, (255, 0, 0))
        win.blit(text, (100,200))
        win.blit(txt, (50, 300))
        pygame.display.update()

        for event in pygame.event.get():
            keys = pg.key.get_pressed()
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                run = False





    main()

while True:
    menu_screen()
