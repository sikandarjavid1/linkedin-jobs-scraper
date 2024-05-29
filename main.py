from helper import *
from job_scrapper import *
import pandas as pd
import os
from selenium import webdriver

from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import WebDriverException
import time


#Use these variables to d change city or role accordingly
keywords='Marketing Data Analyst'
location='Berlin, Berlin, Germany'


keywords_encoded=quote(keywords)
location_encoded=quote(location)

url1=f'https://www.linkedin.com/jobs/search?keywords={keywords_encoded}&location={location_encoded}&geoId=106967730&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0'
url= 'https://www.linkedin.com/uas/login'
# job_info=find_profiles(url1)
# job_info.to_csv('sample_testing.csv')
linkedin_username = ''
linkedin_password = ''
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

#redirect to company's people section
try:
    driver.get(url)
except WebDriverException as e:
    print(f"Error occurred while navigating to the URL: {e}")

driver.maximize_window()
try:
#login to linkedin
    email_field = driver.find_element(By.ID, "username")
    email_field.send_keys(linkedin_username)

    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys(linkedin_password)

    sign_in_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    sign_in_button.click()
    try:
        WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.ID, "input__phone_verification_pin"))
        )
        print("Please enter the 2FA code manually and click verify.")
        
        # Pause execution to allow manual 2FA input and verification
        while True:
            try:
                WebDriverWait(driver, 10).until_not(
                    EC.visibility_of_element_located((By.ID, "input__phone_verification_pin"))
                )
                break
            except TimeoutException:
                print("Waiting for 2FA verification to complete...")

    except TimeoutException:
        print("No 2FA required or timeout exceeded.")
except Exception as e:
    print(f"Error occurred during login: {e}")

extract_jd('sample.csv',driver)