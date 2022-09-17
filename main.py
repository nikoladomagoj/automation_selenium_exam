from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from array import *
import string
import random
import shutil
import requests
import time

import urllib.request
import base64

s = Service("C://bin/chromedriver.exe")
driver = webdriver.Chrome(service = s)

def Add_Remove(x,y): #1
    driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
    time.sleep(1) # added sleep function just for better overview
    for i in range(x):
        driver.find_element(By.XPATH,'//*[@id="content"]/div/button').click()  # adding new buttons //select and copy full xpath on selected button
    time.sleep(1)
    for i in range(y):
        driver.find_element(By.XPATH, '//*[@id="elements"]/button[1]').click() # removing new buttons
    time.sleep(1)

def DropDown(): #2
    driver.get("https://the-internet.herokuapp.com/dropdown")

    tag = driver.find_element(By.ID,"dropdown");
    count_option_tag = len(tag.find_elements(By.TAG_NAME,"option"));
    value = random.randint(2,count_option_tag)
    driver.find_element(By.XPATH, f"//*[@id='dropdown']/option[{value}]").click() #adding random int in range
    time.sleep(1)

def Dynamic(x,y):  #3 // x -wait duration in seconds, y - range of refresh times
    driver.get("https://the-internet.herokuapp.com/dynamic_content")
    wait = WebDriverWait(driver, x)
    img_list = []
    for i in range(y):
        try:
            l1 = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div[1]/div[1]/img'))).get_attribute("src") # 1.image
            img_list.append(l1)
            l2 = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div[2]/div[1]/img'))).get_attribute("src") # 2.image
            img_list.append(l2)
            l3 = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div[3]/div[1]/img'))).get_attribute("src") # 3.image
            img_list.append(l3)
            if(i == y-1):
                [print(img_list.count(x), x) for x in set(img_list)]
            driver.refresh()
        except Exception:
            print(str(i+1) + "." + "Error: Element not founded!")
            continue


def Alerts(text = None):   #4  // Using empty method will trigger random text in the prompt but adding string as parameter will display the text in the prompt
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    wait = WebDriverWait(driver, 10)
    letters = string.ascii_letters
    random_string = ''.join(random.choice(letters) for i in range(10))

    driver.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[1]/button').click() #JS ALert button
    wait.until(EC.alert_is_present())
    time.sleep(1)
    driver.switch_to.alert.accept()

    driver.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[2]/button').click() #JS Confirm button
    wait.until(EC.alert_is_present())
    time.sleep(1)
    driver.switch_to.alert.dismiss()

    driver.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[3]/button').click()  # JS Prompt button
    wait.until(EC.alert_is_present())

    if text == None:
        driver.switch_to.alert.send_keys(random_string)
        time.sleep(1)
        driver.switch_to.alert.accept()
        time.sleep(1)
    else:
        driver.switch_to.alert.send_keys(text)
        time.sleep(1)
        driver.switch_to.alert.accept()
        time.sleep(1)

def DOM(x):  #5
    driver.get("https://the-internet.herokuapp.com/challenging_dom")

    def TableData():
        result = []
        table = driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div/div[2]/table/tbody').get_attribute("textContent").split() #get all data from table and store as array
        for i in table:
            if str(x) in i:    #checks if string contains DOM('?')
                result.append(i)
        result.sort() # sorted ascendingly, for desc sort set-> sort(reverse=True)
        print(result)

    def ReturnAnswer():
        canv = driver.find_element(By.XPATH, '//*[@id="content"]/script').get_attribute("textContent") #remove -> /text() to fix the error (element is not an object)
        canv = canv.split("Answer: ",1)[1]  # geting the string number after "Answer: "
        canv = int(canv.split("'")[0])      # removing everything else after number and converting string to int
        print(canv)
        time.sleep(1)
        return canv

    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/div[1]/a[1]").click()  # qux button
    qux = ReturnAnswer()

    driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/div[1]/a[2]").click()  # buz ALert button
    buz = ReturnAnswer()

    driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/div[1]/a[3]").click()  # bar ALert button
    bar = ReturnAnswer()

    sum = qux + buz + bar
    print("SUM of all Answers: ")
    print(sum)
    TableData()

Add_Remove(5,4)     #1.Test // Add_Remove(<Add x times delete button>, <removes y times delete button>)
DropDown()          #2.Test
Dynamic(0,10)       #3.Test // Dynamic(<wait time>,<refresh count>)
Alerts()            #4.Test // You can add a text or leave empty brackets
DOM(7)              #5.test // Add a number or string