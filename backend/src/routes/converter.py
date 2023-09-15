from fastapi import APIRouter
from requests import HTTPError

from services.converter import Converter

currency_router = APIRouter(tags=["converter"])


@currency_router.get('/rates/')
async def retrieve_all_events(from_: str, to: str, value: int) -> dict:
    try:
        data = {
            "result": Converter().convert(from_, to, value)
        }
    except ValueError as ex:
        return {'error': str(ex)}
    except (HTTPError, KeyError) as ex:
        return {'error': str(ex)}

    return data

