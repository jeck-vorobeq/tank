import pygame

screen = pygame.display.set_mode([1000, 700])
tynk1 = pygame.image.load("photo/d-a1.jpg")
def fp():
    screen.blit(tynk1, [122, 45])
    pygame.display.flip()