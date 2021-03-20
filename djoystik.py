import pygame,zakona

#pygame.key.set_repeat(70)




def xbox():
    events = pygame.event.get()
    for e in events:
        if e.type == pygame.KEYDOWN and e.key == pygame.K_RCTRL:

            zakona.vestrel(zakona.grad1, zakona.one)
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
    for e in events:
        if e.type == pygame.KEYDOWN and e.key == pygame.K_LSHIFT:
            zakona.vestrel(zakona.grad2, zakona.two)




