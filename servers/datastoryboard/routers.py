from fastapi.responses import JSONResponse
from starlette.status import HTTP_200_OK
from fastapi.routing import APIRouter

datastoryboard = APIRouter(
    prefix='/api/v1/dsb/report1401',
    tags=['datastoryboard'],
)


@datastoryboard.get('/chapters/')
async def chapter_list():
    """
    This API returns the list of all available chapters.
    <br>
    :return: chapters
    """
    from .sample_response.chapter import CHAPTER_RESPONSE_LIST_SAMPLE
    return JSONResponse(content=CHAPTER_RESPONSE_LIST_SAMPLE, status_code=HTTP_200_OK)


@datastoryboard.get('/chapters/{slug}')
async def get_chapter(slug: str):
    """
    This API returns the master detail of a chapter based on a specified slug.
    <br>
    :param slug: required, string, unique
    <br>
    :return: chapter, json
    """
    from .sample_response.chapter import CHAPTER_RESPONSE_RETRIEVE_SAMPLE
    return JSONResponse(content=CHAPTER_RESPONSE_RETRIEVE_SAMPLE, status_code=HTTP_200_OK)
