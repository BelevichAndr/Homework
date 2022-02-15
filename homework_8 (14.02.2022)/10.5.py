def main():
    with open('text.txt') as my_file:
        text = my_file.readlines()
        text_for_file_2 = [string for string in text if text.index(string) % 2]
        text_for_file_3 = [string for string in text if text.index(string) % 2 == 0]
        print(text_for_file_2)
        print(text_for_file_3)

    with open('text2.txt', 'w') as my_file:
        my_file.writelines(text_for_file_2)

    with open('text3.txt', 'w') as my_file:
        my_file.writelines(text_for_file_3)


if __name__ == '__main__':
    main()
