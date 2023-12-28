import peewee
import settings

db: peewee.SqliteDatabase = peewee.SqliteDatabase(f'{settings.DATABASE_PATH}{settings.DATABASE_NAME}')


class BaseModel(peewee.Model):
    class Meta:
        database = db


class Client(BaseModel):
    first_name = peewee.CharField(default='')
    last_name = peewee.CharField(default='')
    phone_number = peewee.CharField(default='')
    email = peewee.CharField(default='')
    date_of_birth = peewee.CharField(default='')


class Service(BaseModel):
    service_name = peewee.CharField(default='')
    description = peewee.CharField(default='')
    duration = peewee.IntegerField(default=0)
    cost = peewee.FloatField(default=0.0)


class Employee(BaseModel):
    first_name = peewee.CharField(default='')
    last_name = peewee.CharField(default='')
    position = peewee.CharField(default='')
    phone_number = peewee.CharField(default='')
    email = peewee.CharField(default='')


class Appointment(BaseModel):
    client = peewee.ForeignKeyField(Client, related_name='appointments')
    employee = peewee.ForeignKeyField(Employee, related_name='appointments')
    service = peewee.ForeignKeyField(Service, related_name='appointments')
    date_time = peewee.CharField(default='')
    status = peewee.CharField(default='')


class Room(BaseModel):
    room_name = peewee.CharField(default='')
    description = peewee.CharField(default='')



class Inventory(BaseModel):
    item_name = peewee.CharField(default='')
    quantity = peewee.IntegerField(default=0)
    description = peewee.CharField(default='')


class PaymentTransaction(BaseModel):
    client = peewee.ForeignKeyField(Client, related_name='transactions')
    amount = peewee.FloatField(default=0.0)
    date_time = peewee.CharField(default='')


class Review(BaseModel):
    client = peewee.ForeignKeyField(Client, related_name='reviews')
    service = peewee.ForeignKeyField(Service, related_name='reviews')
    rating = peewee.IntegerField(default=0)
    comment = peewee.CharField(default='')
    date = peewee.CharField(default='')


class Product(BaseModel):
    product_name = peewee.CharField(default='')
    category = peewee.CharField(default='')
    price = peewee.FloatField(default=0.0)
    stock_quantity = peewee.IntegerField(default=0)


class Discount(BaseModel):
    discount_name = peewee.CharField(default='')
    discount_percentage = peewee.IntegerField(default=0)
    start_date = peewee.CharField(default='')
    end_date = peewee.CharField(default='')


db.connect()
db.create_tables(
    [Client, Service, Employee, Appointment, Room, Inventory, PaymentTransaction, Review, Product, Discount])
