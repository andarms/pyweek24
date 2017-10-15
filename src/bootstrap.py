import os
import pygame as pg

SCREEN_SIZE = (1024, 640)
ORIGINAL_CAPTION = "Game"

# init pygame and create the window
pg.init()
os.environ['SDL_VIDEO_CENTERED'] = "TRUE"
pg.display.set_caption(ORIGINAL_CAPTION)
SCREEN = pg.display.set_mode(SCREEN_SIZE)
SCREEN_RECT = SCREEN.get_rect()


# load all the assets
