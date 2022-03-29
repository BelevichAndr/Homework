from flask_sqlalchemy import SQLAlchemy, inspect
from flask import Flask, render_template,  request
from sqlalchemy_utils import database_exists, create_database

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///homework.db"

db = SQLAlchemy(app)


class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    group_id = db.Column(db.Integer, db.ForeignKey("group.id"))


class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))


class Diary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    average_marks = db.Column(db.Float)
    student_id = db.Column(db.Integer, db.ForeignKey("students.id"))


association_table = db.Table("association", db.metadata,
                             db.Column('id', db.Integer, primary_key=True),
                             db.Column("book_id", db.Integer, db.ForeignKey("book.id")),
                             db.Column("student_id", db.Integer, db.ForeignKey("students.id")),
                             )


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    pages_count = db.Column(db.Integer)


if not database_exists(db.engine.url):
    create_database(db.engine.url)
    db.init_app(app)
    db.create_all()


@app.route("/")
def main():
    return render_template("main.html", title="Главная")


@app.route("/student", methods=["POST", "GET"])
def student():
    if request.method == "POST":
        try:
            write_student = Students(first_name=request.form["first_name"],
                                     last_name=request.form["last_name"],
                                     group_id=request.form["group_id"])
            db.session.add(write_student)
            db.session.flush()
            db.session.commit()
        except:
            db.session.rollback()
            print("Ошибка доабвления в БД")
    return render_template("student.html", title="Студент")


@app.route("/group", methods=["POST", "GET"])
def group():
    if request.method == "POST":
        try:
            write_group = Group(name=request.form["name"])
            db.session.add(write_group)
            db.session.flush()
            db.session.commit()
        except:
            db.session.rollback()
            print("Ошибка доабвления в БД")
    return render_template("group.html", title="Группа")


@app.route("/diary", methods=["POST", "GET"])
def diary():
    if request.method == "POST":
        try:
            write_diary = Diary(average_marks=request.form["average_marks"],
                                student_id=request.form["student_id"])
            db.session.add(write_diary)
            db.session.flush()
            db.session.commit()
        except:
            db.session.rollback()
            print("Ошибка доабвления в БД")
    return render_template("diary.html", title="Дневник")


@app.route("/book", methods=["POST", "GET"])
def book():
    if request.method == "POST":
        try:
            write_book = Book(name=request.form["name"],
                               pages_count=request.form["pages_count"])
            db.session.add(write_book)
            db.session.flush()
            db.session.commit()
        except:
            db.session.rollback()
            print("Ошибка доабвления в БД")
    return render_template("book.html", title="Книга")


@app.route("/library", methods=["POST", "GET"])
def library():
    if request.method == "POST":
        try:
            connection = db.engine.connect()
            insert_string = association_table.insert().values(book_id=request.form["book_id"],
                                                              student_id=request.form["student_id"])
            connection.execute(insert_string)
        except:
            db.session.rollback()
            print("Ошибка доабвления в БД")
    return render_template("library.html", title="Книга")


if __name__ == "__main__":
    app.run(debug=True)
