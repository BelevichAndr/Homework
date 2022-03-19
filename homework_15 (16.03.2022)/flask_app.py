import json
from datetime import datetime
from flask import Flask, render_template, request

app = Flask(__name__)

now = str(datetime.now())


@app.route("/")
def hello_world():
    return now


@app.route("/two_pow/<float:number>")
def two_pow(number):
    return f"<h1>2 to the power of {number} is equal to {pow(2, number)}</h1>"


@app.route("/my_word/<path:word>")
def my_word(word):
    if len(word) % 2 == 0:
        return f"<h1>{word[::2]}</h1>"
    return f"<h1>{word}</h1>"


@app.route("/login", methods=["POST", "GET"])
def login():
    work_dict = {}

    for value in request.form:
        work_dict[value] = request.form[value]

    with open("data.json", "w", encoding="utf8") as file:
        json.dump(work_dict, file, ensure_ascii=False, indent=2)

    return render_template("18.03.html")


if __name__ == '__main__':
    app.run()
