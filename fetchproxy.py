from telethon import TelegramClient, events

import argparse
from config import api_id, api_hash

parser = argparse.ArgumentParser(description='Fetch proxy from https://t.me/proxy_list_misha')
parser.add_argument('file_path', metavar='FILE', type=str, help='File path', nargs='?', default='proxy.txt')
parser.add_argument('--socks', help='fetch socks proxies', action='store_true')
parser.add_argument('--http', help='fetch http proxies', action='store_true')
file_path = parser.parse_args().file_path
socks = parser.parse_args().socks
http = parser.parse_args().http

if not socks and not http:
    print("Specify --http or --socks")
    exit(1)

client = TelegramClient('autoproxy', api_id, api_hash)


def callback(current, total):
    print('Downloaded', current, 'out of', total,
          'bytes: {:.2%}'.format(current / total))


async def main():
    last_proxy = None
    if socks:
        last_proxy = [i async for i in client.iter_messages('@proxy_list_misha')][0]
    else:
        last_proxy = [i async for i in client.iter_messages('@proxy_list_misha')][1]

    await client.download_media(last_proxy, file=file_path, progress_callback=callback)


with client:
    client.loop.run_until_complete(main())
