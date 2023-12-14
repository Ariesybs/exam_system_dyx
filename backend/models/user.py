from mongodb import user_collection

# 用户模型
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    # 保存
    @staticmethod
    def save(username,password)->bool:
        if not User.find_by_username(username):
            res = user_collection.insert_one({
                'username': username,
                'password': password,
            })

            print(f"insert id {res.inserted_id}")
            return True
        else:
            print("用户名存在")
            return False

    @staticmethod
    def delete_by_username(username)->bool:
        user_findOne = User.find_by_username(username)
        if user_findOne:
            res = user_collection.delete_one({"username":username})
            if res.deleted_count>0:
                print("删除成功")
                return True
        else:
            print("查无此人")
            return False

    @staticmethod
    def update_password(username,new_password):
        if User.find_by_username(username):
            res = user_collection.update_one({"username":username},{"$set":{"password":new_password}})
            if res.modified_count>0:
                print("update success")
            else:
                print("update failed")
        else:
            print("no find")


    @staticmethod
    def find_by_username(username):
        user_data = user_collection.find_one({'username': username})
        if user_data:
            return User(user_data['username'], user_data['password'])
        return None

    @staticmethod
    def find_by_username_and_password(username,password):
        user_findOne = user_collection.find_one({"username":username,"password":password})
        if user_findOne:
            return User(user_findOne["username"], user_findOne["password"])
        else:
            return None
        

