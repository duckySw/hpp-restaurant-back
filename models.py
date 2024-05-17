from pydantic import BaseModel
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float

Base = declarative_base()

# 定义管理员信息模型
class AdminInfo(BaseModel):
    AdminID: int
    Name: str
    Password: str

# 定义用户信息模型
class User(BaseModel):
    username: str
    password: str

# 定义菜品信息模型
class DishInfo(BaseModel):
    id: int
    name: str
    price: float
    description: str
    stock: int
    img: str

# 定义订单信息模型
class Order(BaseModel):
    user_id: int
    dish_id: int
    quantity: int
    total_price: float