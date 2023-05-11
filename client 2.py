import pygame
import pygame as pg
from player import Player
from network import Network

width = 500
height = 500
win = pg.display.set_mode((width, height))
pg.display.set_caption("Client")


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

main()
