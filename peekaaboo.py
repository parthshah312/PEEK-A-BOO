import random
import time

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

# Function to handle option 1: Guessing a pair of cells
def guess_pair(grid):
    size = len(grid)
    # Get first cell coordinates
    while True:
        cell1 = input("Enter the coordinates of the first cell (e.g., A0): ")
        if validate_cell(cell1, size):
            break
        else:
            print("Invalid cell. Try again.")
    # Get second cell coordinates
    while True:
        cell2 = input("Enter the coordinates of the second cell (e.g., B1): ")
        if validate_cell(cell2, size) and cell1 != cell2:
            break
        else:
            print("Invalid cell. Try again.")
    # Extract row and column values from cell coordinates
    row1, col1 = convert_cell(cell1)
    row2, col2 = convert_cell(cell2)
    # Reveal the numbers in the selected cells
    number1, visible1 = grid[row1][col1]
    number2, visible2 = grid[row2][col2]
    grid[row1][col1] = (number1, True)
    grid[row2][col2] = (number2, True)
    # Display the updated grid
    display_grid(grid)
    # Compare the numbers in the selected cells
    if number1 == number2:
        print("You found a pair!")
        return True
    else:
        print("Not a match.")
        # Hide the numbers after a short delay
        time.sleep(2)
        grid[row1][col1] = (number1, False)
        grid[row2][col2] = (number2, False)
        return False

# Function to handle option 2: Manually reveal a cell
def reveal_cell(grid):
    size = len(grid)
    # Get the cell coordinates to reveal
    while True:
        cell = input("Enter the coordinates of the cell to reveal (e.g., C2): ")
        if validate_cell(cell, size):
            break
        else:
            print("Invalid cell. Try again.")
    # Extract row and column values from cell coordinates
    row, col = convert_cell(cell)
    # Reveal the number in the selected cell
    number, visible = grid[row][col]
    grid[row][col] = (number, True)
    # Display the updated grid
    display_grid(grid)

def reveal_game(grid):
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
            print(number, end=" ")
        print()

# Function to validate cell coordinates
def validate_cell(cell, size):
    if len(cell) != 2:
        return False
    col = cell[0].upper()
    row = cell[1]
    return col.isalpha() and col.isupper() and col >= 'A' and col < chr(ord('A') + size) and row.isdigit() and int(row) >= 0 and int(row) < size

# Function to convert cell coordinates to row and column values
def convert_cell(cell):
    col = cell[0].upper()
    row = int(cell[1])
    return row, ord(col) - ord('A')

# Function to calculate the score
def calculate_score(min_guesses, actual_guesses):
    if actual_guesses == 0:
        return 0
    else:
        return (min_guesses / actual_guesses) * 100
    

# Main game loop
def play_game(size):
    grid = initialize_grid(size)
    display_grid(grid)
    min_guesses = size * size // 2
    actual_guesses = 0

    while True:
        print("Menu Options:")
        print("1. Guess a pair of cells")
        print("2. Reveal a cell")
        print("3. Give up - Reveal the grid")
        print("4. Start a new game")
        print("5. Quit")
        option = input("Enter your choice (1-5): ")

        if option == "1":
            success = guess_pair(grid)
            actual_guesses += 1
            if success:
                min_guesses -= 1
        elif option == "2":
            reveal_cell(grid)
            actual_guesses += 2
        elif option == "3":
            print("You gave up!")
            reveal_game(grid)
            break
        elif option == "4":
            play_game(size)
            break
        elif option == "5":
            print("Thanks for playing!")
            break
        else:
            print("Invalid option. Try again.")

        # Check if all pairs have been found
        if min_guesses == 0:
            score = calculate_score(size * size // 2, actual_guesses)
            print("Congratulations! You found all pairs!")
            print(f"Your score is: {score:.1f}")
            break

# Start the game
if __name__ == "__main__":
    size = int(input("Enter the size of the grid (2, 4, or 6): "))
    if size in [2, 4, 6]:
        play_game(size)
    else:
        print("Invalid grid size. The size must be 2, 4, or 6.")
