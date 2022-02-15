def main():
    with open('text.txt', 'a') as my_file:
        my_file.writelines([input('Input first string: ') + '\n',
                            input('Input second string: ') + '\n',
                            input('Input third string: ') + '\n'])


if __name__ == '__main__':
    main()
