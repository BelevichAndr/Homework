# classic
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData
from sqlalchemy.sql import and_
meta = MetaData()

users = Table("Users", meta,
              Column('user_id', Integer, primary_key=True),
              Column('first_name', String),
              Column('last_name', String),
              Column('age', Integer)
              )

engine = create_engine("sqlite:///classic.db", pool_pre_ping=True)
meta.create_all(engine)

connection = engine.connect()

for i in range(5):
    print(f"String {i+1}")
    input_first_name = input("Input fist name: ")
    input_last_name = input("Input last name: ")
    input_age = int(input("Input age: "))
    insert_string = users.insert().values(first_name=input_first_name,
                                          last_name=input_last_name,
                                          age=input_age)
    connection.execute(insert_string)

find_name = input("Input name which you want to find: ")
get_info = users.select().where(users.c.first_name == find_name)
result = connection.execute(get_info)
for row in result:
    print(row)

print()

get_info = users.select().where(users.c.age < 25)
result = connection.execute(get_info)
for row in result:
    print(row)

print()

get_info = users.select().where(and_(users.c.age > 15, users.c.age < 18))
result = connection.execute(get_info)
for row in result:
    print(row)

# declarative


from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///declarative.db")

Base = declarative_base()


class Users(Base):
    __tablename__ = "Users"

    user_id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    age = Column(Integer)


Base.metadata.create_all(engine)

DBSession = sessionmaker(bind=engine)
session = DBSession()

for i in range(5):
    print(f"String {i+1}")
    input_first_name = input("Input fist name: ")
    input_last_name = input("Input last name: ")
    input_age = int(input("Input age: "))
    new_user = Users(first_name=input_first_name,
                     last_name=input_last_name,
                     age=input_age)
    session.add(new_user)
    session.commit()

find_name = input("Input name which you want to find: ")
for row in session.query(Users).filter(Users.first_name == find_name):
    print(row.first_name, row.last_name, row.age)

print()

for row in session.query(Users).filter(Users.age < 25):
    print(row.first_name, row.last_name, row.age)

print()

for row in session.query(Users).filter(Users.age > 15).filter(Users.age < 18):
    print(row.first_name, row.last_name, row.age)
