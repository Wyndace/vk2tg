from json import dump, loads
from os import remove, path as ospath, makedirs, getcwd


def delete_path(path):
    if ospath.exists(path):
        remove(path)


def create_dir(path: str):
    if not ospath.exists(f'{path}'):
        makedirs(f'{path}')


def write_to_json(data: dict | list, path: str):
    with open(path, 'w', encoding='utf8') as file:
        dump(data, file, indent=3, ensure_ascii=False)


def read_from_json(path: str, is_file=True) -> dict | list:
    if is_file:
        with open(path, 'r', encoding='utf8') as file:
            data = loads(file.read())
    else:
        data = loads(path)
    return data


def update_json(data: dict | list, path: str):
    try:
        old_data = read_from_json(path)
    except Exception:
        old_data = None
    print(data, old_data, type(data), type(old_data))
    if old_data and type(old_data) == type(data) == dict:
        old_data.update(data)
    elif old_data and type(old_data) == type(data) == list:
        data += old_data
    write_to_json(data, path)
