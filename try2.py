#spell
import pygame,math
w=640
h=480
screen=pygame.display.set_mode((w,h))
flag=1
startx=10
endx=600
y=100
spellcolor=(255,0,0)
rad=3.14/180
while flag:
 
 for x in range(startx,endx,1):
  screen.set_at((x,y+int(7*math.sin(x*rad))),spellcolor)
  screen.set_at((x,y+int(7*math.sin((x+90)*rad))),spellcolor)
  screen.set_at((x,y+int(7*math.sin((x+180)*rad))),spellcolor)
  
  pygame.display.flip()
 



 
 for e in pygame.event.get():
  if e.type in (pygame.QUIT,pygame.KEYDOWN):
   flag=0
  elif e.type==pygame.MOUSEBUTTONDOWN:
   print e.pos



