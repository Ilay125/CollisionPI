import pygame
from Block import Block

WIDTH = 800
HEIGHT = 600

win = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

b1 = Block(10000, 0.5, (20, 100, 255), 600, 500, 100)
b2 = Block(1, 0, (200, 0, 0), 200, 500, 50)

coll_cnt = 0

'''
while b1.v > b2.v:
    b1.collide(b2)
    coll_cnt += 1
    if b2.v > 0:
        b2.wall_collide()
        coll_cnt += 1

print(coll_cnt)
'''



pygame.init()


def write(txt, x, y, color=(255, 255, 255), size=50, aa=True, angle=0):
    temp = pygame.font.SysFont("Arial", size)
    temp = temp.render(txt, aa, color)
    temp = pygame.transform.rotate(temp, angle)
    win.blit(temp, (x, y))


while True:
    win.fill((0, 0, 0))

    pygame.draw.line(win, (255, 255, 255), (0, 500), (WIDTH, 500), 3)
    pygame.draw.line(win, (255, 255, 255), (10, 0), (10, HEIGHT), 3)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    if b1.is_collide_block(b2):
        b1.collide(b2)
        coll_cnt += 1

    if b2.is_collide_block(b1):
        b2.collide(b1)
        coll_cnt += 1

    if b1.x <= 10:
        b1.wall_collide()
        coll_cnt += 1

    if b2.x <= 10:
        b2.wall_collide()
        coll_cnt += 1

    b1.move()
    b2.move()

    b1.draw(win, "M")
    b2.draw(win, "m")

    write(f"VM: {b1.v}", 10, 10, size=30)
    write(f"Vm: {b2.v}", 10, 40, size=30)
    write(f"Collisions: {coll_cnt}", 10, 70, size=30)

    clock.tick()
    pygame.display.update()
