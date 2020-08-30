from selenium.webdriver.firefox.options import Options

from seleniumwire import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import asyncio
#import requests
from concurrent.futures import ThreadPoolExecutor

from time import sleep
import os
import subprocess
import shutil


async def load_episode(chunk_list):
    with ThreadPoolExecutor(max_workers=15) as requester:
        loop = asyncio.get_event_loop()

        task = [loop.run_in_executor(requester, req_get, url) for url in chunk_list]

        for chunk_loaded in await asyncio.gather(*task):
            chunk_name = chunk_loaded.url.split(':')[-1]
            folder_name = (chunk_loaded.url.split(':')[-3]).split('/')[-1]
            if not os.path.exists(f"./{folder_name}"):
                os.mkdir(folder_name)
            with open(f'./{folder_name}/{chunk_name}', 'wb') as chunk:
                chunk.write(chunk_loaded.content)


def req_get(url):
    response = requests.get(url)
    print(response.url, "    loaded")
    return response

def download_episode(chunk_list):
    loop = asyncio.get_event_loop()
    future = asyncio.ensure_future(load_episode(chunk_list))
    loop.run_until_complete(future)

def make_file(chunk_urls):
    folder = (chunk_urls[0].split(':')[-3]).split('/')[-1]
    chunk_names = [ './'+folder+'/'+url.split(':')[-1] for url in chunk_urls]
    
    command_string = 'concat:' + '|'.join(chunk_names)

    subprocess.call(['ffmpeg',
        '-i',
        command_string,
        '-c',
        'copy',
        './test_episode.ts']) 

    shutil.rmtree('./'+folder, ignore_errors=False, onerror=None)

def get_chunk_links(driver: webdriver, url: str):
    driver.get(url)
        
    player = driver.find_element_by_id('player')
    driver.execute_script("arguments[0].scrollIntoView();", player)
    play_button = driver.find_element_by_xpath(
        '//pjsdiv[@id="oframecdnplayer"]/pjsdiv/pjsdiv/pjsdiv[@style="position: absolute; top: -15px; left: -21px; width: 42px; height: 30px; border-radius: 3px; background: rgb(29, 174, 236) none repeat scroll 0% 0%; opacity: 1; transition: opacity 0.1s linear 0s, background 0.1s linear 0s, transform 0.1s linear 0s; cursor: pointer; pointer-events: auto; transform: scale(2);"]'
        )
    play_button.click()
    driver.wait_for_request('.m3u8', timeout=10)
    chunk_urls = []
    for request in driver.requests:
        if '.m3u8' in request.path and request.response and request.response.body:
            request_url = "/".join(request.path.split('/')[:-1])
            chunk_urls = [request_url + line[1:] for line in request.response.body.decode().split('\n')[7::2] if line[-2:]=="ts"]
            return chunk_urls


if __name__ == "__main__":
    options = Options()
    options.add_argument('-headless')
    
    url = "https://rezka.ag/cartoons/comedy/2136-rik-i-morti-2013.html#t:111-s:1-e:2"
    profile = webdriver.FirefoxProfile()
    profile.set_preference("permissions.default.image", 2)
    driver = webdriver.Firefox(executable_path=r'./geckodriver', firefox_profile=profile, options=options)
    chunk_urls = []

    try:
        chunk_urls = get_chunk_links(driver, url)
    finally: driver.close()

    if chunk_urls:
        print('rabotaet')
        download_episode(chunk_urls)
        make_file(chunk_urls)

