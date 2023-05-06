from fastapi import FastAPI

from servers.spider.routers import spider as spider_router

app = FastAPI()


@app.get('/')
async def hello():
    return {'welcomeMessage': 'Wellcome!'}


# router
app.include_router(spider_router)
