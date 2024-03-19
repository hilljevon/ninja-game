import pygame
import os
BASE_IMG_PATH = 'data/images/'
def load_image(path):
    # .convert allows for performance
    img = pygame.image.load(BASE_IMG_PATH + path).convert()
    img.set_colorkey((0,0,0))
    return img

def load_images(path):
    images = []
    # os.listdir takes a path as argument and returns all images in that path. in this case, navigating to our specified pathing and iterating through the entire directory
    for img_name in os.listdir(BASE_IMG_PATH + path):
        images.append(load_image(path + '/' + img_name))
    return images