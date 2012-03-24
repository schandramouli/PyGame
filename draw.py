import pygame
screen=pygame.display.set_mode((640,480))
flag=1
color=(0,0,0)
clock=pygame.time.Clock()
while flag:
 for e in pygame.event.get():
 
  if e.type==pygame.QUIT: flag=0
  elif e.type==pygame.MOUSEBUTTONDOWN: 
   color=(255,255,255)
   screen.set_at(e.pos,color)
  elif e.type==pygame.MOUSEMOTION: screen.set_at(e.pos,color)
  elif e.type==pygame.MOUSEBUTTONUP:
   screen.set_at(e.pos,color)
   color=(0,0,0)

 
 pygame.display.flip()
 clock.tick(1000)

