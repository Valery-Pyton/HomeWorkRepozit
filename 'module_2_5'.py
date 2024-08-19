def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix_1 = []
        matrix.append(matrix_1)
        for j in range(m):
            matrix_1.append(value)
    print(matrix, '\n')

    def upgrade1_draw_matrix(matrix):
        print('\n', 'Матричный вар-т написания матрицы')
        for k in matrix:
            print(k)

    upgrade1_draw_matrix(matrix)

    def upgrade2_draw_matrix(matrix):
        print('\n', 'Распакованный матричный вар-т написания матрицы')
        for k in matrix:
            print(*k)

    upgrade2_draw_matrix(matrix)
    return matrix


get_matrix(4, 4, 1)
get_matrix(10, 10, 10)
get_matrix(2, 2, 2)