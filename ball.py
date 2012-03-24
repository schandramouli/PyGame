import pygame
w=640
h=480
sp=[20,20]
screen=pygame.display.set_mode((w,h))
ball=pygame.image.load("Desktop//ball.gif")
br=ball.get_rect()
flag=1
while flag:
 for e in pygame.event.get():
  if e.type==pygame.QUIT:
   flag=0
 
 br=br.move(sp)
 if br.left<=0 or br.right>=w:
  sp[0]=-sp[0]
 elif br.top<=0 or br.bottom>=h:
  sp[1]=-sp[1]
 screen.fill((0,0,0))
 screen.blit(ball,br)
 pygame.display.flip()

