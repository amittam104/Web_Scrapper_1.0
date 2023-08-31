import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from oauth2client.service_account import ServiceAccountCredentials
import gspread


driver1 = webdriver.Chrome()
driver2 = webdriver.Chrome()
driver1.get('http://quotes.toscrape.com/')
driver2.get('http://quotes.toscrape.com/page/2/')

scopes =[
    "http://www.googleapis.com/spreadsheets"
    "http://www.googleapis.com/drive"
]

Credentials = ServiceAccountCredentials.from_json_keyfile_name('auth.json')
file = gspread.authorize(credentials=Credentials)
sheet = file.open('Web_Scrapper')

sheet = sheet.sheet1

for i in range(1, 10):
    quote1 = driver1.find_element(By.XPATH, '/html/body/div/div[2]/div[1]/div['+str(i)+']/span[1]').text
    quote_by1 = driver1.find_element(By.XPATH, '/html/body/div/div[2]/div[1]/div['+str(i)+']/span[2]/small').text
    tags1 = driver1.find_element(By.XPATH, '/html/body/div/div[2]/div[1]/div['+str(i)+']/div').text
    
    print(quote1)
    print(quote_by1)
    print(tags1)

    print('')

    quote2 = driver2.find_element(By.XPATH, '/html/body/div/div[2]/div[1]/div['+str(i)+']/span[1]').text
    quote_by2 = driver2.find_element(By.XPATH, '/html/body/div/div[2]/div[1]/div['+str(i)+']/span[2]/small').text
    tags2 = driver2.find_element(By.XPATH, '/html/body/div/div[2]/div[1]/div['+str(i)+']/div').text

    print(quote2)
    print(quote_by2)
    print(tags2)

    sheet.update_acell('A'+str(i+1),quote1)
    sheet.update_acell('B'+str(i+1),quote_by1)
    sheet.update_acell('C'+str(i+1),tags1)

    sheet.update_acell('A1'+str(i+1),quote2)
    sheet.update_acell('B1'+str(i+1),quote_by2)
    sheet.update_acell('C1'+str(i+1),tags2)