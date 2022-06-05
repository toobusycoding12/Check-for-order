#-------------------------------------------------------------------------------
# Imports
import csv
from selenium import webdriver
import time

#-------------------------------------------------------------------------------
# Setup

tokenid = 0

with open('data.csv', 'r') as csv_file:

    csv_reader = csv.reader(csv_file)

#-------------------------------------------------------------------------------
# Web Automation

    driver = webdriver.Chrome()
    driver.get('https://goblintown.wtf/mcgoblin/')

    time.sleep(5)

    enter = driver.find_element_by_xpath('//*[@id="Enter"]')
    enter.click()

    time.sleep(3)

    connect = driver.find_element_by_xpath('//*[@id="Connect"]')
    connect.click()

    time.sleep(10)

    for line in csv_reader:

        tokenid_field = driver.find_element_by_xpath('//*[@id="check"]')
        tokenid_field.click()
        tokenid_field.clear()
        time.sleep(1)
        tokenid_field.send_keys(line[0])

        time.sleep(1)

        submit = driver.find_element_by_xpath('//*[@id="Avail-Btn"]')
        submit.click()

        time.sleep(1)

        print(driver.find_element_by_xpath('//*[@id="Avail-Btn"]').text)








#-------------------------------------------------------------------------------
