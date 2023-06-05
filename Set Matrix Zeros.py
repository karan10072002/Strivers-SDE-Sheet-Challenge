from typing import List

def setZeros(matrix: List[List[int]]) -> None:

    del_columns=[]
    zeroed_row =[]
    rows = len(matrix)
    columns = len(matrix[0])

    for i in range(rows):
        flag = 0
        for j in range(columns):
            if matrix[i][j] == 0:
                flag = 1
                del_columns.append(j)
        if flag == 1:
            matrix[i] = [0 for _ in range(columns)]
        else: 
            zeroed_row.append(i)

    for old_i in zeroed_row:
        for previous in del_columns:
            matrix[old_i][previous] = 0

    return matrix
