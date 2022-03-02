import pygame


def write(win, txt, x, y, color=(255, 255, 255), size=50, aa=True, angle=0):
    temp = pygame.font.SysFont("Arial", size)
    temp = temp.render(txt, aa, color)
    temp = pygame.transform.rotate(temp, angle)
    win.blit(temp, (x, y))


class Block:
    def __init__(self, m, v, c, x, y, s):
        self.m = m
        self.v = v
        self.color = c
        self.x = x
        self.y = y - s
        self.s = s

    def collide(self, b):
        u1 = (self.m * self.v + 2 * b.m * b.v - b.m * self.v) / (self.m + b.m)
        u2 = self.v - b.v + u1

        self.v = u1
        b.v = u2

    def wall_collide(self):
        self.v = -self.v

    def draw(self, win, n):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.s, self.s))
        write(win, n, self.x, self.y)

    def move(self):
        self.x -= self.v

    def is_collide_block(self, b):
        return b.x <= self.x <= b.x + b.s


