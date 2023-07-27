from fastapi import FastAPI
from utils import get_message, get_prayer_times_by_date, get_monthly_prayer_times_for_region, get_region_name_by_id

app = FastAPI()


@app.get("/get/message/")
async def get_msg(region_id: int, month: int, day: int, language: str):
    result = get_message(region_id, month, day, language)
    return {"result": {'message': result}}


@app.get("/get/prayer_times/")
async def get_prayer_times(region_id: int, month: int, day: int, language: str):
    result = get_prayer_times_by_date(region_id, month, day, language)
    return {"result": result}


@app.get("/get/monthly_prayer_times/")
async def get_monthly_prayer_times(region_id: int, month: int, language: str):
    result = get_monthly_prayer_times_for_region(region_id, month, language)
    return {"result": result}


@app.get("/get/region_name/")
async def get_region_name(region_id: int, language: str):
    result = get_region_name_by_id(region_id, language)
    return {"result": result}