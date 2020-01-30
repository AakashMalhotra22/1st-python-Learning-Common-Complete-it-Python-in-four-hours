# Type -I Mix


number_grid = [
    [1,2,3],
    ["r","s","t"],
    [True, False],
    [0]

]

print(number_grid)

print(number_grid[2])
print(number_grid[2][1])

for col in number_grid:
    for row in col:
        print(row)

print("                                                                                                             ")

for row in number_grid:
    for col in row:
        print(col)