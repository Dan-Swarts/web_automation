from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
import time
import json
from os.path import exists
import web
from web import click_element
import random

def solve_quiz(driver,quiz_name):
    # Load answers from the associated json file
    fname = 'quiz_answers/' + quiz_name + '.json'
    with open(fname, 'r') as file:
        answer_dict = json.load(file)

    # prepare variables
    actions = ActionChains(driver)
    wait = WebDriverWait(driver, 9999)
    update = False

    # 12 questions = loop 12 times
    for i in range(12):

        # get the question:
        question = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="quizContainer"]/table[2]/tbody/tr[2]/td[2]/div[1]'))).text

        # wait for the answers to become fully opaque:
        next_question = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="nextQuestion"]/div')))
        
        # get all answers
        possible_answers = [answer.text for answer in driver.find_elements(By.CLASS_NAME, "answerText")]

        # try to get the true answer from the answer dictionary. 
        try: 
            true_answer = answer_dict[question]

            # case 1: a list of possible answers exists in the dictionary.
            # no way to find the true one. guess.
            if type(true_answer) == list:
                index = 0

            # case 2: true answer exists in the dictionary. 
            else:
                index = possible_answers.index(true_answer)

        # case 3: this question hasn't been recorded among the answers. prepare to add it. 
        # guess.
        except KeyError:
            answer_dict[question] = possible_answers
            update = True
            index = 0

        # find all possible selections
        checkboxes = driver.find_elements(By.CLASS_NAME,"largecheckbox")


        # pick the correct one, or guess
        click_element(driver,checkboxes[index])

        # move on to the next question
        click_element(driver,next_question)

    # update the json file if a new question was found
    if(update):
        with open(fname, 'w') as file:
            json.dump(answer_dict,file,indent=4)

    # click to see score
    see_score = driver.find_element(By.XPATH,'//*[@id="quizFormComponent"]/div[3]/div[1]/div[2]/a')
    click_element(driver,see_score)

    # Go to proper iframe
    iframe = wait.until(EC.visibility_of_element_located((By.ID, "jPopFrame_content")))
    driver.switch_to.frame(iframe)

    # click button
    claim_your_reward = wait.until(EC.visibility_of_element_located((By.ID, "submit")))
    click_element(driver,claim_your_reward)

    # switch back to defaut iframe
    driver.switch_to.default_content()
    
    # bring it back to the home page
    another_one = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="quizFormComponent"]/div[3]/div[2]/div/a')))
    click_element(driver,another_one)
    
    return None


def solve_quizzes(driver,uid):

    wait = WebDriverWait(driver, 9999)

    # login to the account
    web.login(driver,uid)
    
    # go to trivia 
    earn_crowns = wait.until(EC.visibility_of_element_located((By.ID,'earnCrownsLink')))
    click_element(driver,earn_crowns)

    play_trivia = driver.find_element(By.XPATH,'//*[@id="img_8ad6a41245d5c0cb01461af1244b1400"]')
    click_element(driver,play_trivia)

    
    # the skip variable is enacted if a quiz has already been completed today. this will cause 
    # the bot to skip one iteration in order to proceed without causeing an error
    skip = False

    for i in range(1,11):

        if not skip:
            # go to educational trivia
            educational_trivia = driver.find_element(By.XPATH,'//*[@id="renderRegionDiv"]/tbody/tr[5]/td/div/table[2]/tbody/tr[2]/td[2]/p/b/a')
            click_element(driver,educational_trivia)

        skip = False

        # get the quiz:
        q_name = driver.find_elements(By.CLASS_NAME,'darkerparchment_headermiddle')[i].text
        q_element = driver.find_elements(By.CLASS_NAME,'thumb')[i]

        # open the quiz
        click_element(driver,q_element)


        # this exeption is meant to catch the error caused when a quiz has already been completed. 
        # this will cause the page not to not go to the quiz, since it is unavailable. then the 
        # elements of the quiz will not be found.
        try:
            question = driver.find_element(By.CLASS_NAME,'quizQuestion')
        except NoSuchElementException as e:
            skip = True
            continue
        
        solve_quiz(driver,q_name)
    

    web.logout(driver,uid)
    return



