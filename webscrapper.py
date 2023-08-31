import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from oauth2client.service_account import ServiceAccountCredentials
import gspread
import time


driver = webdriver.Chrome()
driver.get("http://quotes.toscrape.com/")

# time.sleep(20)

scopes = [
    'http://www.googleapis.com/auth/spreadsheets'
    'http://www.googleapis.com/auth/drive'
]

Credentials = ServiceAccountCredentials.from_json_keyfile_name('auth.json')
file = gspread.authorize(credentials=Credentials)
sheet = file.open("Web_Scrapper")

sheet = sheet.sheet1



for i in range(1, 9):
    Quote = driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/div["+str(i)+"]/span[1]").text
    Quote_by = driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/div["+str(i)+"]/span[2]/small").text
    tags = driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/div["+str(i)+"]/div").text

    print(Quote)
    print(Quote_by)
    print(tags)


    sheet.update_acell('A'+str(i+1), Quote)
    sheet.update_acell('B'+str(i+1), Quote_by)
    sheet.update_acell('C'+str(i+1), tags)