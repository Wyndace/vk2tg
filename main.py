import logging
from asyncio import run
from time import monotonic
from vkwave.bots import TaskManager, SimpleLongPollUserBot
from app.states.menu import menu
from app.tools.vk_tg_mover import tg_mover


def main():

    bot = SimpleLongPollUserBot(
        tokens="077c088363fc8036755dd3965e0013ac63d217b9af3fc4e0f422c56742c5375ba2e3aa71d44dcd3b7bcd4")

    bot.dispatcher.add_router(tg_mover)
    task_manager = TaskManager()
    task_manager.add_task(bot.run(ignore_errors=False))
    task_manager.run()


if __name__ == '__main__':
    start = monotonic()
    main()
    print('Кол-во секунд, которые скрипт работал ->', monotonic() - start)
