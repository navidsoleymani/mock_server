from fastapi import FastAPI

from servers.spider.routers import spider as spider_router
from servers.datastoryboard.routers import datastoryboard as datastoryboard_router

app = FastAPI()


@app.get('/')
async def hello():
    return {'welcomeMessage': 'Wellcome!'}


# router
app.include_router(spider_router)
app.include_router(datastoryboard_router)
