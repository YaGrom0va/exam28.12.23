from src.server.database import models as database_models
from src.server.database import pydantic_models
from src.server.service import *

routers = (
    RouterManager(
        database_model=database_models.Client,
        pydantic_model=pydantic_models.Client
    ).fastapi_router,

    RouterManager(
        database_model=database_models.Service,
        pydantic_model=pydantic_models.Service
    ).fastapi_router,

    RouterManager(
        database_model=database_models.Employee,
        pydantic_model=pydantic_models.Employee
    ).fastapi_router,

    RouterManager(
        database_model=database_models.Appointment,
        pydantic_model=pydantic_models.Appointment
    ).fastapi_router,

    RouterManager(
        database_model=database_models.Inventory,
        pydantic_model=pydantic_models.Inventory
    ).fastapi_router,

    RouterManager(
        database_model=database_models.Room,
        pydantic_model=pydantic_models.Room
    ).fastapi_router,

    RouterManager(
        database_model=database_models.PaymentTransaction,
        pydantic_model=pydantic_models.PaymentTransaction
    ).fastapi_router,

    RouterManager(
        database_model=database_models.Product,
        pydantic_model=pydantic_models.Product
    ).fastapi_router,

    RouterManager(
        database_model=database_models.Discount,
        pydantic_model=pydantic_models.Discount
    ).fastapi_router,
)


def find_router_by_tag(rt: list, tag: str):
    for r in rt:
        if r.tags[0] == tag:
            return r
