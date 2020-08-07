USERNAME = "USERNAME"
PASSWORD = "PASSWORD"
VERBOSE = True

import selenium
import time
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')

driver = webdriver.Chrome(executable_path='./chromedriver', chrome_options=chrome_options, service_args=["--verbose", "--log-path=/tmp/chromedriver.log"])
driver.implicitly_wait(1)

def connect():
  driver.get('https://aternos.org/go')
  if VERBOSE: print('at',driver.title)
  
  element = driver.find_element_by_id('user')
  element.send_keys(USERNAME)
  if VERBOSE: print('Username:', USERNAME)
  
  element = driver.find_element_by_id('password')
  element.send_keys(PASSWORD)
  if VERBOSE: print('Password:', ('*' * len(password)))
  
  element = driver.find_element_by_id('login')
  element.click()
  if VERBOSE: print('Logging in')
  
  time.sleep(1)
  element = driver.find_element_by_class_name('server')
  element.click()
  
  time.sleep(1)
  if VERBOSE: print('On server page')
  if VERBOSE: print('Connected!')
  
  
def status():
  return driver.find_element_by_class_name('statuslabel-label').get_attribute('innerHTML')
  
def player_count():
  return driver.find_element_by_class_name('statusplayerbadge').get_attribute('innerHTML')


