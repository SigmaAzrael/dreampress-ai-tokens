from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge import service
import os
import time

options = webdriver.EdgeOptions()
options.use_chromium = True
options.add_argument('headless') # that is, run in the command line only, server run prep
# options.add_argument("start-maximized")
my_service=service.Service(r'msedgedriver')
options.page_load_strategy = 'eager' #do not wait for images to load
options.add_experimental_option("detach", True)
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-dev-shm-usage') # uses disk instead of RAM, may be slow, use it if You receive "driver Run out of memory" crashed browser message

s = 60 #time to wait for a single component on the page to appear, in seconds; increase it if you get server-side errors «try again later»

driver = webdriver.Edge(service=my_service, options=options)
action = ActionChains(driver)
wait = WebDriverWait(driver,s)
   
username = os.environ.get('LOGIN')
password = os.environ.get('KEY')

login_page = "https://www.dreampress.ai"
tokens_page = "https://www.dreampress.ai/library"

def god_click(driver, element): # 3 events
    try:
        if element.is_displayed() and element.is_enabled():
            element_id = element.get_attribute("id")
            
            driver.execute_script(f"""
                arguments[0].scrollIntoView();
                var element = document.getElementById('{element_id}');
                ['mousedown', 'mouseup', 'click'].forEach(function(evtType) {{
                    var event = new MouseEvent(evtType, {{
                        'view': window,
                        'bubbles': true,
                        'cancelable': true
                    }});
                    element.dispatchEvent(event);
                }});
            """, element)
        else:
            print("Element is not visible or not enabled for clicking.")
    except Exception as e:
        print(f"An error occurred: {e}")

def login():
    driver.get(login_page)
    time.sleep(5)
    
    first_login_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[contains(., "LOG IN/SIGN UP")]/parent::div')))
    god_click(driver, first_login_button) 
    
    try:
        second_login_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[contains(., "OR LOGIN HERE")]')))
        god_click(driver, second_login_button)
    except:
        pass 
    
    wait.until(EC.element_to_be_clickable((By.XPATH, '//input[type="email"]'))).send_keys(username)

    wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@type="password"]'))).send_keys(password)

    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(., "LOGIN")]')))
    god_click(driver, login_button)
    
def collect_tokens():
    try:
        collect_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[contains(., "🎁 COLLECT DAILY TOKENS")]/parent::div')))
        god_click(driver, collect_button)
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