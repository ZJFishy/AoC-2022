from time import sleep

def read_grid(filepath:str) -> list[list[str]]:
    grid = []

    for line in open(filepath):
        line_list = []
        for i in range(len(line)):
            if line[i] != "\n":
                line_list.append(line[i])
        grid.append(line_list)
    
    return grid

def find_start(grid:list[list[str]]) -> tuple[int, int]:
    for i in range(len(grid)):
        if "S" in grid[i]:
            return (i, grid[i].index("S"))
    return (-1, -1)
        
def iterate_search(height_grid:list[list[str]], last_visit_grid:list[list[bool]], visited_grid:list[list[bool]], grid_height:int, grid_width:int):
    current_visit_grid = [[False for i in range(grid_width)] for j in range(grid_height)]
    for row in range(grid_height):
        for col in range(grid_width):
            if last_visit_grid[row][col]:
                print(f"\tChecking around {(row, col)}")
                for row_offset, col_offset in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    if grid_height > row + row_offset >= 0 and grid_width > col + col_offset >= 0:
                        if not visited_grid[row+row_offset][col+col_offset]:
                            if height_grid[row][col] == "z" and height_grid[row+row_offset][col+col_offset] == "E":
                                return True
                            elif height_grid[row][col] == "S" and height_grid[row+row_offset][col+col_offset] == "a":
                                print(f"\t\tVisited {(row+row_offset, col+col_offset)}")
                                current_visit_grid[row+row_offset][col+col_offset] = True
                                visited_grid[row+row_offset][col+col_offset] = True
                            elif ord(height_grid[row+row_offset][col+col_offset]) - ord(height_grid[row][col]) <= 1 and height_grid[row+row_offset][col+col_offset] != "E":
                                print(f"\t\tVisited {(row+row_offset, col+col_offset)}")
                                current_visit_grid[row+row_offset][col+col_offset] = True
                                visited_grid[row+row_offset][col+col_offset] = True
    return current_visit_grid

if int(input("Enter the part number: ")) == 1:
    grid_in = read_grid("./day_12_input.txt")
    grid_height = len(grid_in)
    grid_width = len(grid_in[0])
    last_visit_grid = [[False for i in range(grid_width)] for j in range(grid_height)]
    visited_grid = [[False for i in range(grid_width)] for j in range(grid_height)]
    start_location = find_start(grid_in)
    last_visit_grid[start_location[0]][start_location[1]] = True
    visited_grid[start_location[0]][start_location[1]] = True
    step_number = 0

    while last_visit_grid != True:
        step_number += 1
        print(f"Iteration {step_number}:")
        last_visit_grid = iterate_search(grid_in, last_visit_grid, visited_grid, grid_height, grid_width)
        if not last_visit_grid:
            visited_grid += last_visit_grid
        sleep(0.1)

    print(step_number)

else:
    grid_in = read_grid("./day_12_input.txt")
    grid_height = len(grid_in)
    grid_width = len(grid_in[0])
    last_visit_grid = [[((grid_in[j][i] == "S")|(grid_in[j][i] == "a")) for i in range(grid_width)] for j in range(grid_height)]
    visited_grid = [[((grid_in[j][i] == "S")|(grid_in[j][i] == "a")) for i in range(grid_width)] for j in range(grid_height)]
    step_number = 0

    for row in visited_grid:
        for entry in row:
            print("X" if entry else ".", end="")
        print()

    while last_visit_grid != True:
        step_number += 1
        print(f"Iteration {step_number}:")
        last_visit_grid = iterate_search(grid_in, last_visit_grid, visited_grid, grid_height, grid_width)
        if last_visit_grid != True:
            for i in range(grid_height):
                for j in range(grid_width):
                    visited_grid[i][j] = last_visit_grid[i][j] | visited_grid[i][j]
                    # print("X" if visited_grid[i][j] else ".", end="")
                # print()
        # sleep(0.1)

    print(step_number)