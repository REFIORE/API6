# Описание проекта
Создали телеграм-бота, который автоматически отправляет случайные комиксы в заданный телеграм-канал. Проект ориентирован на упрощение процесса публикации развлекательного контента и автоматизацию рутины.

Функционал
Отправка случайных комиксов:
Бот выбирает случайный комикс из заранее подготовленной базы данных или через API популярных ресурсов (xkcd)

## Установка библиотеки
Для загрузки всех необходимых библиотек впишите в консоль.
```
pip install -r requirements.txt
``` 

## Как запустиь программу
Создайте бота у отцов ботов. Создавайте новый канал в Telegram.
В консоль панели нужно вписать

```
python main.py
```

## Переменные окружения

Часть настроек проекта берётся из переменных окружения. Переменные окружения — это переменные, значения которых присваиваются программе Python извне. Чтобы их определить, создайте файл `.env` рядом с `main.py` и запишите туда данные в таком формате: ПЕРЕМЕННАЯ=значение.

Пример содержания файла `.env`:

```
TELEGRAM_TOKEN='token'
TG_CHAT_ID='chad_id'
```

Получить токен `TELEGRAM_TOKEN` можно с помощью отца ботов. В описании канала получите и положите в переменную `TG_CHAT_ID`.

## Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
