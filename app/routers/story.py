from fastapi import APIRouter
from app.services.story import StoryService

router = APIRouter(
    prefix="/story",
    tags=["stories"]
)


@router.get("/stories/")
async def get_story():
    return [{"story": "story 1"}, {"story": "story 2"}]


@router.get("/story/{id}")
async def read_story(id: str):
    return {"story": id}
