### Minesweeper ###

"""

Write a function that will take 2 arguments:
bombs = a list of bomb locations
rows, columns
Ex. mine_sweeper([0,0], [0,1], 3, 4)

returns an 3 x 4 array
with cells filled with number meaning the number of bombs surrounding it
(-1) = bomb
Ex. returns
[[-1,-1,1,0],
[2,2,1,0],
[0,0,0,0]]

"""


def mine_sweeper(bombs, rows, cols):
    field = [[0 for a in range(cols)] for b in range(rows)]
    for bomb in bombs:
        r = bomb[0]
        c = bomb[1]
        field[r][c] = -1
        for j in range(-1, 2):
            for k in range(-1, 2):
                if [r + j, c + k] in bombs or r + j < 0 or c + k < 0 or (j == 0 and k == 0):
                    continue
                field[r + j][c + k] += 1

    return field


print(mine_sweeper([[0, 0], [0, 1]], 3, 4))
