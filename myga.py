import pygame
screen=pygame.display.set_mode((640,480))
flag=1
cl=pygame.time.Clock()
while flag==1:
 for e in pygame.event.get():
  if e.type==pygame.QUIT:
   flag=0
  elif e.type==pygame.MOUSEBUTTONDOWN:
   print "%d %d" % e.pos
  
 pygame.display.flip()
 cl.tick(1)

