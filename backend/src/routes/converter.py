from fastapi import APIRouter, Query
from requests import HTTPError

from services.converter import Converter

currency_router = APIRouter(tags=["converter"])


@currency_router.get('/rates/')
async def retrieve_all_events(to: str, value: int, from_: str = Query(alias='from')) -> dict:
    try:
        result = Converter().convert(from_, to, value)
    except (ValueError, HTTPError, KeyError) as ex:
        return {'error': str(ex)}

    return {'result': result}
