import aiohttp
import asyncio
import time
import sys
from concurrent.futures import ThreadPoolExecutor
import requests
from bs4 import BeautifulSoup

if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

async def download(url):
    async with aiohttp.ClientSession() as sess:
        async with sess.get(url) as resp:
            return await resp.text()

async def main():
    url = "http://httpbin.org/get"
    res = await download(url)
    return res

async def mainp(n):
    urls = ["http://httpbin.org/get" for _ in range(n)]
    res = await asyncio.gather(*[download(u) for u in urls])
    return res

def fetch(url):
    response = requests.get(url)
    return response.text

def parsehtml(html):
    page = BeautifulSoup(html, 'html.parser')
    links = [link.get('href') for link in page.find_all('a', href=True)]
    return links

def fetchandparse(url):
    html = fetch(url)
    links = parsehtml(html)
    print(links)

if __name__ == '__main__':
    st = time.time()
    asyncio.run(main())
    print("Time taken", time.time() - st, "secs")
    print('now running in parallel')
    asyncio.run(mainp(10))
    print("Time taken", time.time() - st, "secs")

    url = "https://docs.python.org/3/"
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(fetchandparse, url) for _ in range(5)]
    for future in futures:
        future.result()
