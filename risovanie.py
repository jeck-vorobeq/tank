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
phon=pygame.image.load("photo/cat.jpg")
phon=izmeni_kartinku(phon,1000,700,[255,255,255],10)
baz1=pygame.image.load("photo/baza.jpg")
baz1=pygame.transform.scale(baz1,[100,60])
baz2=pygame.image.load("photo/bazagreen.jpg")
baz2=pygame.transform.scale(baz2,[100,60])
tynk1 = pygame.image.load("photo/d-a1.jpg")
tynk1=izmeni_kartinku(tynk1,58,68,[255,255,255],20)
tynk2 = pygame.image.load("photo/RE.jpg")
tynk2=izmeni_kartinku(tynk2,58,68,[255,255,255],20)
hp1 = pygame.image.load("photo/serdce.jpg")
hp1 = izmeni_kartinku(hp1, 58, 68, [255, 255, 255], 20)
hp2 = pygame.image.load("photo/serdcegreen.jpeg")
hp2 = izmeni_kartinku(hp2, 58, 68, [255, 255, 255], 20)
pula = pygame.image.load("photo/pula.png")
pula = izmeni_kartinku(pula,18,58,[230,230,230],50)

def fps():
    screen.fill([8,8,8])
    screen.blit(phon, [0, 0])
    one1 = pygame.transform.rotate(tynk1, zakona.grad1)
    two2 = pygame.transform.rotate(tynk2, zakona.grad2)
    screen.blit(baz1, zakona.baz1)
    screen.blit(baz2, zakona.baz2)
    screen.blit(one1, zakona.one)
    screen.blit(two2, zakona.two)
    if zakona.pularect is not None:
        #screen.blit(pula, zakona.pularect)
        pygame.draw.rect(screen, [200,2,20], zakona.pularect, 1)



    q = 0
    dz=[*range(zakona.hp1)]
    for zd in dz:
        screen.blit(hp1, [100 + q, 3])
        q += 50
    dz2 = range(zakona.hp2)
    q = 0
    for zd in dz2:
        screen.blit(hp2, [700 + q, 630])
        q+=50
    puli = [*range(zakona.pula)]
    for zd in puli:
        screen.blit(pula, [100 + q, 3])
        q += 50
    puli2 = range(zakona.pula)
    q = 0
    for zd in puli2:
         screen.blit(pula, [700 - q, 630])
         q += 50
    pygame.display.flip()


