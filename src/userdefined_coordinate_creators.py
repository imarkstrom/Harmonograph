# Author: Ingemar Markström
# This file wont be touched (heh, oh yes, but probably only when big changes occur)
# Add your own coord generators and color generators.
import math

class USER_COORDS_FUNCTIONS:
    def fetch_functions(coords):
        def c0():
            x = coords.size_x / 2 + (coords.size_x / 2 * ((math.cos(coords.t * coords.p1_t + coords.p1_off)) * coords.p1_a))
            y = coords.size_y / 2 + (coords.size_y / 2 * ((math.sin(coords.t * coords.p2_t + coords.p2_off)) * coords.p2_a))
            table_x = coords.size_x/2 * coords.table_xa * math.cos(coords.t * coords.p3_t + coords.ptable_off)
            table_y = coords.size_y/2 * coords.table_ya * math.sin(coords.t * coords.p3_t + coords.ptable_off)
            x += table_x
            y += table_y
            return x, y
        
        def color0():
            rgb1 = (100+ math.sin(coords.t)*100,0,100+math.sin(coords.t+math.pi)*100)
            rgb2 = (100,100, 100 + math.sin(coords.t)*100)
            rgb3 = (30+math.sin(coords.t)*30,80+math.sin(coords.t + math.pi)* 80, 0)
            rgb = [math.pow((1 - coords.t/coords.timeout),3) * rgb1[i] + 3*math.pow(1 - coords.t/coords.timeout,2)*(coords.t/coords.timeout) * rgb2[i] + 3*math.pow(coords.t/coords.timeout,2)*(1-coords.t/coords.timeout) * rgb3[i] + math.pow(coords.t/coords.timeout,3)*rgb1[i] for i in range(3)]
            return rgb
 
        coord_functions = {0: c0}
        color_functions = {0: color0}
        return coord_functions, color_functions
