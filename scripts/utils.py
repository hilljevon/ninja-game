import pygame
BASE_IMG_PATH = 'data/images/'
def load_image(path):
    # .convert allows for performance
    img = pygame.image.load(BASE_IMG_PATH + path).convert()
    img.set_colorkey((0,0,0))
    return img