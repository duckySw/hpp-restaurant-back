import service
from fastapi import FastAPI, HTTPException

from models import User

app = FastAPI()

# 管理员相关接口
@app.get("/admin/getAdminInfo")
async def getAdminInfo():
    return service.getAdminInfo()

# 用户相关接口
@app.post("/users/register", status_code=201)
async def register_user(user: User):
    try:
        # 增加一些检验逻辑，比如用户名是否已存在



        res = service.createUser(user.username, user.password)
        if res:
            return {"message": "User created successfully"}
        else:
            raise HTTPException(status_code=500, detail="Failed to create user")
    except ValueError as ve:
        raise HTTPException(status_code=422, detail=str(ve))  # 422 Unprocessable Entity 用于表单填写错误
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 菜品相关接口
@app.get("/dishes/getDishInfo")
async def getDishInfo():
    return service.getDishInfo()


# 订单相关接口
# 创建订单
@app.post("/orders/createOrder")
async def create_order(admin_id: int, dish_id: int, quantity: int, total_price: float):
    return service.create_order(admin_id, dish_id, quantity, total_price)




# 评论相关接口