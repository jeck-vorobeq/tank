import pygame,zakona

pygame.key.set_repeat(70)




def xbox():
    events = pygame.event.get()
    keys=pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        zakona.grad1=0
        zakona.up_down_tank(-3,zakona.one)
    elif keys[pygame.K_DOWN]:
        zakona.grad1 = 180
        zakona.up_down_tank(3,zakona.one)
    elif keys[pygame.K_RIGHT]:
        zakona.grad1 = -90
        zakona.left_right_tank(3,zakona.one)
    elif  keys[pygame.K_LEFT]:
        zakona.grad1 = 90
        zakona.left_right_tank(-3,zakona.one)
    elif pygame.key.get_mods() & pygame.KMOD_RCTRL:
        zakona.vestrel()


    if keys[pygame.K_w]:
        zakona.grad2 = 0
        zakona.up_down_tank(-3, zakona.two)
    elif keys[pygame.K_s]:
        zakona.grad2 = 180
        zakona.up_down_tank(3, zakona.two)
    elif keys[pygame.K_d]:
        zakona.grad2 = -90
        zakona.left_right_tank(3, zakona.two)
    elif keys[pygame.K_a]:
        zakona.grad2 = 90
        zakona.left_right_tank(-3, zakona.two)




