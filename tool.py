from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import pyautogui as gui
import pyperclip
import time

def make_driver():
    chrome_path = "chromedriver.exe"
    driver = webdriver.Chrome(chrome_path)
    return driver

class Student:
    def __init__(self, name, birth, pw):
        self.name = name
        self.birth = birth
        self.pw = pw
    
    def start(self, driver):
        url = 'https://hcs.eduro.go.kr/'
        driver.get(url)
        time.sleep(1)

        try:
            driver.find_element(By.CLASS_NAME, 'reset_account').click()
            time.sleep(1)
            gui.press('enter')
            time.sleep(1)
            driver.find_element(By.ID, 'btnConfirm2').click()
            time.sleep(1)
        except:
            driver.find_element(By.ID, 'btnConfirm2').click()
            time.sleep(1)
    
    def choose_school(self, driver):
        driver.find_element(By.ID, 'schul_name_input').click()
        sidolabel = Select(driver.find_element(By.ID, 'sidolabel'))
        sidolabel.select_by_value(value='17')
        time.sleep(0.5)
        crseScCode = Select(driver.find_element(By.ID, 'crseScCode'))
        crseScCode.select_by_value(value='4')
        time.sleep(0.5)
        schul_name_input = driver.find_element(By.ID, 'orgname')
        schul_name_input.clear()
        schul_name_input.click()
        pyperclip.copy('경남과학고등학교')
        schul_name_input.send_keys(Keys.CONTROL, 'v')
        gui.press('enter')
        gui.press(['tab', 'tab', 'enter', 'tab', 'enter'])
        time.sleep(1)
    
    def input_name(self, driver):
        tag_name = driver.find_element(By.ID, 'user_name_input')
        tag_name.clear()
        tag_name.click()
        pyperclip.copy(self.name)
        tag_name.send_keys(Keys.CONTROL, 'v')

    def input_birthday(self, driver):
        tag_birthday = driver.find_element(By.ID, 'birthday_input')
        tag_birthday.clear()
        tag_birthday.click()
        pyperclip.copy(self.birth)
        tag_birthday.send_keys(Keys.CONTROL, 'v')
    
    def open_pw_keyboard(self, driver):
        driver.find_element(By.ID, 'btnConfirm').click()
        time.sleep(1)
        driver.find_element(By.CLASS_NAME, 'keyboard-icon').click()
        time.sleep(1)
    
    def click_password(self, driver, num):
        pw_buttons = driver.find_elements(By.CLASS_NAME, 'transkey_div_3_2') + driver.find_elements(By.CLASS_NAME, 'transkey_div_3_3')
        for btn in pw_buttons:
            if btn.get_attribute('aria-label') == str(num):
                pw_button = btn
        pw_button.click()
    
    def find_me(self, driver):
        driver.find_element(By.ID, 'btnConfirm').click()
        time.sleep(1)
        people = driver.find_elements(By.CLASS_NAME, 'survey-button')
        me = people[0]
        me.click()
        time.sleep(1)
    
    def do_survey(self, driver):
        driver.find_element(By.ID, 'survey_q1a1').click()
        driver.find_element(By.ID, 'survey_q2a3').click()
        driver.find_element(By.ID, 'survey_q3a1').click()
        driver.find_element(By.ID, 'btnConfirm').click()
        time.sleep(1)

    def hcs(self):
        driver = make_driver()
        self.start(driver)
        self.choose_school(driver)
        self.input_name(driver)
        self.input_birthday(driver)
        self.open_pw_keyboard(driver)
        for num in str(self.pw):
            self.click_password(driver, num)
        self.find_me(driver)
        self.do_survey(driver)

if __name__ == '__main__':
    me = Student('이민재', '040626', '0626')