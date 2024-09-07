import os
import pickle
import random
import requests
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

COOKIES_PATH = 'linkedin_cookies.pkl'

def wait_for_internet(timeout=5, retry_interval=10):
    """
    Waits for an active internet connection.

    Parameters:
    - timeout (int): The maximum time to wait for a response from the server in seconds.
    - retry_interval (int): The time to wait between retries in seconds.
    """
    while True:
        try:
            # Try to connect to a reliable website
            response = requests.get("https://www.google.com", timeout=timeout)
            if response.status_code == 200:
                print("Internet connection is available.")
                break  # Exit the loop if the internet is available
        except requests.ConnectionError:
            print("No internet connection. Retrying in {} seconds...".format(retry_interval))
            time.sleep(retry_interval)

def save_cookie(driver, path):
    cookies = driver.get_cookies()
    with open(path, 'wb') as filehandler:
        pickle.dump(cookies, filehandler)

def load_cookie(driver, path):
    with open(path, 'rb') as cookiesfile:
        cookies = pickle.load(cookiesfile)
    
    for cookie in cookies:
        driver.add_cookie(cookie)
    
    print('Using existing cookies.')
    return True

def setup_driver():
    service = Service('c:/Users/PMLS/chromedriver.exe') #replace with your chromedriver path
    driver = webdriver.Chrome(service=service)   
    return driver          

def login(driver):
    driver.get('https://www.linkedin.com/login')
    driver.implicitly_wait(3)
    time.sleep(random.uniform(2, 4))

    if os.path.exists(COOKIES_PATH):
        load_cookie(driver, COOKIES_PATH)
        driver.implicitly_wait(3)
        driver.refresh()
        try:
            password_field = driver.find_element(By.ID, 'password')
            time.sleep(random.uniform(1, 2))
            password_field.send_keys('21082003jz') #replace with you password
            time.sleep(random.uniform(1, 3))

            password_field.submit()
            input("Please solve the CAPTCHA manually, then press Enter to continue...")
        except:
            print("step skipped")    
    else:    
        email_field = driver.find_element(By.ID, 'username')
        time.sleep(random.uniform(1, 3))
        email_field.send_keys('i2cproject11@gmail.com') #replace with your email
        time.sleep(random.uniform(2, 1))

        password_field = driver.find_element(By.ID, 'password')
        time.sleep(random.uniform(1, 2))
        password_field.send_keys('21082003jz') #replace with you password
        time.sleep(random.uniform(1, 3))

        password_field.submit()
        time.sleep(2)
        input("Please solve the CAPTCHA manually, then press Enter to continue...")

        # First try-except block for the "try-another-way" step
        try:
            authenticator_link = driver.find_element(By.ID, 'try-another-way')
            authenticator_link.click()
            print("Navigating to the authenticator app page...")
        except Exception as e:
            print("Additional step not required:", e)

        time.sleep(3)

        # Second try-except block for the 2FA code input
        while True:
            try:
                twofa_field = driver.find_element(By.ID, 'input__phone_verification_pin')
                twofa_code = input("Enter your 2FA code: ")
                twofa_field.send_keys(twofa_code)
                twofa_field.submit()
                time.sleep(3)

                # Check if the alert for invalid code is present
                try:
                    alert_message = driver.find_element(By.XPATH, "//span[@role='alert']").text
                    if "The verification code you entered isn’t valid" in alert_message:
                        print("Invalid 2FA code. Please try again.")
                        continue
                except:
                    print("2FA code submitted successfully.")
                    break  
            except:
                print("No 2FA required or could not locate 2FA field.")
                break  # Exit the loop if no 2FA is required


        save_cookie(driver,COOKIES_PATH)
    return "login successful"

def random_delay(min_sec=2, max_sec=5):
    time.sleep(random.uniform(min_sec, max_sec))



if __name__ == "__main__":
    driver=setup_driver()
    login(driver)