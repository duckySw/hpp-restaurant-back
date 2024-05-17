from pydantic import BaseModel

# 定义 Pydantic 模型，用于对象序列化与反序列化

# 定义管理员信息模型
class AdminInfo(BaseModel):
    AdminID: int
    Name: str
    Password: str


# 定义菜品信息模型
class DishInfo(BaseModel):
    id: int
    name: str
    price: float
    description: str
    stock: int
    img: str