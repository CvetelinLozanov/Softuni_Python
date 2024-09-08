import json
import random

from sqlalchemy.orm import Session, sessionmaker

from models import engine, Employee, City


def create_employee():
    # similar to object in django session to interact with database
    Session = sessionmaker(bind=engine)
    with Session() as session:
        employee = Employee(
            first_name="Ivan",
            last_name="Dobrev",
            age=33
        )

    session.add(employee)
    session.commit()


def load_data():
    Session = sessionmaker(bind=engine)
    with Session() as session:
        with open('MOCK_DATA.json') as jsf:
            file_content = json.load(jsf)

            for d in file_content:
                #parsed_json = json.loads(json.dumps(d))
                employee = Employee(
                    first_name=d['first_name'],
                    last_name=d['last_name'],
                    age=d['age']
                )
                session.add(employee)
            session.commit()


def get_employees():
    Session = sessionmaker(bind=engine)
    with Session() as session:
        #employees = session.query(Employee).all()
        #employees = session.query(Employee).filter(Employee.age >= 40)
        #employees = session.query(Employee).filter_by(first_name='Ivan')
        employees = session.query(Employee).where(
            (Employee.first_name.startswith('A')) | (Employee.age > 60)
        ).order_by(Employee.first_name.desc())

        for e in employees:
            print(e.first_name, e.last_name, e.age)


def delete_first_employee():
    Session = sessionmaker(bind=engine)
    with Session() as session:
        employee = session.query(Employee).first()
        session.delete(employee)
        session.commit()


def add_cities():
    Session = sessionmaker(bind=engine)
    with Session() as session:
        session.add_all(
            (
                City(name='Sofia'),
                City(name='Burgas'),
                City(name='Varna'),
                City(name='Smolqn'),
                City(name='Stara Zagora')
            )
        )

        session.commit()


def fill_data_in_cities_id():
    Session = sessionmaker(bind=engine)
    with Session() as session:
        for e in session.query(Employee).all():
            e.city_id = random.randint(1, 5)

        session.commit()


fill_data_in_cities_id()




