from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import os
import time

s = 60 #time to wait for a single component on the page to appear, in seconds; increase it if you get server-side errors «try again later»

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('disable-gpu')
options.add_experimental_option("detach", True)
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-dev-shm-usage')

# Instantiate the Service object with the path to the Chrome driver
chrome_service = ChromeService(ChromeDriverManager().install())

# Then pass the service and options like this
driver = webdriver.Chrome(service=chrome_service, options=options)

action = ActionChains(driver)
wait = WebDriverWait(driver,s)
   
username = os.environ.get('LOGIN')
password = os.environ.get('KEY')

login_page = "https://www.dreampress.ai"
tokens_page = "https://www.dreampress.ai/library"

def login():
    try:
        driver.get(login_page)
        time.sleep(10)
        eighteen_button =  wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(., "Agree and Enter")]')))
        eighteen_button.click()
        
        login_start_button =  wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(., "Login/Signup")]')))
        login_start_button.click()
        
        second_login_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[contains(@class,"bubble-r-container flex row")]/div[contains(., "Log In")]')))
         
        second_login_button.click()
        
        # try:
        #     second_login_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[contains(., "OR LOGIN HERE") and @class="bubble-element Text cmaUaOaJ clickable-element"]')))
        #     second_login_button.click()
        # except:
        #     pass 
        
        wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@type="email"]'))).send_keys(username)

        wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@type="password"]'))).send_keys(password)

        login_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[contains(@class, "bub)]button[contains(., " Login")]')))
        login_button.click()
        
    except Exception as e:
        # driver.save_screenshot('error.png')
        print(e)
        # You can also dump the current HTML to see what's on the page
        print(driver.page_source)
        raise
    
def collect_tokens():
    try:
        # collect_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[contains(., "🎁 COLLECT DAILY TOKENS")]/parent::div[@class="bubble-element Text cmaSaZr bubble-r-vertical-center clickable-element"]')))
        collect_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(., "Free tokens")]')))
        collect_button.click()
        time.sleep(5)
        return "success"
    except:
        return 1
           
def main():
    login()
    time.sleep(5)
    driver.get(tokens_page)
    time.sleep(5)

    if (collect_tokens() == "success"): 
        print("Your daily tokens are successfully collected on dreampress.ai! \n \nSincerely Yours, \nNAKIGOE.ORG\n")
    else:
        print("Something went wrong, dreampress.ai HTML might have been updated, so please update button selectors in the COLLECT-TOKENS.PY code.\n")
    driver.close()
    driver.quit()
main()