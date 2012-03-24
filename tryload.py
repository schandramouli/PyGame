import pygame
w=640
h=480
screen=pygame.display.set_mode((w,h))
flag=1
while flag:

 pygame.draw.arc(screen,(255,255,255),(w/2,h/2-150/3.46,25,150/1.73),0,8,1)
 pygame.display.flip()
 for e in pygame.event.get():
  if e.type==pygame.KEYDOWN:
   flag=0
