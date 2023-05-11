import pygame
import pygame as pg


class Player:
    def __init__(self, position, dimensions, colour, name):
        self.pos = position
        self.dims = dimensions
        self.colour = colour
        self.name = name
        self.rect = (self.pos[0], self.pos[1], dimensions[0], dimensions[1])
        self.vel = 3

    def draw(self, win):
        pg.draw.rect(win, self.colour, self.rect)
        txt = pg.font.SysFont('Arial', 20).render(str(self.name), True, 'black')
        win.blit(txt, (self.pos[0], self.pos[1] - 10))

    def move(self):
        keys = pg.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.pos[0] -= self.vel
        if keys[pygame.K_RIGHT]:
            self.pos[0] += self.vel
        if keys[pygame.K_UP]:
            self.pos[1] -= self.vel
        if keys[pygame.K_DOWN]:
            self.pos[1] += self.vel

        self.update()

    def change_colour(self):
        keys = pg.key.get_pressed()
        if keys[pygame.K_b]:
            self.colour = 'blue'
        if keys[pygame.K_r]:
            self.colour = 'red'
        if keys[pygame.K_y]:
            self.colour = 'yellow'

    def update(self):
        self.change_colour()
        self.rect = (self.pos[0], self.pos[1], self.dims[0], self.dims[1])



