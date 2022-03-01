# fetchproxy

## DESCRIPTION

Скріпт витягує файл проксі з https://t.me/proxy_list_misha та зберігає до файлу 

## INSTALL

```commandline
git clone https://github.com/Andrmist/fetchproxy.git
pip3 install telethon dotenv
```

## CONFIG

Отримати нижче вказані значення можна на [my.telegram.org](my.telegram.org)

`.env`
```
TELEGRAM_API_ID=
TELEGRAM_API_HASH=
```

## USAGE

*Увага, перший запуск потребує вводу номеру телефону (або token_id) та коду з Телеграму. [(Для лякливих)](https://docs.telethon.dev/en/stable/basic/signing-in.html)*

```commandline
usage: fetchproxy.py [-h] [FILE]

Fetch proxy from https://t.me/proxy_list_misha

positional arguments:
  FILE        File path

options:
  -h, --help  show this help message and exit
```