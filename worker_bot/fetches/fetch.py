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


async def post_user_info(data, token):
    url = url = f"{os.environ['API']}worker/"

    headers = {
        'Authorization': token
    }

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.post(url, data=data) as response:
            data = await response.json()
            response_code = response.status
            return response_code
        

async def user_exist(telegram_id, token):
    url = f"{os.environ['API']}account/{telegram_id}"

    headers = {
        'Authorization': token
    }

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(url) as response:
            response_code = response.status
            return response_code
        

async def get_user_data(telegram_id, token):
    url = f"{os.environ['API']}worker/{telegram_id}"

    headers = {
        'Authorization': token
    }

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(url) as response:
            if response.status == 200:
                response_data = await response.json()
            else:
                response_data = None

            return response_data
        

async def delete_user_data(telegram_id, token):
    url = f"{os.environ['API']}worker/delete/{telegram_id}"

    headers = {
        'Authorization': token
    }

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.delete(url) as response:
            return response.status


async def user_change_column(telegram_id, data, token):
    url = f"{os.environ['API']}worker/{telegram_id}"

    headers = {
        'Authorization': token
    }

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.patch(url, data=data) as response:
            response_code = response.status
            return response_code
        

async def get_orders(token):
    url = f"{os.environ['API']}order/"

    headers = {
        'Authorization': token
    }

    async with aiohttp.ClientSession(headers=headers) as sessions:
        async with sessions.get(url) as response:
            response_code = response.status
            data = await response.json()
            if response_code == 200:
                return data
            

async def take_order(order_id, data, token):
    url = f"{os.environ['API']}order/{order_id}"

    headers = {
        'Authorization': token
    }

    async with aiohttp.ClientSession(headers=headers) as sessions:
        async with sessions.patch(url, data=data) as response:
            response_code = response.status
            data = await response.json()
            if response_code == 200:
                return data
            else:
                print("123")
