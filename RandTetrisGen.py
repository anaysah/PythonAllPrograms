from random import randint,choice
import pygame
pygame.init()

win = pygame.display.set_mode((400,600))
win.fill((225,225,225))
pygame.display.set_caption("TETRIS")

row = randint(1, 4)
col = 5-row
cell_size = 40
lis = []
newlis = []

for r in range(1,row+1):
    for i in range(1,col+1):
        lis.append([r,i])

cho = choice(lis)
newlis.append(cho)
lis.remove(cho)
while len(newlis)!=4:
    cho = choice(lis)
    found = [cho[0]+1,cho[1]] in newlis or [cho[0],cho[1]+1] in newlis or [cho[0]-1,cho[1]] in newlis or [cho[0],cho[1]-1] in newlis
    if found:
        newlis.append(cho)
        lis.remove(cho)

clock = pygame.time.Clock()
while exit:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    for r in newlis:
        block = pygame.draw.rect(win,"Blue",((r[1])*cell_size,(r[0])*cell_size,cell_size,cell_size))

    pygame.display.update()



