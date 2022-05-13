import os
from threading import Thread
from multiprocessing import Process


def create_directory(directory_name: str):
    if not os.path.isdir(f"{directory_name}"):
        os.mkdir(f"{directory_name}")


def file_creator(directory: str, number: int):
    with open(f"{os.getcwd()}\{directory}\{number}.txt", "w", encoding="utf-8") as file:
        file.write(f"файл - {number}")


def default_variant(count: int):
    directory = "defoult"
    create_directory(directory)
    for i in range(1, count + 1):
        file_creator(directory, i)


def thread_variant(count: int):
    directory = "thread"
    create_directory(directory)
    threads = (Thread(target=file_creator, args=(directory, i)) for i in range(1, count+1))
    for thread in threads:
        thread.start()


def process_variant(count: int):
    directory = "process"
    create_directory(directory)
    processes = (Process(target=file_creator, args=(directory, i)) for i in range(1, count + 1))
    for process in processes:
        process.start()


if __name__ == "__main__":
    default_variant(10)
    thread_variant(10)
    process_variant(10)
