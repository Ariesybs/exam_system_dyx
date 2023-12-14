from fastapi import FastAPI
from login import router

app = FastAPI()

# 导入其他模块的路由
app.include_router(router)