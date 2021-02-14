from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import os
from bs4 import BeautifulSoup
import requests
from requests import Session
import json
from vkbottle import Bot
import vkbottle

def write(driver):
    os.remove("txt.txt")
    with open("txt.txt", "w", encoding="utf-8") as file:
        file.write(str(driver.page_source))

def none():
    driver = webdriver.Chrome('chrome/chromedriver.exe')
    driver.get("https://content-watch.ru/text/")
    write(driver)

    driver.find_element_by_xpath("//textarea[@name='text']").send_keys("[OLD] Shortcuts - Inferno")
    driver.find_element_by_css_selector("[role=button]").click()

    soup = BeautifulSoup(driver.page_source, features="html.parser")



from bs4 import BeautifulSoup
import requests


def main(url):
    r = requests.get(url)

    soup = BeautifulSoup(r.text, features="html.parser")

    r = soup.find_all("div", class_="player-wrapper")[0]
    r = str(r).split("\n")[0]

    print(r.split("rel")[1].replace('=', "").replace('"', "").replace(" >", ""))


if __name__ == "__main__":
    url = "https://www.looperman.com/loops/detail/209709/nick-mira-x-foreigngotem-type-melody-150bpm-hip-hop-electric-guitar-loop"
    main(url)