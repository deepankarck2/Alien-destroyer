import sys
import pygame as pg 

def run_game():
    pg.init()
    screen = pg.display.set_mode((1299,800))
    pg.display.set_caption("Alien Invation")

    #Start the main loop ofr the game.

    while True:

        #watch for keyboard and mouse events.
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
        # Make the most recently drawn screen visible.
        pg.display.flip()

run_game()