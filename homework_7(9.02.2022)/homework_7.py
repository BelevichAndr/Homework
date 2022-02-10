#TASK 1---------------------------------------------------------------------
def generate_list():
    string_list = ['That which does not kill us makes us stronger.',
                   'In the middle of every difficulty lies opportunity.',
                   'Better to remain silent and be thought a fool than to speak out and remove all doubt.',
                   'You must be the change you wish to see in the world.',
                   'An eye for an eye leaves the whole world blind.']

    formatted_list = [f'{string_number + 1} - {string_list[string_number]}'
                      for string_number in range(len(string_list))]
    print(formatted_list)


#TASK 2---------------------------------------------------------------------
def generate_lambda_dict():
    lambda_function = lambda **kwargs: {key*2: value for key, value in kwargs.items()}
    print(lambda_function(Andrei=5149017, Olga=6133524))


#TASK 3--------------------------------------------------------------------
def decorator_task_3(function):
    def wrapper(*args):
        work_list = function(*args)
        odd_numbers_list = [number for number in work_list if number % 2]
        print(odd_numbers_list)
        return odd_numbers_list
    return wrapper

@decorator_task_3
def function_for_decorator_task_3(list_of_numbers):
    sorted_list = sorted(list_of_numbers)
    print(sorted_list)
    return sorted_list


#TASK 4-------------------------------------------------------------------------------
def universal_decorator(function):
    def wrapper(*args):
        function(*args[::-1])
    return wrapper


@universal_decorator
def function_for_decorator_task_4(first_name, last_name, age):
    print(f'First_name is: {first_name}')
    print(f'Last_name is: {last_name}')
    print(f'Age is: {age}')


#MAIN--------------------------------------------------------------------------------
def main():
    generate_list()
    generate_lambda_dict()

    example_list = [1, 6, 7, 9, 2, 5, 7, 8, 1]
    function_for_decorator_task_3(example_list)

    function_for_decorator_task_4('Andrei', 'Belevich', 21)


if __name__ == '__main__':
    main()
