#Selenium button pressing
from selenium import webdriver
from selenium.webdriver.common.by import By
import sys
import bs4
import requests
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)







url ='https://finance.yahoo.com/quote/AAPL/financials?p=AAPL'







def test(url):

    global browser
    browser = webdriver.Chrome()
    browser.get('https://finance.yahoo.com/quote/AAPL/financials?p=AAPL')
# working!
    cookiesButton = browser.find_element(By.CSS_SELECTOR,'#consent-page > div > div > div > form > div.wizard-body > div.actions.couple > button')

    cookiesButton.click()

    opExButton = browser.find_element(By.XPATH,'//*[@id="Col1-1-Financials-Proxy"]/section/div[3]/div[1]/div/div[2]/div[4]/div[1]/div[1]/div[1]/button')

    opExButton.click()
    elem = browser.find_element(By.XPATH,'//*[@id="Col1-1-Financials-Proxy"]/section/div[3]/div[1]/div/div[2]/div[4]/div[2]/div[1]/div[1]/div[1]/div[1]/span').text

    print (elem)
#prints Selling General and Administrative: link selenium with O's programme
#for final results
#Test

#Does it find the breakdown of values?
 
 


test(url)
