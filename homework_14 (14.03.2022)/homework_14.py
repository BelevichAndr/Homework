from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine("sqlite:///homework.db")

Base = declarative_base()


class Group(Base):
    __tablename__ = "Group"

    id = Column(Integer, primary_key=True)
    name = Column(String)


class Student(Base):
    __tablename__ = "Student"

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    group_id = Column(Integer, ForeignKey("Group.id"))
    group = relationship("Group")


class Diary(Base):
    __tablename__ = "Diary"

    id = Column(Integer, primary_key=True)
    average_marks = Column(Float)
    student_id = Column(Integer, ForeignKey("Student.id"))
    student = relationship("Student")


association_table = Table("association", Base.metadata,
                          Column('id', Integer, primary_key=True),
                          Column("book_id", Integer, ForeignKey("Book.id")),
                          Column("student_id", Integer, ForeignKey("Student.id")),
                          )


class Book(Base):
    __tablename__ = "Book"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    pages_count = Column(Integer)
    student = relationship("Student", secondary=association_table)


Base.metadata.create_all(engine)

DBSession = sessionmaker(bind=engine)
session = DBSession()


group1 = Group(name="python")
group2 = Group(name="java")

student1_1 = Student(first_name="Andrei", last_name="Belevich", group_id=1)
student1_2 = Student(first_name="Vlad", last_name="Bulat", group_id=1)
student1_3 = Student(first_name="Valentin", last_name="Grakovich", group_id=1)
student2_1 = Student(first_name="Yolya", last_name="Yorusova", group_id=2)
student2_2 = Student(first_name="Ivan", last_name="Stefanenko", group_id=2)
student2_3 = Student(first_name="Dmitriy", last_name="Zharikov", group_id=2)
student_list = [student1_1, student1_2, student1_3, student2_1, student2_2, student2_3]

diary1_1 = Diary(average_marks=9.0, student_id=1)
diary1_2 = Diary(average_marks=8.5, student_id=2)
diary1_3 = Diary(average_marks=8.0, student_id=3)
diary2_1 = Diary(average_marks=9.0, student_id=4)
diary2_2 = Diary(average_marks=8.5, student_id=5)
diary2_3 = Diary(average_marks=8.0, student_id=6)
diary_list = [diary1_1, diary1_2, diary1_3, diary2_1, diary2_2, diary2_3]

book1 = Book(name="TruePython", pages_count=300)
book2 = Book(name="JavaSuperLanguage", pages_count=400)
book3 = Book(name="ClearProgramming", pages_count=500)
book4 = Book(name="Algorithms", pages_count=1000)
book5 = Book(name="REST", pages_count=100)
book_list = [book1, book2, book3, book4, book5]

session.add_all([group1, group2])
session.add_all(student_list)
session.add_all(diary_list)
session.add_all(book_list)
session.commit()

connection = engine.connect()


def writer_in_associations(book_id, student_id):
    insert_string = association_table.insert().values(book_id=book_id, student_id=student_id)
    connection.execute(insert_string)


writer_in_associations(1, 1)
writer_in_associations(1, 2)
writer_in_associations(2, 4)
writer_in_associations(2, 5)
writer_in_associations(3, 3)
writer_in_associations(3, 6)
writer_in_associations(3, 5)
writer_in_associations(4, 1)
writer_in_associations(5, 5)
