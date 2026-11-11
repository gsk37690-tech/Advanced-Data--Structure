maze = [
    ['P', '.', 'X', '.', 'E'],
    ['X', '.', 'X', '.', 'X'],
    ['.', '.', '.', '.', 'X']
]

player_pos = [0, 0]

def print_maze(maze, player_pos):
    for i, row in enumerate(maze):
        row_out = ""
        for j, col in enumerate(row):
            if [i, j] == player_pos:
                row_out += "P "
            else:
                row_out += col + " "
        print(row_out)
    print()

while True:
    print_maze(maze, player_pos)
    move = input("Move (W/A/S/D): ").upper()
    next_pos = player_pos.copy()
    if move == 'W': next_pos[0] -= 1
    elif move == 'S': next_pos[0] += 1
    elif move == 'A': next_pos[1] -= 1
    elif move == 'D': next_pos[1] += 1
    else:
        print("Invalid input, try again.")
        continue

    if 0 <= next_pos[0] < len(maze) and 0 <= next_pos[1] < len(maze[0]):
        cell = maze[next_pos[0]][next_pos[1]]
        if cell == 'X':
            print("Hit an obstacle. Try again!")
        elif cell == 'E':
            print("Game Over! You Win!")
            break
        else:
            player_pos = next_pos
    else:
        print("Out of bounds, try again!")
