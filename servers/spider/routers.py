from fastapi.routing import APIRouter
from .schemas import SpiderSchema

spider = APIRouter(
    prefix='/api/spiders',
    tags=['spider'],
)


@spider.post('')
async def create_interest(itm: SpiderSchema):
    return itm


@spider.get('')
async def the_list():
    itm = SpiderSchema()
    return [itm]


@spider.get('/{pk}')
async def retrieve(pk: int):
    itm = SpiderSchema()
    return itm


@spider.patch('/{pk}')
async def update(pk: int):
    itm = SpiderSchema()
    return itm


@spider.put('/{pk}')
async def update(pk: int):
    itm = SpiderSchema()
    return itm


@spider.delete('/{pk}')
async def destroy(pk: int):
    itm = SpiderSchema()
    return itm
