import csv
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

with open('Data.csv', 'r') as csv_file:

    csv_reader = csv.reader(csv_file)

    for line in csv_reader:

        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get('http://localhost:5000/register')

        time.sleep(1)

        email = driver.find_element_by_xpath('//*[@id="email"]')
        email.send_keys(line[0])

        username = driver.find_element_by_xpath('//*[@id="username"]')
        username.send_keys(line[1])

        first_name = driver.find_element_by_xpath('//*[@id="firstName"]')
        first_name.send_keys(line[2])

        last_name = driver.find_element_by_xpath('//*[@id="lastName"]')
        last_name.send_keys(line[3])

        password = driver.find_element_by_xpath('//*[@id="password"]')
        password.send_keys(line[4])

        submit = driver.find_element_by_xpath('//*[@id="form"]/button')
        submit.click()