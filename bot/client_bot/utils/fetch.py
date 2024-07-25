import os
import aiohttp

from data import config


async def get_customers(token):
    url = f"{config.API}account/"

    headers = {
        'Authorization': token
    }

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(url=url) as response:
            data = await response.json()
            return data


async def get_by_phone(contact, token):
    url = f"{config.API}account/phone/{contact}"

    headers = {
        'Authorization': token
    }

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(url=url) as response:
            if response.status == 200:
                data = await response.json()
                return data


async def put_id_by_phone(data, contact, token):
    url = f"{config.API}account/phone/{contact}"

    headers = {
        'Authorization': token
    }

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.patch(url=url, data=data) as response:
            return response.status


async def fetch_place_data(token):
    url = f"{config.API}place/"

    headers = {
        'Authorization': token
    }

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(url) as response:
            data = await response.json()
            return data


async def fetch_rates_data(token):
    url = f"{config.API}rates/"

    headers = {
        'Authorization': token
    }

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(url) as response:
            data = await response.json()
            return data


async def post_user_info(data, token):
    url = f"{config.API}account/"

    headers = {
        'Authorization': token
    }

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.post(url, data=data) as response:
            response_code = response.status
            if response_code == 201 or response_code == 200:
                data = await response.json()
                return data


async def user_exist(telegram_id, token):
    url = f"{config.API}account/{telegram_id}"

    headers = {
        'Authorization': token
    }

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(url) as response:
            response_code = response.status
            return response_code


async def get_user_data(telegram_id, token):
    url = f"{config.API}account/{telegram_id}"

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
    url = f"{config.API}account/delete/{telegram_id}"

    headers = {
        'Authorization': token
    }

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.delete(url) as response:
            return response.status


async def user_change_column(telegram_id, data, token):
    url = f"{config.API}account/{telegram_id}"

    headers = {
        'Authorization': token
    }

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.patch(url, data=data) as response:
            response_code = response.status
            return response_code


async def create_order(data, token):
    url = f"{config.API}order/"

    headers = {
        'Authorization': token
    }

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.post(url, data=data) as response:
            response_code = response.status
            if response_code == 201:
                response_data = await response.json()
                return response_data
            else:
                return None


async def order_exist(telegram_id, token):
    url = f"{config.API}order/"

    headers = {
        'Authorization': token
    }

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(url) as response:
            response_data = await response.json()
            for i in response_data:
                if i["client_id"] == telegram_id:
                    return i
            return False


async def take_order(order_id, data, token):
    url = f"{config.API}order/{order_id}"

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


async def post_user_language(data, token):
    url = f"{config.API}account/language"

    headers = {
        'Authorization': token
    }

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.post(url=url, data=data) as response:
            response_code = response.status

            return response_code


async def user_language(data=None, user_id=None, token=None):
    url = f"{config.API}account/language/{user_id}"

    headers = {
        'Authorization': token
    }

    async with aiohttp.ClientSession(headers=headers) as session:
        if data is not None:
            async with session.patch(url=url, data=data) as response:
                response_code = response.status
                return response_code
        else:
            async with session.get(url=url) as response:
                response_code = response.status
                if response_code == 200:
                    language_data = await response.json()
                    return language_data
                else:
                    print("123")


async def rate_detail(rate_id, token):
    url = f"{config.API}rates/{rate_id}"

    headers = {
        'Authorization': token
    }

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(url=url) as response:
            response_code = response.status
            if response_code == 200:
                response_data = await response.json()
                return response_data
