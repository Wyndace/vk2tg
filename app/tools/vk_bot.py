from vkbottle import UserAuth
from app.tools.files import read_from_json, write_to_json

async def get_token():
    data = read_from_json('./configs/config.json')
    username = data['username']
    password = data['password']
    token = await UserAuth().get_token(username, password)
    data['token'] = token
    write_to_json(data, './configs/config.json')