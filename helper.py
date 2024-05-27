#Import Packages
from selenium import webdriver
from urllib.parse import quote
import time
import pandas as pd
import os

#Import Packages

from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

def  find_profiles(url1):

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.get(url1)


    y=driver.find_element(By.XPATH, '//*[@id="main-content"]/div/h1/span[1]').text
    time.sleep(5)
    n=pd.to_numeric(y)

    #Loop to scroll through all jobs and click on see more jobs button for infinite scrolling
    i = 2
    while i <= int((n+200)/25)+1:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        i = i + 1

        try:

    #         default_xpath="//button[@aria-label='Load more results']"
    #         x_path_='//*[@id="main-content"]/section[2]/button'
    #         send=driver.find_element_by_xpath(x_path_)
    #         driver.execute_script("arguments[0].click();", send)
    #         time.sleep(3)

            buu=driver.find_elements(By.TAG_NAME,"button")
            x=[btn for btn in buu if btn.text=="See more jobs"]
            for btn in x:
                driver.execute_script("arguments[0].click();", btn)
                time.sleep(3)

        except:
            pass
            print('no more scroll')
            time.sleep(5)

    #Create empty lists for company name and job title
    companyname= []
    titlename= []

    try:
        for i in range(n):
    #         company=driver.find_elements('base-search-card__subtitle')[i].text
            company=driver.find_elements(By.CLASS_NAME, "base-search-card__subtitle")[i].text

            companyname.append(company)

    except IndexError:
        print("no")


    #Find title name and append it to the blank list
    try:
        for i in range(n):
    #         title=driver.find_elements_by_class_name('base-search-card__title')[i].text
            title=driver.find_elements(By.CLASS_NAME, "base-search-card__title")[i].text
            titlename.append(title)



    except IndexError:
        print("no")

    #Create dataframe for company name and title
    companyfinal=pd.DataFrame(companyname,columns=["company"])
    titlefinal=pd.DataFrame(titlename,columns=["title"])

    #Join the two lists
    temp=companyfinal.join(titlefinal)
    print(temp)

    #Find job links and append it to a list

    # jobList = driver.find_elements_by_class_name('base-card__full-link')
    jobList=driver.find_elements(By.CLASS_NAME, "base-card__full-link")

    hrefList = []
    for e in jobList:
        hrefList.append(e.get_attribute('href'))

    hreffinal=pd.DataFrame(hrefList,columns=["href"])

    final_df=temp.join(hreffinal)
    driver.close()
    
    return final_df

