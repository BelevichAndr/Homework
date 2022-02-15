def main():
    with open('text.txt') as my_file:
        text = my_file.readlines()
        print(text[0], end='') #TASK 1
        print(text[4], end='') #TASK 2
        generator = [print(string, end='') for string in text[0:5]] #TASK 3
        s1 = int(input('Input "S1" string: '))
        s2 = int(input('Input "S2" string: '))
        generator = [print(string, end='') for string in text[s1-1:s2]] #TASK 4
        generator = [print(string, end='') for string in text] #TASK 5


if __name__ == '__main__':
    main()
