from fastapi import FastAPI
import service

app = FastAPI()

# 管理员相关接口
@app.get("/items/getAdminInfo")
async def getAdminInfo():
    return service.getAdminInfo()

# 用户相关接口



# 菜品相关接口
@app.get("/items/getDishInfo")
async def getDishInfo():
    return service.getDishInfo()


# 订单相关接口





# 评论相关接口