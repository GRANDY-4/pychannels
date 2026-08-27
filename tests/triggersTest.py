import pychannels as p

p.func = """
import pygame as pg

pg.display.set_caption("Test")
pg.display.set_mode((1000, 600))

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
"""
p.triggers.assign("new window", p.func)

p.triggers.trigger("new window")
