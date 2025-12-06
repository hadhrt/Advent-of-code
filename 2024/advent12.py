import timeit
from dataclasses import dataclass

@dataclass
class Region():
    plots: set
    value: str
    area: int
    perimeter: int
    
    

def get_regions(lines):
    ADJ = (complex(-1,0),complex(1,0),
           complex(0,-1),complex(0,1))

    grid = {}
    for row,line in enumerate(lines):
        for col,val in enumerate(line):
            grid[complex(row,col)] = val

    starting_plot_queue = set(grid.keys())
    visited_plots = set()
    regions = []
    
    while starting_plot_queue:
        starting_plot = starting_plot_queue.pop()
        if starting_plot in visited_plots:
            continue

        val = grid.get(starting_plot)
        region = set()
        perimeter = 0
        region_plot_queue = set([starting_plot])
        while region_plot_queue:
            current_plot = region_plot_queue.pop()
            visited_plots.add(current_plot)
            region.add(current_plot)
            fences = 4
            for new_plot in [current_plot + adj for adj in ADJ]:
                # plot already in region
                if new_plot in region:
                    fences -= 1
                # plot has to be added to region
                elif grid.get(new_plot) == val:
                    fences -= 1
                    region_plot_queue.add(new_plot)
                # plot is of another type or outside of grid
                else:
                    pass
            perimeter += fences
                    
        regions.append(Region(plots=region, value=val, area= len(region), perimeter=perimeter))



    return regions



def count_corners(region:Region):
    corners = 0
    for plot in region.plots:
        # Key insight is that each corner also adds exactly one additional side
        # check for corners in each diagonal direction
        # for examples down right corner:
        #  A     B     C
        # ...   ...   ...  
        # .X.=1 .XX=1 .X.=1
        # ...   .X.   ..X
        # all other configuration = 0 additional corners

        for diag_offset in (complex(-1,-1), complex(-1,1),complex(1,-1),complex(1,1)):
            diag = plot + diag_offset
            adj1 = plot + complex(diag_offset.real,0) 
            adj2 = plot + complex(0,diag_offset.imag)
            # Case A
            if   diag not in region.plots and adj1 not in region.plots and adj2 not in region.plots:
                corners +=1
            # Case B
            elif diag not in region.plots and adj1     in region.plots and adj2     in region.plots:
                corners +=1
            # Case C
            elif diag     in region.plots and adj1 not in region.plots and adj2 not in region.plots:
                corners +=1
    return corners
    
    
def p1(lines):
    regions = get_regions(lines)
    return sum([region.perimeter * region.area for region in regions])
    

def p2(lines):
    regions = get_regions(lines)
    price = 0
    for region in regions:
        price += count_corners(region) * region.area
    return price

f = open("input12.txt", "r")
lines = [line.strip() for line in f]
  
start = timeit.default_timer()
print (f"Part 1: {p1(lines)}")
stop = timeit.default_timer()
print(f'Time: {(stop - start):.4}')

start = timeit.default_timer()
print (f"Part 2: {p2(lines)}")
stop = timeit.default_timer()
print(f'Time: {(stop - start):.4}')