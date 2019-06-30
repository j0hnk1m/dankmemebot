import os
import sys
import stat
import urllib.request
import zipfile
import time
import re
from selenium.webdriver import Chrome


# User's Reddit credentials
USERNAME = 'sir_justkidding'
PASSWORD = 'Rjohnkim0414'


def get_api_keys():
    pass_chrome_binary()
    os.environ['webdriver.chrome.driver'] = './chromedriver'
    driver = Chrome('./chromedriver')

    # Log in
    driver.get('https://www.reddit.com/prefs/apps')
    driver.find_element_by_id("loginUsername").send_keys(USERNAME)
    driver.find_element_by_id("loginPassword").send_keys(PASSWORD)
    driver.find_element_by_xpath("//button[@class='AnimatedForm__submitButton'][@type='submit']").submit()

    # Create dummy app
    time.sleep(4)
    driver.refresh()
    driver.find_element_by_id("create-app-button").click()
    driver.find_element_by_xpath("//*[@id='create-app']/table/tbody/tr[1]/td/input").send_keys('test')
    driver.find_element_by_xpath("//*[@id='app_type_script']").click()
    driver.find_element_by_xpath("//*[@id='create-app']/table/tbody/tr[5]/td/textarea").send_keys('for DankMemeBot')
    driver.find_element_by_xpath("//*[@id='create-app']/table/tbody/tr[7]/td/input").send_keys('http://localhost:8080')
    driver.find_element_by_xpath("//*[@id='create-app']/button").submit()

    # Regex Oath2 access token and secret key
    app_details = driver.find_elements_by_id("developed-apps")[-1].text
    access_token = re.findall('personal use script\\n(.+)\\n', app_details)[-1]
    secret = re.findall('\\nsecret(.+)\\n', app_details)[-1]

    return access_token, secret


def pass_chrome_binary():
    if not os._exists('./chromedriver'):
        platform = sys.platform

        if platform == 'linux':
            system = 'linux64.zip'
        elif platform == 'darwin':
            system = 'mac64.zip'
        elif platform == 'win32':
            system = 'win32.zip'
        else:
            sys.exit('Error: no chromedriver available for your system')

        url = 'https://chromedriver.storage.googleapis.com/74.0.3729.6/chromedriver_' + system
        urllib.request.urlretrieve(url, './chromedriver.zip')
        with zipfile.ZipFile('./chromedriver.zip', 'r') as zip_ref:
            zip_ref.extractall('.')

        try:
            os.remove('./chromedriver.zip')
        except FileNotFoundError:
            print('Chrome driver zip file not found.')

        os.chmod('./chromedriver', stat.S_IRWXU)
