from seleniumwire import webdriver
from selenium.webdriver.firefox.options import Options
from time import sleep


if __name__ == '__main__':
    options = Options()
    options.add_argument('-headless')
    profile = webdriver.FirefoxProfile()
    profile.set_preference('permissions.default.image', 2)
    driver = webdriver.Firefox(executable_path=r'./geckodriver', firefox_profile=profile, options=options)
    driver.get('https://rezka.ag/cartoons/comedy/2136-rik-i-morti-2013.html#t:66-s:1-e:1')

    player = driver.find_element_by_id('player')
    driver.execute_script("arguments[0].scrollIntoView();", player)
    play_button = driver.find_element_by_xpath(
        '//pjsdiv[@id="oframecdnplayer"]/pjsdiv/pjsdiv/pjsdiv[@style="position: absolute; top: -15px; left: -21px; width: 42px; height: 30px; border-radius: 3px; background: rgb(29, 174, 236) none repeat scroll 0% 0%; opacity: 1; transition: opacity 0.1s linear 0s, background 0.1s linear 0s, transform 0.1s linear 0s; cursor: pointer; pointer-events: auto; transform: scale(2);"]'
    )
    play_button.click()
    # driver.wait_for_request('.m3u8', timeout=10)
    sleep(30)
    for request in driver.requests:
        if request.response.headers.get('content-type') == 'application/vnd.apple.mpegurl':
            print(
                request.url,
                request.response.status_code,
                # request.response.headers['Content-Type'],
                request.response.headers.get('content-type'),
                '\n',
                '\n',
                request,
                '\n',
                '\n',
                request.response,
                '\n',
                '\n',
                request.response.headers,
                '\n',
                '\n',
                request.headers,
            )
    
    #print(driver.page_source)
    driver.quit()
