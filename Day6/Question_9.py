# Question-9:

import asyncio
import aiohttp
import time
from bs4 import BeautifulSoup

async def download_links(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            html = await response.text()
            soup = BeautifulSoup(html, 'html.parser')
            links = [a['href'] for a in soup.find_all('a', href=True)]
            return links
async def main(urls):
    tasks = [download_links(url) for url in urls]
    results = await asyncio.gather(*tasks)
    for result in results:
        print(result)
        
if __name__ == "__main__":
    start_time = time.time()
    asyncio.run(main(['https://docs.python.org/3/']))
    print(f"Execution time: {time.time() - start_time} seconds" )
    