def main():
    with open('text.txt') as my_file:
        text1 = my_file.readlines()

    with open('text2.txt') as my_file:
        text2 = my_file.readlines()

    if text1 == text2:
        print('match')
    else:
        for string_number in range(len(text1)):
            if text1[string_number] != text2[string_number]:
                print(f'{string_number + 1} - first string where files dont match')
                break


if __name__ == '__main__':
    main()
