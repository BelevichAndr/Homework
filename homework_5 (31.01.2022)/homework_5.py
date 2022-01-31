def main_menu():
    print('Choose function ([S]um or [M]ult).'
          'If you want to finish program input - [E]xit')
    answer = input('Your answer: ')
    if answer.lower() == 's' or answer.lower() == 'sum':
        sum_arg()
    elif answer.lower() == 'm' or answer.lower() == 'mult':
        multiplication_arg()
    elif answer.lower() == 'e' or answer.lower() == 'exit':
        exit_program()


def sum_arg():
    total_sum = 0
    print('You in a sum function. If you want to exit input [E]xit')
    while True:
        value = input('Input value: ')
        if value.lower() == 'e' or value.lower() == 'exit':
            exit_program()
            break
        value = int(value)
        total_sum += value
        print(f'current sum is: {total_sum}')


def multiplication_arg():
    total_mult = 1
    print('You in a multiplication function. If you want to exit input [E]xit')
    while True:
        value = input('Input value: ')
        if value.lower() == 'e' or value.lower() == 'exit':
            exit_program()
            break
        value = int(value)
        total_mult *= value
        print(f'current multiplication is: {total_mult}')


def exit_program():
    answer = input('Do you want to [F]inish program or [C]hoose function? ')
    if answer.lower() == 'c' or answer.lower() == 'choose':
        main_menu()


main_menu()
