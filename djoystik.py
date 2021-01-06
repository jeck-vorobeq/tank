import pygame,zakona

pygame.key.set_repeat(70)




def xbox():
    events = pygame.event.get()
    for e in events:
        if e.type == pygame.KEYDOWN and e.key == pygame.K_UP:
            zakona.one.y-=3
        if e.type == pygame.KEYDOWN and e.key == pygame.K_DOWN:
            pass
        if e.type == pygame.KEYDOWN and e.key == pygame.K_RIGHT:
            pass
        if e.type == pygame.KEYDOWN and e.key == pygame.K_LEFT:
            pass





