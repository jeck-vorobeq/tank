import pygame,zakona

pygame.key.set_repeat(70)




def xbox():
    events = pygame.event.get()
    keys=pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        zakona.grad1=0
        zakona.one.y-=3
    elif keys[pygame.K_DOWN]:
        zakona.grad1 = 180
        zakona.one.y+=3
    elif keys[pygame.K_RIGHT]:
        zakona.grad1 = -90
        zakona.one.x+=3
    elif  keys[pygame.K_LEFT]:
        zakona.grad1 = 90
        zakona.one.x-=3
        zakona.granici()


    if keys[pygame.K_w]:
        zakona.grad2 = 0
        zakona.two.y -= 3
    elif keys[pygame.K_s]:
        zakona.grad2 = 180
        zakona.two.y += 3
    elif keys[pygame.K_d]:
        zakona.grad2 = -90
        zakona.two.x += 3
    elif keys[pygame.K_a]:
        zakona.grad2 = 90
        zakona.two.x -= 3




