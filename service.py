from mysql import connector
from models import AdminInfo, DishInfo


# 数据库配置信息
config = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': 'Zhangyaqing123',
    'database': '点餐系统'
}

def get_database_connection():
    return connector.connect(**config)


# 管理员相关

def getAdminInfo():
    conn = get_database_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Admins")
    items = cursor.fetchall()
    cursor.close()
    conn.close()

    # 封装为 AdminInfo 对象列表
    return [AdminInfo(AdminID=item[0], Name=item[1], Password=item[2]) for item in items]



# 用户相关
# 新建用户
def createUser(username, password):
    conn = None
    cursor = None

    try:
        # 参数验证
        if not (username and password) or not isinstance(username, str) or not isinstance(password, str):
            raise ValueError("Username and password must be non-empty strings.")

        conn = get_database_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Users (username, password) VALUES (%s, %s)", (username, password))
        conn.commit()
    except Exception as e:
        print(f"An error occurred: {e}")
        conn.rollback() if conn else None
        cursor.close() if cursor else None
        conn.close() if conn else None
        return False
    finally:
        cursor.close() if cursor else None
        conn.close() if conn else None
    return True



# 菜品相关
def getDishInfo():
    conn = get_database_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Dishes")
    items = cursor.fetchall()
    cursor.close()
    conn.close()

    # 封装为 DishInfo 对象列表
    return [DishInfo(id=item[0], name=item[1], price=item[2], description=item[3], stock=item[4], img=item[5]) for item in items]






# 订单相关








# 评论相关





# service层测试用
if __name__ == '__main__':
    conn = get_database_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Dishes")  # 替换为你的表名
    items = cursor.fetchall()
    cursor.close()
    conn.close()
    print(items)