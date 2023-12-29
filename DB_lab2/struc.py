from base import Base, Session, engine
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey, Table

s = Session()

tables = {
    1: 'customer',
    2: 'Trav_Comp',
    3: 'Travel',
    4: 'Place',
}


class customer(Base):
    __tablename__ = 'customer'
    customer_id = Column(Integer, primary_key=True)
    name = Column(String)
    phone = Column(String)
    email = Column(String)

    travel_id = Column(Integer, ForeignKey('travel.travel_id'))
    comp_id = Column(Integer, ForeignKey('trcomp.comp_id'))
    place_id = Column(Integer, ForeignKey('place.place_id'))

    def __init__(self, name, phone, email, travel_id, comp_id, place_id):
        self.name = name
        self.phone = phone
        self.email = email
        self.travel_id = travel_id
        self.comp_id = comp_id
        self.place_id = place_id


    def __repr__(self):
        return f"<customer(customer_id={self.customer_id}, name={self.name}, phone={self.phone}, email={self.email}, travel_id={self.travel_id}, comp_id={self.comp_id}, place_id={self.place_id})>"


class trcomp(Base):
    __tablename__ = 'trcomp'
    comp_id = Column(Integer, primary_key=True)
    comp_name = Column(String)
    comp_address = Column(String)
    comp_phone = Column(String)

    customer = relationship("customer")

    def __init__(self, comp_name, comp_address, comp_phone):
        self.comp_name = comp_name
        self.comp_address = comp_address
        self.comp_phone = comp_phone

    def __repr__(self):
        return f"<trcomp(comp_id={self.comp_id}, comp_name={self.comp_name}, comp_address={self.comp_address}, comp_phone={self.comp_phone}, phone_number={self.phone_number})>"


class travel(Base):
    __tablename__ = 'travel'
    travel_id = Column(Integer, primary_key=True)
    time = Column(String)
    form = Column(String)
    pay = Column(String)

    customer = relationship("customer")

    def __init__(self, time, form, pay):
        self.time = time
        self.form = form
        self.pay = pay

    def __repr__(self):
        return f"<travel(travel_id={self.travel_id}, time={self.time}, form={self.form}, pay={self.pay})>"


class place(Base):
    __tablename__ = 'place'
    place_id = Column(Integer, primary_key=True)
    country = Column(String)
    city = Column(String)

    customer = relationship("customer")

    def __init__(self, country, city):
        self.country = country
        self.city = city

    def __repr__(self):
        return f"<place(place_id={self.place_id}, country={self.country}, city={self.city})>"


class Model:
    def __init__(self):
        self.session = Session()
        self.connection = engine.connect()

    @staticmethod
    def insert_customer(name: str, phone: str, email: str, travel_id: int, comp_id: int, place_id: int) -> None:
        Customer = customer(name=name, phone=phone, email=email, travel_id=travel_id, comp_id=comp_id, place_id=place_id)
        s.add(Customer)
        s.commit()

    @staticmethod
    def insert_trcomp(comp_name: str, comp_address: str, comp_phone: str) -> None:
        Trcomp = trcomp(comp_name=comp_name, comp_address=comp_address, comp_phone=comp_phone)
        s.add(Trcomp)
        s.commit()

    @staticmethod
    def insert_travel(time: str, form: str, pay: str) -> None:
        Travel = travel(time=time, form=form, pay=pay)
        s.add(Travel)
        s.commit()

    @staticmethod
    def insert_place(country: str, city: str) -> None:
        Place = place(country=country, city=city)
        s.add(Place)
        s.commit()

    @staticmethod
    def show_customers():
        return s.query(customer.name, customer.phone, customer.email, customer.travel_id, customer.comp_id, customer.place_id).all()

    @staticmethod
    def show_trcomps():
        return s.query(trcomp.comp_name, trcomp.comp_address, trcomp.comp_phone).all()

    @staticmethod
    def show_travels():
        return s.query(travel.time, travel.form, travel.pay).all()

    @staticmethod
    def show_places():
        return s.query(place.country, place.city).all()

    @staticmethod
    def update_customer(customer_id: int, name: str, phone: str, email: str, travel_id: int, comp_id: int, place_id: int) -> None:
        s.query(customer).filter_by(customer_id=customer_id).update({customer.name: name, customer.phone: phone, customer.email: email, customer.travel_id: travel_id, customer.comp_id: comp_id, customer.place_id: place_id})
        s.commit()

    @staticmethod
    def update_trcomp(comp_id: int, comp_name: str, comp_address: str, comp_phone: str) -> None:
        s.query(trcomp).filter_by(comp_id=comp_id).update({trcomp.comp_name: comp_name, trcomp.comp_address: comp_address, trcomp.comp_phone: comp_phone})
        s.commit()

    @staticmethod
    def update_travel(travel_id: int, time: str, form: str, pay: str) -> None:
        s.query(travel).filter_by(travel_id=travel_id).update({travel.time: time, travel.form: form, travel.pay: pay})
        s.commit()

    @staticmethod
    def update_place(place_id: int, country: str, city: str) -> None:
        s.query(place).filter_by(place_id=place_id).update({place.country: country, place.city: city})
        s.commit()


    @staticmethod
    def delete_customer(customer_id) -> None:
        Customer = s.query(customer).filter_by(customer_id=customer_id).one()
        s.delete(Customer)
        s.commit()

    @staticmethod
    def delete_trcomp(comp_id) -> None:
        Trcomp = s.query(trcomp).filter_by(comp_id=comp_id).one()
        s.delete(Trcomp)
        s.commit()


    @staticmethod
    def delete_travel(travel_id) -> None:
        Travel = s.query(travel).filter_by(travel_id=travel_id).one()
        s.delete(Travel)
        s.commit()

    @staticmethod
    def delete_place(place_id) -> None:
        Place = s.query(place).filter_by(place_id=place_id).one()
        s.delete(Place)
        s.commit()
