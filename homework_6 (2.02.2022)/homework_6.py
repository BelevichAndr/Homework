def main():
    words = ['Топот', 'Анна', 'Бумеранг']
    for word in words:
        if word.lower() == word[::-1].lower():
            print(word)


if __name__ == '__main__':
    main()
