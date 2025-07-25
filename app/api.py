from fastapi import APIRouter

router = APIRouter()

@router.get('/locomotives')
def list_locomotives():
    return []
