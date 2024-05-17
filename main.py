import service
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models import User

app = FastAPI()

# 替换为发起请求的确切源
allowed_origins = ["http://localhost:8080"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,  # 明确指定允许的源
    allow_credentials=True,          # 允许携带凭据
    allow_methods=["*"],            # 允许所有方法
    allow_headers=["*"],            # 允许所有头
)

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