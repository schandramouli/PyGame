# loading of deathly hallows

import pygame

w=1024
h=728
screen=pygame.display.set_mode((w,h))
l=150
wid=3
white=(255,255,255)
black=(0,0,0)
clock=pygame.time.Clock()
flag=1
while flag:
 i=4
 while i<=30:
  pygame.draw.line(screen,white,(w/2,h/2-l/1.73),(w/2-l/2,h/2+l/3.46),wid)
  pygame.draw.line(screen,white,(w/2,h/2-l/1.73),(w/2+l/2,h/2+l/3.46),wid) 
  pygame.draw.line(screen,white,(w/2-l/2,h/2+l/3.46),(w/2+l/2,h/2+l/3.46),wid) 
  pygame.draw.line(screen,white,(w/2,h/2-l/1.73),(w/2,h/2+l/3.46),wid)
  pygame.draw.arc(screen,white,(w/2-l/4-5+i,h/2-l/3.46,l/2+10-2*i,l/1.73),-1.57,1.57,i/4)
  pygame.draw.arc(screen,white,(w/2-l/4-5+i,h/2-l/3.46,l/2+10-2*i,l/1.73),1.57,4.71,i/4) 
  pygame.display.flip()
  pygame.time.delay(10)
  pygame.draw.arc(screen,black,(w/2-l/4-5+i,h/2-l/3.46,l/2+10-2*i,l/1.73),-1.57,1.57,i/4)
  pygame.draw.arc(screen,black,(w/2-l/4-5+i,h/2-l/3.46,l/2+10-2*i,l/1.73),1.57,4.71,i/4)
  
  i+=1
 

 for e in pygame.event.get():
  if e.type==pygame.QUIT:
   flag=0
  elif e.type==pygame.KEYDOWN:
   flag=0
 
 clock.tick(200)

