from pymongo import MongoClient

# 连接 MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['exam_system']

user_collection = db["user"]