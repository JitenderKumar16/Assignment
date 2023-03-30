'''Given a 2D matrix of characters and a target word, write a function that returns whether the word can be found in the matrix by going left-to-right, or up-to-down.
For example, given the following matrix:
[['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]
and the target word 'FOAM', you should return true, since it's the leftmost column. Similarly, given the target word 'MASS', you should return true, since it's the last row.'''

def word_in_matrix(matrix, word):
    rows = len(matrix)
    cols = len(matrix)

    # Check rows
    for i in range(rows):
        row_str = "".join(matrix[i])
        if word in row_str:
            return True

    # Check columns
    for j in range(cols):
        col_str = "".join([matrix[i][j] for i in range(rows)])
        if word in col_str:
            return True

    # Word not found
    return False
