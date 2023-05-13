from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI

from servers.datastoryboard.routers import datastoryboard as datastoryboard_router

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount("/dsb-media", StaticFiles(directory="mediafiles"), name="statics")


@app.get('/')
async def hello():
    return {'welcomeMessage': 'Wellcome!'}


# router
app.include_router(datastoryboard_router)
