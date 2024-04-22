import numpy as np

initial_board = np.array([
    [1, 1, 2, 1, 0],
    [1, -1, 0, -1, 1],
    [0, 3, 0, 0, 2],
    [-1, -1, 0, -1, 1],
    [-1, 3, 0, 1, 0]
])
indices = np.where(initial_board < 1)
a, b = indices[0], indices[1]
a = a.reshape((len(a), 1))
b = b.reshape((len(a), 1))
hidden_positions = np.hstack((a,b))
numbers_of_moves = len(hidden_positions)

for i in range(numbers_of_moves):
    initial_board[hidden_positions[i][0]][hidden_positions[i][1]] += 5
    if(initial_board[hidden_positions[i][0]][hidden_positions[i][1]] == 4):
        initial_board[hidden_positions[i][0]][hidden_positions[i][1]] -= 5
    print(initial_board)
