from random import randint
from time import sleep, time
import argparse
import csv
time_now = time()


def my_generator(a=1, b=10, diff=10):
    while True:
        yield randint(a, b)
        sleep(0.2)
        a += diff
        b += diff


for i in my_generator(100, 200, 100):
    print(i)
    if time() - time_now > 2:
        break

# Use this commands:
# cd '.\homework_12 (28.02.2022)\'
# python homework_12.py -fn Andrei -ln Belevich -age 21

parser = argparse.ArgumentParser()

parser.add_argument("-fn", required=True)
parser.add_argument("-ln", required=True)
parser.add_argument("-age", required=True)

args = parser.parse_args()

data = [args.fn, args.ln, args.age]
fields = ["first_name", "last_name", "age"]
file_name = "homework_12.csv"

with open(file_name, "w") as file:
    writer = csv.writer(file)
    writer.writerow(fields)
    writer.writerow(data)
