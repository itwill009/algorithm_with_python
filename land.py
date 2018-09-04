land = [[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]

answer = 0


for i in range(len(land)):

    for j in range(4):

        answer += land[i][j]
