from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
import time
import web
import subprocess
from web import click_element
from download_quizzes import download_quizzes
from solve_quizzes import solve_quizzes
import json
import multiprocessing
import random
import signal
import os
import sys
import argparse

if __name__ == '__main__':

    input("please ensure that you are using a vpn")

    # set up chrome driver
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_service = ChromeService(executable_path='/usr/bin/chromedriver')
    driver = webdriver.Chrome(service=chrome_service,options=chrome_options)
    wait = WebDriverWait(driver, 2)

    # go to the captcha demo
    driver.get("https://www.google.com/recaptcha/api2/demo")

    # press the button
    button = driver.find_element(By.XPATH,'//*[@id="recaptcha-anchor"]/div[1]')
    click_element(driver,see_score)


    time.sleep(4)

    driver.quit