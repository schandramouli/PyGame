import pygame
screen=pygame.display.set_mode((320,200))

while 1:
 e=pygame.event.poll()
 if e.type==pygame.QUIT:
  break
 elif e.type==pygame.MOUSEBUTTONDOWN:
  print "Pressed at (%d,%d)" % e.pos
 elif e.type==pygame.MOUSEBUTTONUP:
  print "Released at (%d,%d)"%e.pos

 screen.fill((0,0,0))
 pygame.display.flip()
