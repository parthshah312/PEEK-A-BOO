import random

# Function to initialize the grid with random pairs of integers
def initialize_grid(size):
    numbers = list(range(size*size//2)) * 2
    random.shuffle(numbers)
    grid = [[(0, True) for _ in range(size)] for _ in range(size)]
    for row in range(size):
        for col in range(size):
            grid[row][col] = (numbers[row*size+col], False)
    return grid

# Function to display the grid
def display_grid(grid):
    print("-----------------")
    print("|   PEEK-A-BOO   |")
    print("-----------------")

    size = len(grid)
    # Display column labels
    print(" ", end=" ")
    for col in range(size):
        print(chr(col + ord('A')), end=" ")
    print()
    # Display rows with grid contents
    for row in range(size):
        print(row, end=" ")
        for col in range(size):
            number, visible = grid[row][col]
            if visible:
                print(number, end=" ")
            else:
                print("X", end=" ")
        print()