from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
import time
from os.path import exists
import web
import random

def download_quizzes(driver):
    actions = ActionChains(driver)
    
    while(True):
        # go to educational trivia
        educational_trivia = driver.find_element(By.XPATH,'//*[@id="renderRegionDiv"]/tbody/tr[5]/td/div/table[2]/tbody/tr[2]/td[2]/p/b/a')
        actions.move_to_element(educational_trivia).click().perform()

        # get all potential quizzes:
        quiz_dict = web.identify_quizzes(driver)

        print(quiz_dict.keys())
        
        # select the right quiz:
        q_name = random.choice(list(quiz_dict.keys()))

        # cannot do spelling quizzes. this is due to the implementation of dictionaries
        # as a part of the quiz solving process: since spelling quizzes' questions are
        # not unique, they can't key to the right answer. Additionally, will not open
        # a quiz if there is already an answer key.
        while "Spelling" in q_name or exists('quiz_answers/' + q_name + '.json'):
            print("cannot do " + q_name)
            quiz_dict.pop(q_name)
            if len(quiz_dict) == 0:
                return 
            q_name = random.choice(list(quiz_dict.keys()))

        print("accessing {} quiz".format(q_name))
        actions.move_to_element(quiz_dict[q_name]).click().perform()

        web.download_quiz(driver,q_name)

