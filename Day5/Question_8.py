import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

def download(url):
    response = requests.get(url)
    return response.text

def parse_links(html):
    soup = BeautifulSoup(html, 'html.parser')
    return [a['href'] for a in soup.find_all('a', href=True)]

def download_link(url):
    print(f"Downloading: {url}")
    response = requests.get(url)
    return response.content

def main(url):
    html = download(url)
    links = parse_links(html)
    with ThreadPoolExecutor() as executor:
        executor.map(download_link, links)

if __name__ == "__main__":
    main("https://www.python.org/ftp/python/3.12.8/python-3.12.8-amd64.exe") 