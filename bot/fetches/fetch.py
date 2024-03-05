import os
import aiohttp


async def fetch_place_data():

    url = os.environ['API_PLACE']

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            return data
        
async def fetch_rates_data():

    url = os.environ['API-RATES']

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            return data


async def post_user_info(data):
    url = os.environ['API_ACCOUNT_CREATE']


    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=data) as response:
            data = await response.json()
            print(data)
            return data
        

async def user_exist(telegram_id):
    url = f"{os.environ['API_ACCOUNT_CREATE']}{telegram_id}"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            response_code = response.status
            return response_code
