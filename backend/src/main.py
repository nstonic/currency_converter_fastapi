from fastapi import FastAPI
from starlette.responses import RedirectResponse

from routes.converter import currency_router

app = FastAPI()

app.include_router(currency_router, prefix='/api')


@app.get('/')
async def home():
    return RedirectResponse(url='/docs/')
