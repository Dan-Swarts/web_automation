from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import json
import random

# will click on an element, with added delay
def click_element(driver,element,min=1.3,max=2):
    actions = ActionChains(driver)
    
    actions\
    .pause(random.uniform(min, max))\
    .move_to_element(element)\
    .pause(random.uniform(1.4, 1.6))\
    .click()\
    .perform()

    return None

# Human-like typing
def type(actions,element,input):
    actions\
    .move_to_element(element)\
    .pause(random.uniform(0.1, 0.3))\
    .click()\
    .perform()

    for char in input:
        element.send_keys(char)
        time.sleep(random.uniform(0.08, 0.12))
    return None

def login(driver,uid):

    """
    logs into wizard101

    Inputs:
        - driver: the selenium website driver which is tuned into the wizard101 trivia page
        - user: a dictionary with all information about one particular account, such as username and password.
    """

    # acess the accounts
    with open('accounts.json') as f:
        accounts = json.load(f)

    actions = ActionChains(driver)

    # find a user and run the algorithm on it
    user = accounts[uid]

    # grab information from user dictionary
    username = user["name"]
    password = user["password"]
    
    # identify login fields 
    loginUserName = driver.find_element(By.ID,"loginUserName")
    loginPassword = driver.find_element(By.ID,"loginPassword")

    # fill in the login fields
    type(actions,loginUserName,username)
    type(actions,loginPassword,password)
    # loginUserName.send_keys(username)
    # loginPassword.send_keys(password)

    # find the login button
    button = driver.find_element(By.CLASS_NAME,"wizardButtonInput")
    
    
    # mouse over the button and press it
    actions = ActionChains(driver)
    click_element(driver,button)
    
    return None

def logout(driver,uid):

    """
    records the number of crowns and logs out of wizard101 account

    Inputs:
        - driver: the selenium website driver which is tuned into the wizard101 trivia page
        - user: a dictionary with all information about one particular account, such as username and password.
    """

    # access the accounts
    with open('accounts.json') as f:
        users = json.load(f)

    # find a user and run the algorithm on it
    user = users[uid]

    actions = ActionChains(driver)

    # go to account settings
    account = driver.find_element(By.ID,"kiAccountsLink")
    click_element(driver,account)

    # record crown balance: 
    balance = driver.find_element(By.CLASS_NAME,"crownsbalance").text
    balance = int(balance.replace(',','').replace(' ',''))
    user["crowns"] = balance

    # record that this user is solved
    user["solved"] = True

    # update json with balance
    with open('accounts.json', 'w') as file:
        json.dump(users, file, indent=4)

    # go back to home page
    time.sleep(1.6)
    driver.get("https://www.wizard101.com/game/trivia")

    # find the logout button
    button = driver.find_element(By.ID,"logoutLink")
    click_element(driver,button)
    
    return None


def identify_quizzes(driver):
    """
    identify all available quizzes 

    Inputs:
        - driver: the selenium website driver which is tuned into the wizard101 trivia page
        - solved_quizzes: a list of the quizzes to exclude from the output

    Outputs:
        - a dictionary: the key is the name of the quiz. the value is the element, clicking on which will lead to that quiz.
    """

    quiz_dict = {}
    
    # identify quiz elements 
    quiz_names = driver.find_elements(By.CLASS_NAME,'darkerparchment_headermiddle')
    quiz_elements = driver.find_elements(By.CLASS_NAME,'thumb')
    
    
    # append all quizzes to output:
    for i in range(len(quiz_names)):
        name = quiz_names[i].text
        quiz = quiz_elements[i]

        # cannot do spelling quizzes. this is due to the implementation of dictionaries
        # as a part of the quiz solving process: since spelling quizzes' questions are
        # not unique, they can't key to the right answer.
        if "spelling" not in name : 
            quiz_dict[name] = quiz

            # will stop with the first 10 quizzes. this is because 
            # only 10 quizzes can be don every day.
            if(len(quiz_dict) >= 10):
                return quiz_dict

    return quiz_dict


def download_quiz(driver,quiz_name):

    answer_dict = {}
    actions = ActionChains(driver)
    wait = WebDriverWait(driver, 13)
    # reward_text = driver.find_element(By.XPATH,'//*[@id="quizFormComponent"]/div[3]/div[2]')

    for i in range(12):
        # identify the question:
        try:
            question = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="quizContainer"]/table[2]/tbody/tr[2]/td[2]/div[1]'))).text
        except:
            input("what happened?")

        answer_text = []

        
        # wait for the answers to become fully opaque:
        next_question = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="nextQuestion"]/div')))
        

        # get all answers
        answers = driver.find_elements(By.CLASS_NAME,"answerText")

        for answer in answers:
            answer_text.append(answer.text)


        answer_dict[question] = answer_text

        # select the first answer:
        checkboxes = driver.find_elements(By.CLASS_NAME,"largecheckbox")
        click_element(driver,checkboxes[0])
        click_element(driver,next_question)

    # click see score
    see_score = driver.find_element(By.XPATH,'//*[@id="quizFormComponent"]/div[3]/div[1]/div[2]/a')
    click_element(driver,see_score)

    fname = 'quiz_answers/' + quiz_name + '.json'
    # open the JSON file for writing
    with open(fname, 'w') as file:
        # write the modified dictionary back to the file
        json.dump(answer_dict,file,indent=4)

    # wait for the page to load
    try:
        # define xpath to the question
        claim_reward = wait.until(EC.visibility_of_element_located((By.ID, 'submit')))
        print("we found it")
        
    except TimeoutException:
        # if a timeout exception occurs because the widget doesn't appear, 
        # continue as normal
        input("please do the recaptcha")


    # bring it back to the home page
    another_one = driver.find_element(By.XPATH,'//*[@id="quizFormComponent"]/div[3]/div[2]/div/a')
    click_element(driver,another_one)

    # wait for the page to load
    try:
        # define xpath to the question
        home = '//*[@id="renderRegionDiv"]/tbody/tr[1]/td/div/div/div/h1'
        wait.until(EC.visibility_of_element_located((By.XPATH,home)))
        home = driver.find_element(By.XPATH,home)
        click_element(driver,home)

    except TimeoutException:
        # if a timeout exception occurs because the widget doesn't appear, 
        # continue as normal
        print("didn't appear")
    return None


def basic_captcha(driver):
    return None