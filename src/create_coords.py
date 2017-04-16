import math

class COORDS_FUNCTIONS:
    def fetch_functions(coords, version):
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
            x = coords.size_x / 2 + (coords.size_x / 2 * ((math.cos(coords.t * coords.p1_t + coords.p1_off)*math.sin(coords.t * coords.p1_t + coords.p1_off) * coords.p1_a)))
            y = coords.size_y / 2 + (coords.size_y / 2 * ((math.sin(coords.t * coords.p2_t + coords.p2_off)*math.cos(coords.t * coords.p2_t + coords.p2_off) * coords.p2_a)))
            table_x = coords.size_x/2 * coords.table_xa * math.cos(coords.t * coords.p3_t + coords.ptable_off)
            table_y = coords.size_y/2 * coords.table_ya * math.sin(coords.t * coords.p3_t + coords.ptable_off)
            x += table_x
            y += table_y
            return x, y
 

        
        c_d = {0: c0, 1: c1, 2: c2}
        
        return c_d[version]
