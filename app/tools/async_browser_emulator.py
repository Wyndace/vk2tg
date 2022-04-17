from asyncio import sleep, run

from pyppeteer import launch

URL = 'https://vk.com/'


async def get_message(dialog_id):
    pass


async def login(username, password):
    browser = await launch(headless=False, executablePath='/usr/bin/google-chrome-unstable')
    page = await browser.newPage()
    # try:
    await page.goto(URL)
    print('Проходим авторизацию')
    await page.waitForSelector('.VkIdForm__signInButton')
    login_button = await page.querySelector('.VkIdForm__signInButton')
    await login_button.click()
    await page.waitForSelector('[name="login"]')
    username_field = await page.querySelector('[name="login"]')
    await username_field.click()
    await page.evaluate('(username_field, username) => {username_field.click(); username_field.value = username}', username_field, username)
    await page.waitForResponse(URL + 'feed')
    # except:
    #     pass
    await browser.close()


if __name__ == '__main__':
    run(login('wyndace@hotmail.com', '323'))
