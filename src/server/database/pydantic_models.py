from pydantic import BaseModel
from typing import Optional


class BaseModelModify(BaseModel):
    id: Optional[int] = 1


class Client(BaseModelModify):
    first_name: str
    last_name: str
    phone_number: int
    email: str
    date_of_birth: str


class Service(BaseModelModify):
    name: str
    description: str
    duration: int
    cost: float


class Employee(BaseModelModify):
    first_name: str
    last_name: str
    position: str
    phone_number: int
    email: str


class Appointment(BaseModelModify):
    client_id: int
    employee_id: int
    service_id: int
    date_time: str
    status: str


class Room(BaseModelModify):
    name: str
    description: str


class Inventory(BaseModelModify):
    item_name: str
    quantity: int
    description: str


class PaymentTransaction(BaseModelModify):
    client_id: int
    amount: float
    date_time: str


class Review(BaseModelModify):
    client_id: int
    service_id: int
    rating: int
    comment: str
    date: str


class Product(BaseModelModify):
    name: str
    category: str
    price: float
    stock_quantity: int


class Discount(BaseModelModify):
    name: str
    discount_percentage: int
    start_date: str
    end_date: str


class LoginData(BaseModel):
    login: str
    password: str
