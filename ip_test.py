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
from http_request_randomizer.requests.proxy.requestProxy import RequestProxy
from selenium.webdriver.common.proxy import Proxy, ProxyType

def worker(config_file):
    # connect to the respective VPN tunnel: 
    connect(config_file)

    # set up chrome driver
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_service = ChromeService(executable_path='/usr/local/bin/chromedriver')
    driver = webdriver.Chrome(service=chrome_service,options=chrome_options)

    # access the internet
    driver.get("https://www.wizard101.com/game")
    wait = WebDriverWait(driver, 2)


    # handle the cookies widget:
    try:
        # define xpath to the cookie widget
        cookieXpath = '//*[@id="onetrust-reject-all-handler"]'
        # Wait for "accept all cookies" widget to become visible
        wait.until(EC.visibility_of_element_located((By.XPATH,cookieXpath)))

        # if it becomes visible, grab the reject all button and press it
        cookie = driver.find_element(By.XPATH,cookieXpath)
        click_element(driver,cookie)
        
    except TimeoutException:
        # if a timeout exertion occurs because the widget doesn't appear, 
        # continue as normal
        print("cookie widget didn't appear")

    # wait
    input("waiting")

    driver.quit
    return


def connect(config_file,auth_file="ip_config_files/auth_user_pass.txt"):
    # sudo password
    with open(auth_file, "r") as file:
        sudo = file.readlines()[2]

    command = f'echo {sudo} | sudo -S openvpn --config "{config_file}" --auth-user-pass {auth_file}'
    subprocess.Popen(command, shell=True)
    input()
    return


if __name__ == '__main__':

    # Number of processes
    num_processes = 1


    # dir = "ip_config_files"
    # config_files = []
    # for fname in os.listdir(dir):
    #     if fname.endswith('.ovpn'):
    #         relative_path = dir + "/" + fname
    #         config_files.append(relative_path)
    # print(config_files)

    # connect(config_files[0])

    # Set up the proxy server
    PROXY = Proxy()
    PROXY.proxy_type = ProxyType.MANUAL
    PROXY.http_proxy = '139.227.109.43:44844'
    PROXY.ssl_proxy = '139.227.109.43:44844'



    # set up chrome driver
    chrome_options = Options()
    chrome_options.add_argument('--proxy-server=%s' % PROXY)
    chrome_service = ChromeService(executable_path='/usr/local/bin/chromedriver')
    driver = webdriver.Chrome(service=chrome_service,options=chrome_options)

    # access the internet
    driver.get("https://www.wizard101.com/game")
    input("pause")

    # # Create a process pool
    # pool = multiprocessing.Pool(processes=num_processes)

    # # Apply algorithm to each portion of the keys
    # pool.map(worker, config_files)

    # Close the process pool