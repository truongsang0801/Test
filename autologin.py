from selenium import webdriver
from time import sleep
from pynput.keyboard import Key, Controller
import time

user = input('Enter Email Id: ')
pwd = input('Enter Password: ')

driver = webdriver.Chrome(executable_path="C:/java5/chromedriver.exe")
driver.get('http://www.facebook.com')
print("opened facebook")


sleep(3)

username_box = driver.find_element_by_id('email')
username_box.send_keys(user)
print("Email Id entered")


password_box = driver.find_element_by_id('pass')
password_box.send_keys(pwd)
print("Password entered")

login_box = driver.find_element_by_name('login')
login_box.click()



print("Finishes")


keyboard = Controller()

time.sleep(3)

while True:
    keyboard.press('j')
    keyboard.release('j')

    keyboard.press('l')
    keyboard.release('l')

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    time.sleep(5)