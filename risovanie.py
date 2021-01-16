import pygame,zakona


def izmeni_kartinku(kartinka, shirina, visota, uberi_cvet, porog):
    kartinka = pygame.transform.scale(kartinka, [shirina, visota])
    kartinka = kartinka.convert()
    m1 = pygame.mask.from_threshold(kartinka, uberi_cvet, [porog, porog, porog])
    m1.invert()
    q2 = kartinka.copy()
    q2.fill([0, 0, 0, 0])
    m1.to_surface(q2, kartinka, None, None, None)
    q2.set_colorkey([0, 0, 0])
    return q2

screen = pygame.display.set_mode([1000, 700])
tynk1 = pygame.image.load("photo/d-a1.jpg")
tynk1=izmeni_kartinku(tynk1,58,68,[255,255,255],20)
tynk2 = pygame.image.load("photo/RE.jpg")
tynk2=izmeni_kartinku(tynk2,58,68,[255,255,255],20)
hp1 = pygame.image.load("photo/serdce.jpg")
hp1 = izmeni_kartinku(hp1, 58, 68, [255, 255, 255], 20)
hp2 = pygame.image.load("photo/serdcegreen.jpeg")
hp2 = izmeni_kartinku(hp2, 58, 68, [255, 255, 255], 20)

def fp():
    screen.fill([0,0,255])
    one1 = pygame.transform.rotate(tynk1, zakona.grad1)
    two2 = pygame.transform.rotate(tynk2, zakona.grad2)
    screen.blit(one1, zakona.one)
    screen.blit(two2, zakona.two)


    q = 0
    dz=[*range(zakona.hp1)]
    for zd in dz:
        screen.blit(hp1, [100 + q, 3])
        q += 50
    dz2 = range(zakona.hp2)
    q = 0
    for zd in dz2:
        screen.blit(hp2, [610 + q, 630])
        q += 50
    pygame.display.flip()


