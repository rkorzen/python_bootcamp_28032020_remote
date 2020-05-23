

def add_matrices(a: list, b: list) -> list:
    out = []
    # for i, row in enumerate(a):
    #     n_row = []
    #     for j, col in enumerate(row):
    #         n_row.append(col + b[i][j])
    #     out.append(n_row)
    # for row_a, row_b in zip(a, b):
    #     row = []
    #     for col_a, col_b in zip(row_a, row_b):
    #         row.append(col_a + col_b)
    #     out.append(row)
    out = [[col_a + col_b for col_a, col_b in zip(row_a, row_b)] for row_a, row_b in zip(a, b)]
    return out

def sub_matrices(a, b):
    out = []
    for i, row in enumerate(a):
        n_row = []
        for j, col in enumerate(row):
            n_row.append(col - b[i][j])
        out.append(n_row)

    return out
