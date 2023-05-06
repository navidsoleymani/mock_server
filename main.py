from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

from slowapi import _rate_limit_exceeded_handler as limited_handler
from slowapi.errors import RateLimitExceeded
from slowapi.util import get_remote_address
from slowapi import Limiter

from servers.spider.routers import spider as spider_router

app = FastAPI()


# limiter = Limiter(key_func=get_remote_address)
#
# origins = ['*']
#
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# limiter
# app.state.limiter = limiter
# app.add_exception_handler(RateLimitExceeded, limited_handler)

# router
# app.include_router(spider_router)

@app.get('/')
async def create_interest():
    return {}
