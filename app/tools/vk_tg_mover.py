import logging
from time import ctime

from vkwave.bots import DefaultRouter, simple_user_message_handler, EventTypeFilter, SimpleUserEvent
from app.tools.common import get_msg
from app.tools.files import read_from_json, write_to_json
from vkwave.types.user_events import MessageFlag

tg_mover = DefaultRouter()


@simple_user_message_handler(tg_mover, EventTypeFilter(4))
async def simple(event: SimpleUserEvent):
    logging.info(f'[{ctime()}] {event}')
    data = read_from_json('./configs/config.json')
    if not data['lock']:
        user_data = (await event.get_user())
        if user_data.id not in data['sent'] and MessageFlag.OUTBOX not in event.object.object.flags:
            await event.answer(get_msg(user_data.first_name, user_data.last_name))
            data['sent'].append(user_data.id)
            write_to_json(data, './configs/config.json')
