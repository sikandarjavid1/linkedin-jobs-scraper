import pandas as pd
import os
from selenium import webdriver

from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def login():
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    options.add_argument ("start -maximized")
    browser= webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=options)
    #Add Linkedin Cred
    your_email=''
    your_password=''
    try:
        browser. get( "https://www.linkedin.com/uas/login")
        elementID = browser.find_element('id', 'username')
        elementID.send_keys(your_email)
        elementID = browser.find_element('id', 'password' )
        elementID.send_keys(your_password)
        elementID.submit()
        return browser
    except Exception as e:
        raise Exception("Can't able to login")
    
def ensure_empty_directory(directory_path):
    if os.path.exists(directory_path):  # Check if directory exists
        if os.listdir(directory_path):  # Check if directory is not empty
            # Empty the directory
            for file in os.listdir(directory_path):
                file_path = os.path.join(directory_path, file)
                try:
                    if os.path.isfile(file_path):
                        os.remove(file_path)
                    elif os.path.isdir(file_path):
                        os.rmdir(file_path)
                except Exception as e:
                    print(f"Failed to delete {file_path}: {e}")
    else:
        # Create the directory
        try:
            os.makedirs(directory_path, exist_ok=True)
            print(f"Directory created at {directory_path}")
        except Exception as e:
            print(f"Failed to create directory at {directory_path}: {e}")

def extract_jd(csv_file_path,driver):
    linkedin_urls=pd.read_csv(csv_file_path).head(15)

    directory_path = r"C:\Users\Administrator\Desktop\microservices\fetchprofile\scraping_linkedin_jobs\JD_Scrapped"
    ensure_empty_directory(directory_path)

    for idx,i in enumerate(linkedin_urls.href):
        print(i)
    #     driver = login()

        driver.implicitly_wait(10)
        driver.get(i)
        driver.implicitly_wait(10)
        try:

            xpath='//*[@id="ember38"]'
            button=driver.find_element(By.XPATH, xpath).click()
            driver.implicitly_wait(10)
            xpath='//*[@id="job-details"]/span'
            y=driver.find_element(By.XPATH, xpath).text

            with open(f'{directory_path}/{linkedin_urls.company[idx]}_{linkedin_urls.title[idx]}.txt','w') as file:
                file.write(y)
            # print(y)
            # print('\n'*10)
        except:
            pass