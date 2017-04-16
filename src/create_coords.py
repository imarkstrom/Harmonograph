# Author: Ingemar Markström
import math

class COORDS_FUNCTIONS:
    def fetch_functions(coords):
        def c0():
            x = coords.size_x / 2 + (coords.size_x / 2 * ((math.cos(coords.t * coords.p1_t + coords.p1_off)) * coords.p1_a))
            y = coords.size_y / 2 + (coords.size_y / 2 * ((math.sin(coords.t * coords.p2_t + coords.p2_off)) * coords.p2_a))
            table_x = coords.size_x/2 * coords.table_xa * math.cos(coords.t * coords.p3_t + coords.ptable_off)
            table_y = coords.size_y/2 * coords.table_ya * math.sin(coords.t * coords.p3_t + coords.ptable_off)
            x += table_x
            y += table_y
            return x, y
        
        def c1():
            x = coords.size_x / 2 + (coords.size_x / 2 * ((math.cos(coords.t * coords.p1_t + coords.p1_off)) * coords.p1_a * math.cos(1.02*coords.t * coords.p1_t)))
            y = coords.size_y / 2 + (coords.size_y / 2 * ((math.sin(coords.t * coords.p2_t + coords.p2_off)) * coords.p2_a * math.sin(0.999*coords.t * coords.p2_t)))
            table_x = coords.size_x/2 * coords.table_xa * math.cos(coords.t * coords.p3_t + coords.ptable_off)
            table_y = coords.size_y/2 * coords.table_ya * math.sin(coords.t * coords.p3_t + coords.ptable_off)
            x += table_x
            y += table_y
            return x, y
        
        def c2():
            x = coords.size_x / 2 + (coords.size_x / 2 * ((math.cos(coords.t * coords.p1_t + coords.p1_off) + 0.3*math.cos(-1.02*coords.t * coords.p1_t + coords.p1_off)) * coords.p1_a))
            y = coords.size_y / 2 + (coords.size_y / 2 * ((math.sin(coords.t * coords.p2_t + coords.p2_off) + 0.3*math.sin(1.04*coords.t * coords.p2_t + coords.p2_off)) * coords.p2_a))
            table_x = coords.size_x/2 * coords.table_xa * math.cos(coords.t * coords.p3_t + coords.ptable_off)
            table_y = coords.size_y/2 * coords.table_ya * math.sin(coords.t * coords.p3_t + coords.ptable_off)
            x += table_x
            y += table_y
            return x, y
 
        def c3():
            x = coords.size_x / 2 + (coords.size_x / 2 * ((math.cos(coords.t * coords.p1_t + coords.p1_off) + 0.3*math.cos(2*coords.t * coords.p1_t)) * coords.p1_a))
            y = coords.size_y / 2 + (coords.size_y / 2 * ((math.sin(coords.t * coords.p2_t + coords.p2_off) )) * coords.p2_a)
            table_x = coords.size_x/2 * coords.table_xa * math.cos(coords.t * coords.p3_t + coords.ptable_off)
            table_y = coords.size_y/2 * coords.table_ya * math.sin(coords.t * coords.p3_t + coords.ptable_off)
            x += table_x
            y += table_y
            return x, y
  
        def color0():
            rgb1 = (255,0,0)
            rgb2 = (0,200,0)
            rgb3 = (0,0,250)
            rgb = [math.pow((1 - coords.t/coords.timeout),2) * rgb1[i] + 2*(1 - coords.t/coords.timeout)*(coords.t/coords.timeout) * rgb2[i] + math.pow(coords.t/coords.timeout,2)*rgb3[i] for i in range(3)]
            return rgb
 
        def color1():
            rgb1 = (255,60,40)
            rgb2 = (255,200,0)
            rgb3 = (0,100,100)
            rgb = [math.pow((1 - coords.t/coords.timeout),3) * rgb1[i] + 3*math.pow(1 - coords.t/coords.timeout,2)*(coords.t/coords.timeout) * rgb2[i] + 3*math.pow(coords.t/coords.timeout,2)*(1-coords.t/coords.timeout) * rgb3[i] + math.pow(coords.t/coords.timeout,3)*rgb1[i] for i in range(3)]
            return rgb
 
        def color2():
            rgb1 = (100+ math.sin(coords.t)*100,0,100+math.sin(coords.t+math.pi)*100)
            rgb2 = (100,100, 100 + math.sin(coords.t)*100)
            rgb3 = (30+math.sin(coords.t)*30,80+math.sin(coords.t + math.pi)* 80, 0)
            rgb = [math.pow((1 - coords.t/coords.timeout),3) * rgb1[i] + 3*math.pow(1 - coords.t/coords.timeout,2)*(coords.t/coords.timeout) * rgb2[i] + 3*math.pow(coords.t/coords.timeout,2)*(1-coords.t/coords.timeout) * rgb3[i] + math.pow(coords.t/coords.timeout,3)*rgb1[i] for i in range(3)]
            return rgb
 
        color_d = {0: color0, 1: color1, 2: color2}
        c_d = {0: c0, 1: c1, 2: c2, 3: c3}
        return c_d, color_d
