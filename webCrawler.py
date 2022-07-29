from lib2to3.pgen2 import driver
from pickle import FALSE, TRUE
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, json

# define ur own account and password of instagram
IG_LINK = "https://www.instagram.com/"
UR_ACCOUNT = "Input your instagram account"
UR_PASSWORD = "Input your instagram password"
target_username = "the instagram username you want to give likes to"
target_username_link = IG_LINK + target_username

# function
def checkAndGiveLike(like_btn):
    # if no like has been given then give like to post, and vice versa
    try:      
        print("check like status")
        like_status = WebDriverWait(chrome, 2).until(
            EC.presence_of_element_located((By.XPATH, "//*[@aria-label=\"收回讚\"]"))
        )                      
        time.sleep(1)
        print("already has like")                            
    except:
        print("give like to post")
        like_btn.click()
        
# check if the current version of chromedriver exists, if not download it automatically, then add it to current directory
chromedriver_autoinstaller.install(cwd=TRUE)
chrome = webdriver.Chrome()
chrome.get(IG_LINK)

# wait for account field to appear on screen
element = WebDriverWait(chrome, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )

# find HTML element of account, password fields and login button
username = chrome.find_element(By.NAME, "username")
password = chrome.find_element(By.NAME, "password")
login_btn = chrome.find_element(By.XPATH, "/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button")

# login to instagram
print("type in username")
username.send_keys(UR_ACCOUNT)
time.sleep(1) # imitate real person
print("type in password")
password.send_keys(UR_PASSWORD)
time.sleep(1)
print("login to instagram")
login_btn.click()

# wait for notifications to appear on page and then click the ignore buttons
element = WebDriverWait(chrome, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/section/main/div/div/div/div/button"))
    )
print("clicked the not-store button")
chrome.find_element(By.XPATH, "/html/body/div[1]/section/main/div/div/div/div/button").click()
element = WebDriverWait(chrome, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[2]"))
    )
time.sleep(1)
print("click ignore notification button")
chrome.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[2]").click()
time.sleep(2)

# search target instagram account
print("goto target instagram user")
chrome.get(target_username_link)
element = WebDriverWait(chrome, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "_aagw"))
    )
latest_post = chrome.find_element(By.XPATH, "(//div[@class = '_aagw'])[1]")
print("click on latest post")
latest_post.click()
element = WebDriverWait(chrome, 10).until(
        EC.presence_of_element_located((By.XPATH, "(//button[@class = '_abl-'])[4]"))
    )
like_btn = chrome.find_element(By.XPATH, "(//button[@class = '_abl-'])[4]")
next_post_btn = chrome.find_element(By.XPATH, "(//button[@class = '_abl-'])[2]")
# give like if it's not given
checkAndGiveLike(like_btn)
time.sleep(2)
print("goto next post")
next_post_btn.click()

# start giving likes to every posts
while True:
    like_btn = WebDriverWait(chrome, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button"))
        )    
    checkAndGiveLike(like_btn)
    try:
        next_post_btn = chrome.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div[2]/button")
        time.sleep(1)
        print("goto next post")
        next_post_btn.click()
    except:
        print("this is the last post")
        break
    
print("finish giving likes")