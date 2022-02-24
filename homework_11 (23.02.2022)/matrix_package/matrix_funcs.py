def matrix_max_elem(matrix):
    total_max = matrix[0][0]
    for string in matrix:
        string_max = max(string)
        if string_max > total_max:
            total_max = string_max
    print(f'The biggest number in matrix is: {total_max}')
    return total_max


def matrix_min_elem(matrix):
    total_min = matrix[0][0]
    for string in matrix:
        string_min = min(string)
        if string_min < total_min:
            total_min = string_min
    print(f'The smallest number in matrix is: {total_min}')
    return total_min


def matrix_total_sum(matrix):
    total_sum = 0
    for string in matrix:
        string_sum = sum(string)
        total_sum += string_sum
    print(f'Total element summ is: {total_sum}')
    return total_sum