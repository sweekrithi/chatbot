import random

import re
import selenium
import io
import requests
import bs4
import urllib.request
import urllib.parse
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from _datetime import datetime
from selenium.webdriver.common.keys import Keys

print("Hi ! I'm TravelBud. Your friendly virtual tour guide :)")

def greeting(sentence):
    greeting_input = ("hello", "hola", "hi","greetings","hey")
    greeting_response = ["hi","hello there","hello","hola"]
    for word in sentence.split():
        if word.lower() in greeting_input :
            return random.choice(greeting_response)


flag = True
while (flag==True):
      user_response = input()
      user_response = user_response.lower()
      if ((user_response)!="bye") :
          if ((user_response)=="thank you") :
              flag=False
              print("You're welcome !")
          else :
            if (greeting(user_response)!=None) :
                print(greeting(user_response))

                l = input( "Please enter the city you would like to explore : " )
                g = input( "What would you like to check out ? Hotels or Restaurants or Places to visit ? " )
                options=webdriver.ChromeOptions()
                options.headless=False
                prefs={"profile.default_content_setting_values.notifications" :2}
                options.add_experimental_option("prefs",prefs)
                driver=webdriver.Chrome("C:/Users/Surendra/OneDrive/Documents/avi/chromedriver.exe")  #chromedriver path should be from your PC
                driver.maximize_window()
                time.sleep(2)
                driver.get("https://www.tripadvisor.in/")
                time.sleep(2)
                driver.find_element_by_xpath('//*[@id="lithium-root"]/main/div[1]/div[1]/div/div/div[3]/a').click()
                driver.find_element_by_xpath('/html/body/div[4]/div/form/input[1]').send_keys(l,Keys.RETURN)
                if g=="Hotels":
                    driver.find_element_by_xpath('//*[@id="search-filters"]/ul/li[2]/a').click()
                elif g=="Restaurants":
                    driver.find_element_by_xpath('//*[@id="search-filters"]/ul/li[4]/a').click()
                else:
                    driver.find_element_by_xpath('//*[@id="search-filters"]/ul/li[5]/a').click()
                time.sleep(2)

            else :
                flag=False
                print("Thank you for talking to me,bye !")


