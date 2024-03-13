import pygame

import os

BASE_IMAGE_PATH = "src/image/"

def load_image(path):
    img = pygame.image.load(BASE_IMAGE_PATH + path).convert()
    surf = pygame.Surface(img.get_size(),pygame.HWSURFACE)
    surf.blit(img, (0,0))
    surf.set_colorkey((0,0,0))
    return surf

def load_images(path):
    images = []
    for img_name in sorted(os.listdir(BASE_IMAGE_PATH + path)):
        images.append(load_image(path + '/' + img_name))
    return images