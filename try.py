#loading
import pygame,math
pygame.init()
screen=pygame.display.set_mode((640,320))
flag=1
pi=math.pi
f=pygame.font.Font(None,25)
text = f.render("LOADING",True,(255,255,255),(0,0,0))
rect=text.get_rect()
rect.centerx=320
rect.centery=230
screen.blit(text,rect)
while flag:
 for i in range(0,372,10):
  pygame.draw.arc(screen,(255,255,255),(245,165,150,150),0,i*pi/180,13)  
  t2=f.render(str(i*100/370)+'%',True,(255,255,255),(0,0,0))
  r2=t2.get_rect()
  r2.centerx=320
  r2.centery=250  
  screen.blit(t2,r2)
  pygame.display.flip()
  pygame.time.delay(100)
  flag=0
  
 for e in pygame.event.get():
  if e.type==pygame.QUIT:
   flag=0
  elif e.type==pygame.MOUSEBUTTONDOWN:
   print e.pos



