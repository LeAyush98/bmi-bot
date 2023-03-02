import os
from selenium import webdriver
from selenium.webdriver.common.by import By

gomez = webdriver.Chrome()

gomez.get("https://www.calculator.net/bmi-calculator.html")

age = gomez.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[4]/div[2]/table/tbody/tr/td/table[1]/tbody/tr[1]/td[2]/input")
age.clear()

input_age = int(input("What is your age? "))

age.send_keys(input_age)

height = gomez.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[4]/div[2]/table/tbody/tr/td/table[3]/tbody/tr[1]/td[2]/input")
height.clear()

input_height = int(input("Please enter your height in cm "))

height.send_keys(input_height)

weight = gomez.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[4]/div[2]/table/tbody/tr/td/table[3]/tbody/tr[2]/td[2]/input")
weight.clear()

input_weight = int(input("Please enter your weight in kg fatty "))

weight.send_keys(input_weight)

button = gomez.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[4]/div[2]/table/tbody/tr/td/table[4]/tbody/tr/td/input[2]")

button.click()

result = gomez.find_element(By.TAG_NAME, "b")

print(result.text)
