def get_magic_triangle(n):
    result = []
    for cur_row_idx in range(n):
        result.append([1])
        for internal_idx in range(1, cur_row_idx):
            internal_sum = result[cur_row_idx - 1][internal_idx - 1] + result[cur_row_idx - 1][internal_idx]
            result[cur_row_idx].append(internal_sum)
        if cur_row_idx != 0:
            result[cur_row_idx].append(1)
    return result


get_magic_triangle(5)