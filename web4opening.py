# -*- coding: utf-8 -*-
"""
Created on Wed May 20 05:05:10 2020

@author: Amsa
"""

# -*- coding: utf-8 -*-
"""
Created on Tue May 19 05:33:07 2020

@author: Amsa
"""
import pandas as pd
#from pynput.keyboard import Key, Controller
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
#from urllib.request import urlopen
#from bs4 import BeautifulSoup
import ssl
import csv

#keyboard=Controller()

path="C:\Program Files (x86)\chromedriver.exe"
driver=webdriver.Chrome(path)

#driver.get('http://tcbbazardor.com/home/index/2018/04/16')
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

'''
csv_file = open('cms_A_I_N.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['newsName','imgsrc', 'link'])
'''
#excelReader = pd.ExcelWriter('University.xlsx', engine='xlsxwriter')
tim=0
'''

while(i):
    try:
        print(excel['ielts'][i])
    except:
        break
    i+=1
'''
#################################################from prompt
def prompt():
    path="C:\Program Files (x86)\chromedriver.exe"
    driver=webdriver.Chrome(path)
    while(1):
        uni=input('Enter University name: ')
        try:
            #driver.close()
            driver=webdriver.Chrome(path)
            print(uni+ ' loading...')
            #######################################################################1st tab
            driver.get('https://www.google.com/')
            searchbox=driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
            searchbt=driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]')
            searchbox.send_keys(uni+' MS fall 2023 deadline for international')
            searchbt.click()
            time.sleep(tim)
            ######################################################################2nd tab
            driver.execute_script("window.open('about:blank', 'secondtab');")
            driver.switch_to.window("secondtab")
            driver.get('https://www.google.com/')
            searchbox=driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
            searchbt=driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]')
            searchbox.send_keys(uni+' GRE requirements for computer science fall 2023')
            searchbt.click()
            time.sleep(tim)
            #######################################################################3rd tab
            driver.execute_script("window.open('about:blank', 'thirddtab');")
            driver.switch_to.window("thirddtab")
            driver.get('https://www.google.com/')
            searchbox=driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
            searchbt=driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]')
            searchbox.send_keys(uni+' IELTS requirements for computer science fall 2023')
            searchbt.click()
            time.sleep(tim)
            ######################################################################4th tab
            driver.execute_script("window.open('about:blank', 'fourthtab');")
            driver.switch_to.window("fourthtab")
            driver.get('https://www.google.com/')
            searchbox=driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
            searchbt=driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]')
            searchbox.send_keys(uni+' computer science faculty')
            searchbt.click()
            driver.execute_script("window.open('about:blank', 'fifthtab');")
            driver.switch_to.window("fifthtab")
            driver.get('https://www.google.com/')
            driver.close()
            time.sleep(tim)
        except:
            print(uni+ ' loading...')
#################################################from execl

def exce():
    path="C:\Program Files (x86)\chromedriver.exe"
    driver=webdriver.Chrome(path)
    excel=pd.read_excel('UniversityName.xlsx')
    i=1
    while(i): 
        try:
            #driver.close()
            driver=webdriver.Chrome(path)
            uni=excel["Name"][i-1]
            print(uni+ ' loading...')
            
            #######################################################################1st tab
            driver.get('https://www.google.com/')
            searchbox=driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
            searchbt=driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]')
            searchbox.send_keys(uni+' MS fall 2023 deadline for international')
            searchbt.click()
            time.sleep(tim)
            
            ######################################################################2nd tab
            driver.execute_script("window.open('about:blank', 'secondtab');")
            driver.switch_to.window("secondtab")
            driver.get('https://www.google.com/')
            searchbox=driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
            searchbt=driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]')
            searchbox.send_keys(uni+' GRE requirements for computer science fall 2023')
            searchbt.click()
            time.sleep(tim)
            #######################################################################3rd tab
            driver.execute_script("window.open('about:blank', 'thirdtab');")
            driver.switch_to.window("thirdtab")
            driver.get('https://www.google.com/')
            searchbox=driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
            searchbt=driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]')
            searchbox.send_keys(uni+' IELTS requirements for computer science fall 2023')
            searchbt.click()
            time.sleep(tim)
            ######################################################################4th tab
            driver.execute_script("window.open('about:blank', 'fourthtab');")
            driver.switch_to.window("fourthtab")
            driver.get('https://www.google.com/')
            searchbox=driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
            searchbt=driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]')
            searchbox.send_keys(uni+' computer science faculty')
            searchbt.click()
            time.sleep(tim)
        except:
            print('next...')
            
        driver.execute_script("window.open('about:blank', 'fifthtab');")
        driver.switch_to.window("fifthtab")
        driver.get('https://www.google.com/')
        driver.close()
        #i+=1
        while(1):
            if(input("Do you want to go to next university? press 'y': ")=='y'):
                i+=1
                break
        
if(input("Do you want to input university name manually? press 'y': ")=='y'):
    prompt()
else:
    exce()