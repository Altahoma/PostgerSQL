from selenium.webdriver import Firefox

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.support.ui import WebDriverWait

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

if __name__ == "__main__":
    profile = webdriver.FirefoxProfile()
    profile.set_preference("permissions.default.image", 2)
    
    
    options = Options()
    options.add_argument('-headless')
    #driver = Firefox(executable_path='geckodriver', options=options)
    #wait = WebDriverWait(driver, timeout=10)
    #driver.get('http://www.google.com')
    
    driver = webdriver.Firefox(executable_path=r'geckodriver', firefox_profile=profile, options=options)
    driver.get("https://rezka.ag/cartoons/comedy/2136-rik-i-morti-2013.html#t:66-s:1-e:1")
    player = driver.find_element_by_id('player')
    driver.execute_script("arguments[0].scrollIntoView();", player)
    #play_button = driver.find_element_by_xpath(
    #        '//pjsdiv[@id="oframecdnplayer"]/pjsdiv/pjsdiv/pjsdiv[@style="position: absolute; top: -15px; left: -21px; width: 42px; height: 30px; border-radius: 3px; background: rgb(29, 174, 236) none repeat scroll 0% 0%; opacity: 1; transition: opacity 0.1s linear 0s, background 0.1s linear 0s, transform 0.1s linear 0s; cursor: pointer; pointer-events: auto; transform: scale(2);"]'
    #        )
    #play_button = driver.find_element_by_xpath("//pjsdiv[@style='position: absolute; top: -15px; left: -21px; width: 42px; height: 30px; border-radius: 3px; background: rgb(29, 174, 236) none repeat scroll 0% 0%; opacity: 1; transition: opacity 0.1s linear 0s, background 0.1s linear 0s, transform 0.1s linear 0s; cursor: pointer; pointer-events: auto; transform: scale(2);']")
    #driver.switch_to.frame('pjsfrrscdnplayer')
    #play_button = driver.find_element_by_xpath("//pjsdiv[@style='position: absolute; top: -11.5px; left: -20px; width: 40px; height: 23px; border-radius: 2.3px; background: rgb(23, 35, 34) none repeat scroll 0% 0%; opacity: 0.7; transition: opacity 0.1s linear 0s, background 0.1s linear 0s, transform 0.1s linear 0s; cursor: pointer; pointer-events: auto; transform: scale(1.6);']")
    #current_series = driver.find_element_by_xpath("//li[@class='b-simple_episode__item active']")
    
    #wait.until(expected.visibility_of_element_located((By.NAME, 'q'))).send_keys('headless firefox' + Keys.ENTER)
    #wait.until(expected.visibility_of_element_located((By.CSS_SELECTOR, '#ires a'))).click()
    print(driver.page_source)
    driver.quit()
