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

def worker(uids):
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
        # if a timeout exeption occurs because the widget doesn't appear, 
        # continue as normal
        print("cookie widget didn't appear")

    # solve the quizzes
    for uid in uids:
        solve_quizzes(driver,uid)

    driver.quit
    return

def solved_false():
    # Open the accounts
    with open("accounts.json", "r") as file:
        accounts = json.load(file)

    # Update the each account to unsolved
    for value in accounts.values():
        value['solved'] = False

    # Write the updated data back to the same file
    with open("accounts.json", "w") as file:
        json.dump(accounts, file, indent=4)
    return


if __name__ == '__main__':

    # take in arguments:
    parser = argparse.ArgumentParser(description='ALL')
    parser.add_argument('--reset',type=bool,default=False)
    parser.add_argument('--num_processes',type=int,default=1)
    args = parser.parse_args()

    # optional: set solved status to False. do this when running for the first time each day.
    if args.reset:
        solved_false()
        exit()

    # Number of processes
    num_processes = args.num_processes

    # grab all acccounts that need to do the trivia for
    with open('accounts.json','r') as file:
        accounts = json.load(file)
        # grab every UID that isn't solved:
        keys = []
        for key, value in accounts.items():
            if value['solved'] == False:
                keys.append(key)


    # Split the work between processes:
    key_parts = [[] for _ in range(num_processes)]

    # populate the array using modulo
    for i, key in enumerate(keys):
        index = i % num_processes
        key_parts[index].append(key)

    input("please ensure that you are using a vpn")

    # Create a process pool
    pool = multiprocessing.Pool(processes=num_processes)

    # Apply algorithm to each portion of the keys
    pool.map(worker, key_parts)

    # Close the process pool
    pool.close()
    pool.join()