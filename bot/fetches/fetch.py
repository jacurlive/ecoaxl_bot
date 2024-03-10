import os
import aiohttp


async def fetch_place_data(token):

    url = f"{os.environ['API']}place/"

    headers = {
        'Authorization': token
    }

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(url) as response:
            data = await response.json()
            return data
        
async def fetch_rates_data(token):

    url = f"{os.environ['API']}rates/"

    headers = {
        'Authorization': token
    }

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(url) as response:
            data = await response.json()
            return data


async def post_user_info(data, token):
    url = url = f"{os.environ['API']}account/"

    headers = {
        'Authorization': token
    }

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.post(url, data=data) as response:
            data = await response.json()
            print(data)
            return data
        

async def user_exist(telegram_id, token):
    url = f"{os.environ['API']}account/{telegram_id}"

    headers = {
        'Authorization': token
    }

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(url) as response:
            response_code = response.status
            return response_code
