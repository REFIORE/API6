import telegram
import requests
import random
import os
import asyncio
from dotenv import load_dotenv


def get_comic(random_number):
    url = f'https://xkcd.com/{random_number}/info.0.json'
    response = requests.get(url)
    response.raise_for_status()
    response_comic = response.json()
    img = response_comic['img']
    comment = response_comic['alt']
    return comment, img


def download(img, filepath):
    response = requests.get(img)
    response.raise_for_status()
    with open(filepath, 'wb') as file:
        file.write(response.content)


def get_total_number_of_comics():
    url_comic = 'https://xkcd.com/info.0.json'
    response = requests.get(url_comic)
    response.raise_for_status()
    all_number = response.json()['num']
    return all_number


async def publish_img(tg_token, chat_id):
    bot = telegram.Bot(token=tg_token)
    with open('Comic.png', 'rb') as f:
        await bot.send_photo(chat_id=chat_id, photo=f)


def main():
    try:
        load_dotenv()
        tg_token = os.environ['TELEGRAM_TOKEN']
        chat_id = os.environ['TG_CHAT_ID']
        random_number = random.randint(0, get_total_number_of_comics())
        comment, img = get_comic(random_number)
        download(img, 'Comic.png')
        asyncio.run(publish_img(tg_token, chat_id))
    finally:
        os.remove('Comic.png', dir_fd=None)


if __name__ == '__main__':
    main()
