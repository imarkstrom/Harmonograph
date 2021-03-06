# Author: Ingemar Markström
import sys
import pygame
import coords_collection
import os


def change_color_to_brush(brush, color):
    brush_c = pygame.surfarray.pixels3d(brush)
    brush_c[:, :, 0] = color[0]
    brush_c[:, :, 1] = color[1]
    brush_c[:, :, 2] = color[2]


def main():
    pygame.init()
    ins = open(sys.argv[1], "r").readlines()
    outs = sys.argv[2]
    user_coords = False
    if sys.argv[3][0] == "u":
        user_coords = True
        sys.argv[3] = sys.argv[3][1:]
        
    user_color = False
    if sys.argv[4][0] == "u":
        user_color = True
        sys.argv[4] = sys.argv[4][1:]
        print(sys.argv[4])

    version = int(sys.argv[3])
    color_version = int(sys.argv[4])
    strike_through = False
    if len(sys.argv) > 5:
        strike_through_num = int(sys.argv[5])
        if strike_through_num > 0:
            strike_through = True

    brush_path = "src/brush.png"
    if len(sys.argv) > 6:
        brush_path = sys.argv[6] 

    
    simulation = coords_collection.COORDS(ins,version,user_coords,color_version,user_color)

    main_screen = pygame.display.set_mode(simulation.get_size())
    main_screen.fill((0, 0, 0))
    pygame.display.flip()

    #screen_area = pygame.Surface( (8, 8), flags=pygame.SRCALPHA)
    brush = pygame.image.load(brush_path)
    brush.convert_alpha()

    flips = 0
    while simulation.next_step(0.001):
        if strike_through:
            if (flips // strike_through_num) % 2 == 0:
                change_color_to_brush(brush, simulation.get_color())
                main_screen.blit(brush, simulation.get_xy())
        else:
            change_color_to_brush(brush, simulation.get_color())
            main_screen.blit(brush, simulation.get_xy())
        flips += 1
        
        if flips % 400 == 0:
            pygame.display.flip()
    pygame.display.flip()
    input("exit? (enter for yes)")
    pygame.image.save(main_screen, outs)
