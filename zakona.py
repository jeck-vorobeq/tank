import pygame



one = pygame.Rect(-10, 400, 58, 68)
two = pygame.Rect(100, 400, 58, 68)

baz2 = pygame.Rect(5, 4, 100, 40)
baz1 = pygame.Rect(850, 630, 100, 40)

grad1 = 0
grad2 = 180
puli = []

hp1 = 3
hp2 = 3

pulu1 = 6
pulu2 = 6


def granici(tank):
    if tank.left <= 0:
        tank.x = 0
    if tank.right >= 1000:
        tank.right = 1000
    if tank.top <= 0:
        tank.y = 0
    if tank.bottom >= 700:
        tank.bottom = 700


def up_down_tank(move, tank):
    tank.y += move
    tank.width = 58
    tank.height = 68
    granici(tank)


def left_right_tank(move, tank):
    tank.x += move
    tank.width = 68
    tank.height = 58
    granici(tank)


def vestrel(gradus, tank):
    global pulu1, pulu2
    if tank is one and pulu1 > 0:
        canstrel1 = True
    else:
        canstrel1 = False

    if tank is two and pulu2 > 0:
        canstrel2 = True
    else:
        canstrel2 = False

    if canstrel1 == True or canstrel2 == True:
        if gradus == 90:
            pulagrad = 90
            pularect = pygame.Rect(tank.left - 30, tank.centery - 10, 30, 20)
        if gradus == -90:
            pulagrad = -90
            pularect = pygame.Rect(tank.right, tank.centery - 10, 30, 20)
        if gradus == 0:
            pulagrad = 0
            pularect = pygame.Rect(0, 0, 20, 30)
            pularect.bottom = tank.top
            pularect.centerx = tank.centerx
        if gradus == 180:
            pularect = pygame.Rect(0, 0, 20, 30)
            pulagrad = 180
            pularect.top = tank.bottom
            pularect.centerx = tank.centerx
        if tank == one:
            pulu1 -= 1
        if tank == two:
            pulu2 -= 1

        pula = {"rect": pularect, "grad": pulagrad}
        puli.append(pula)


def polet_puli():
    for b in puli:

        r = b["rect"]
        if b["grad"] == 90:
            r.x -= 6
        if b["grad"] == -90:
            r.x += 6
        if b["grad"] == 180:
            r.y += 6
        if b["grad"] == 0:
            r.y -= 6


def otduh():
    global pulu1, pulu2
    w = one.colliderect(baz1)
    if w == 1:
        pulu1 = 6
    w = two.colliderect(baz2)
    if w == 1:
        pulu2 = 6


def popadanie():
    global hp1, hp2
    for among in puli:

        q = one.colliderect(among["rect"])
        if q == 1:
            hp1 -= 1
            puli.remove(among)

        q = two.colliderect(among["rect"])
        if q == 1:
            hp2 -= 1
            puli.remove(among)

    if hp1 == 0:
        print("GAME OVER GREEN")

    if hp2 == 0:
        print("GAME OVER RED")

