
arr = [
    [1, 3, 7],
    [2, 9, 4],
    [0, 6, 8]
]

# je veux le sum de a=1 + 3 + 2 + 9 , b=3 + 7 + 9 + 4 puis c=2 + 9 + 0 + 6, d=9 + 4 + 6 + 8
# [[a, b], [c, d]]
# [[15, 23], [17, 27]]

def sumGrid(grid: list):
    result = []
    for i in range(len(grid) - 1):
        # parcourir les lignes de grid sauf la dernière (-1)
        row = []
        for j in range(len(grid[0]) - 1):
            # parcorir les colonnes de grid sauf la dernière (-1)
            print(grid[i][j], grid[i][j+1], grid[i+1][j], grid[i+1][j+1])
            somme = grid[i][j] + grid[i][j+1] + grid[i+1][j] + grid[i+1][j+1]
            row.append(somme)
        result.append(row)
    return result

print(sumGrid(arr))