import math
import sys
import pygame
from create_coords import COORDS_FUNCTIONS

class COORDS:
    def __init__(self, ins, version):

        self.l1_a = float(ins[0])
        self.l2_a = float(ins[1])
        self.ltable_a = float(ins[2])

        self.p1_off = float(ins[3])
        self.p2_off = float(ins[4])
        self.ptable_off = float(ins[5])

        self.size_x = int(ins[14])
        self.size_y = int(ins[15])
        self.p1_t = 2*math.pi*math.sqrt(self.l1_a/9.8) # -2.0
        self.p2_t = 2*math.pi*math.sqrt(self.l2_a/9.8) #1.013
        self.p3_t = 2*math.pi*math.sqrt(self.ltable_a/9.8) #1.00301

        self.p1_a_def = float(ins[6])
        self.p2_a_def = float(ins[7])
        self.table_xa_def = float(ins[8])
        self.table_ya_def = float(ins[9])

        self.p1_frict = 1 - float(ins[10])
        self.p2_frict = 1 - float(ins[11])
        self.table_frict = 1 - float(ins[12])

        self.timeout = float(ins[13])

        self.p1_a = self.p1_a_def
        self.p2_a = self.p2_a_def 
        self.table_xa = self.table_xa_def 
        self.table_ya = self.table_ya_def
        self.t = 0

        self.coords = COORDS_FUNCTIONS.fetch_functions(self, version)

    def get_size(self):
        return (self.size_x, self.size_y)

    def get_color(self):
        rgb1 = (255,60,40)
        rgb2 = (255,200,0)
        rgb3 = (0,100,100)
        rgb = [math.pow((1 - self.t/self.timeout),3) * rgb1[i] + 3*math.pow(1 - self.t/self.timeout,2)*(self.t/self.timeout) * rgb2[i] + 3*math.pow(self.t/self.timeout,2)*(1-self.t/self.timeout) * rgb3[i] + self.t*self.t/self.timeout/self.timeout*rgb1[i] for i in range(3)]
        return rgb
    
    def next_step(self,diff):
        self.x, self.y = self.coords()
        self.color = self.get_color()
        
        self.p1_a *= self.p1_frict
        self.p2_a *= self.p2_frict
        self.table_xa *= self.table_frict
        self.table_ya *= self.table_frict

        self.t += diff
        return not self.done()

    def get_xy(self):
        return self.x, self.y
    
    def done(self):
        if self.t < self.timeout:
            return False
        return True


def change_color_to_brush(brush, color):
    brush_c = pygame.surfarray.pixels3d(brush)
    brush_c[:, :, 0] = color[0]
    brush_c[:, :, 1] = color[1]
    brush_c[:, :, 2] = color[2]


def main():
    pygame.init()
    ins = open(sys.argv[1], "r").readlines()
    outs = sys.argv[2]

    simulation = COORDS(ins)

    main_screen = pygame.display.set_mode(simulation.get_size())
    main_screen.fill((0, 0, 0))
    pygame.display.flip()

    screen_area = pygame.Surface((8, 8), flags=pygame.SRCALPHA)
    brush = pygame.image.load("yellowbrush.png")
    brush.convert_alpha()

    flips = 0
    while simulation.next_step(0.001):
        change_color_to_brush(brush, simulation.get_color())
        main_screen.blit(brush, simulation.get_xy())
        flips += 1
        if flips % 400 == 0:
            pygame.display.flip()
    pygame.display.flip()
    input("exit? (enter for yes)")
    pygame.image.save(main_screen, outs)


if __name__ == "__main__":
    main()
