from asyncio import run

from app.states.gsheet_menu import gsheet_menu
from app.states.parser_menu import parser_menu
from app.tools.common import async_chooser_menu
from app.tools.files import read_from_json, write_to_json


def chose_lock():
    inp_text = '''Выберите пункт записи данных в excel: 
    1.) Перезаписать файл (очистить и добавить новые данные)
    2.) Добавить новые поля к уже имеющимся

Ваш выбор: '''
    lock = -1
    while 0 > lock or lock >= 2:
        try:
            lock = int(input(inp_text)) - 1
        except Exception:
            print('\nВведено неверное значение! Попробуйте ещё раз!\n')
            continue
        if 0 > lock or lock >= 2:
            print('\nВведено неверное значение! Попробуйте ещё раз!\n')
    return lock


async def menu(*args):
    inp_text = '''Выберете пункт меню:
    1.) Пункт управления аккаунтом
    2.) Включить/Выключить автоответчика

Ваш выбор: '''
    choice = await async_chooser_menu(inp_text, 2)
    if choice == 1:
        while True:
            break
    elif choice == 2:
        data = read_from_json('./configs/config.json')
        data['lock'] = not data['lock']
        write_to_json(data, './configs/config.json')


if __name__ == '__main__':
    while True:
        run(menu())
