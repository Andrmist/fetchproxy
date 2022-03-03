import argparse


parser = argparse.ArgumentParser(description='Parse proxy file (fetched from fetchproxy.py) to /etc/proxychains.conf')
parser.add_argument('proxy_path', metavar='FILE', type=str, help='proxy path', nargs='?', default='proxy.txt')
parser.add_argument('-c', metavar='config', type=str, help='proxychains config', default='/etc/proxychains.conf')
parser.add_argument('--socks', help='fetch socks proxies', action='store_true')
parser.add_argument('--http', help='fetch http proxies', action='store_true')

file_path = parser.parse_args().proxy_path
proxychains_path = parser.parse_args().c
socks = parser.parse_args().socks
http = parser.parse_args().http

proxy_file = open(file_path, 'r')
if not socks and not http:
    print("Specify --http or --socks")
    exit(1)

proxychains_file = open(proxychains_path, 'r+')
lines = proxychains_file.readlines()
proxychains_file.seek(0)
index = 0

# print(lines)

try:
    index = lines.index('[ProxyList]\n')
except ValueError:
    index = len(lines)

print(index)

proxychains_file.truncate()

for number, line in enumerate(lines):
    if number not in range(index + 1, len(lines)):
        proxychains_file.write(line)

for proxy in proxy_file.readlines():
    host, port = proxy.split(':')
    proxychains_file.write(f'{"socks5" if socks else "http"} {host} {port}')

proxychains_file.close()