import sys
import pygame as pg
from mob import Mob
pg.init()

#game window
SCR_WIDTH = 1280
SCR_HEIGHT = 720
screen = pg.display.set_mode((SCR_WIDTH,SCR_HEIGHT))
pg.display.set_caption('Reverse Tower Defense')

clock = pg.time.Clock()
fps = 60

#load images
bg = pg.image.load('img/bg.png').convert_alpha()

#mob
mob_img_01 = pg.image.load('img/mob1.PNG').convert_alpha()

mob_group = pg.sprite.Group()

waypoints = [
    (380,520),
    (430,490),
    (210,340),
    (360,255),
    (650,440),
    (820,340),
    (540,140),
    (700,55),
    (845,145),
    (880,125)
]

mob = Mob(waypoints,mob_img_01,0.1)
mob_group.add(mob)




#game loop
run = True
while run:

    clock.tick(fps)
    screen.blit(bg, (0,0))

    #mob's path
    pg.draw.lines(screen,"red",False,waypoints,3)

    #update group
    mob_group.update()

    mob_group.draw(screen)
    
    #event handler
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    pg.display.flip()
    
pg.quit()
sys.exit()