import pygame
screen=pygame.display.set_mode((640,400))
x=0
y=0
while 1:
 event=pygame.event.poll()
 if event.type==pygame.QUIT:
  break
 elif event.type==pygame.MOUSEMOTION:
  x,y=event.pos
 screen.fill((0,0,0))
 pygame.draw.line(screen,(255,255,255),(x,0),(x,399))
 pygame.draw.line(screen,(255,255,255),(0,y),(639,y))
 pygame.display.flip()

