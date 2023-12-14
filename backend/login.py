from fastapi import APIRouter

router = APIRouter()

@router.get('/exams')
def get_exams():
    # 处理获取考试列表的逻辑
    pass

@router.get('/exams/{exam_id}')
def get_exam(exam_id: int):
    # 处理获取单个考试的逻辑
    pass