import pygame
y=0
d=3
b=[]
screen = pygame.display.set_mode((300,240))
for i in range(1,63):
 b.append((0,0,i*4))
for i in range(1,63):
 b.append((0,0,255-i*4))

while 1:
 e=pygame.event.poll()
 if e.type==pygame.QUIT:
  break
 screen.fill((0,0,0))
 for i in range(0,124):
  pygame.draw.line(screen,b[i],(50,y+i),(100,y+i))
 y+=d;
 if y+124>0 or y<0:d*=-1
 pygame.display.flip()


