import random

# TASK 1 -----------------------------------------------------------------------------
name_list = ['Andrei', 'Misha', 'Anya', 'Alesya', 'Natasha']


def hello(name):
    print(f'Hello {name}')


for name in name_list:
    hello(name)
print('--------------------------------')

# TASK 2 -----------------------------------------------------------------------------

main_matrix = []


def matrix_init(matrix):
    count_str = int(input('Input count matrix string: '))
    count_columns = int(input('Input count matrix columns: '))
    for i in range(1, count_str + 1):
        work_list = []
        for j in range(1, count_columns + 1):
            value = int(input(f'Input value{i}{j}: '))
            work_list.append(value)
        matrix.append(work_list)
    return matrix


def matrix_print(matrix):
    for row in matrix:
        print(*row)


def matrix_total_sum(matrix):
    total_sum = 0
    for string in matrix:
        string_sum = sum(string)
        total_sum += string_sum
    print(f'Total element summ is: {total_sum}')
    return total_sum


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


matrix_init(main_matrix)
matrix_print(main_matrix)
matrix_total_sum(main_matrix)
matrix_max_elem(main_matrix)
matrix_min_elem(main_matrix)
print('--------------------------------')


# TASK 3 -----------------------------------------------------------------------------


def factorial(n):
    result = 1
    if n < 0:
        print('factorial is not defined for n < 0')
        return
    elif n == 0:
        print(f'factorial = {result}')
        return result
    else:
        for i in range(1, n + 1):
            result *= i
        print(f'factorial = {result}')
        return result


factorial(5)
factorial(-5)
factorial(0)
print('-----------------------------------------------------')


# TASK 4 --------------------------------------------------------------------------

def matrix_for_task_4(n, random_from=1, random_to=9):
    #   in parameter 'n' input the size of the matrix in the form: 'n,m'
    #   where n - count matrix strings
    #         m - count matrix columns
    matrix = []
    work_list = n.split(',')
    count_str = int(work_list[0])
    count_columns = int(work_list[1])
    for i in range(1, count_str + 1):
        work_list = []
        for j in range(1, count_columns + 1):
            value = random.randint(random_from, random_to)
            work_list.append(value)
        matrix.append(work_list)
    return matrix


matrix_print(matrix_for_task_4('5,5'))
print('--------------------------------------------------------------------')


# TASK 5 -----------------------------------------------------------------------


def sum_elements(*args):
    total_sum = 0
    count_args = len(args)
    for i in range(count_args):
        total_sum += args[i] * i
    return total_sum


print(f'Args total sum = {sum_elements(6, 7, 3, 5, 6)}')
print('-------------------------------------------------------------------------')


# TASK 6 -------------------------------------------------------------------------


def sum_and_max_args(*args):
    total_sum = 0
    max_element = max(args)
    for i in range(len(args)):
        total_sum += args[i]
    return total_sum, max_element


print(f'TASK 6: {sum_and_max_args(5, 7, 8, 9, 4, 2, 45, 63, 14, 5)}')
print('----------------------------------------------------------------------------')


# TASK 7 -------------------------------------------------------------------------------


def kwargs_function(**kwargs):
    for key, value in kwargs.items():
        if type(value) == type(1):
            work_value = str(value)
            if not len(work_value) % 2:
                print(key, value)
        else:
            if not len(value) % 2:
                print(key, value)


kwargs_function(a=5555, b='asfasf', c=123)
print('----------------------------------------------------------------------------------')


# TASK 8-----------------------------------------------------------------------------------


def foo(mean_type, *args):
    if mean_type == 'ARIFM':
        avg_arifm(args)
    elif mean_type == 'GEOM':
        avg_geom(args)


def avg_arifm(args):
    total_sum = 0
    count = len(args)
    for arg in args:
        total_sum += arg
    result = total_sum / count
    print(f'Среднее арифметическое: {result}')


def avg_geom(args):
    total_geom = 1
    count = len(args)
    for arg in args:
        total_geom *= arg
    result = total_geom / count
    print(f'Среднее геометрическое: {result}')


foo('ARIFM', 5, 5, 10)
