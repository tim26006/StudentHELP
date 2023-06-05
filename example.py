from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def parseLK(username:str,password:str,course:int)->dict:
    return_dict = {}
    driver = webdriver.Chrome("C:/Users/ulibk/PycharmProjects/Neural/chromedriver.exe")
    driver.get("https://student.knastu.ru/")
    driver.find_element_by_css_selector("input[type=text]").send_keys(username)
    driver.find_element_by_css_selector("input[type=password]").send_keys(password)
    driver.find_element_by_css_selector("button[type=submit]").click()
    time.sleep(5)
    if course==1:
        driver.find_elements_by_xpath(".//button[@class='select_course__btn btn btn-primary']")[0].click()
    if course==2:
        driver.find_elements_by_xpath(".//button[@class='select_course__btn btn btn-outline-primary']")[0].click()
    if course == 3:
        driver.find_elements_by_xpath(".//button[@class='select_course__btn btn btn-outline-primary']")[1].click()
    if course == 4:
        driver.find_elements_by_xpath(".//button[@class='select_course__btn btn btn-outline-primary']")[2].click()

    time.sleep(5)

    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    all_subjects = soup.findAll('div', class_='row gx-0')
    text2marks = {
    "отлично":5,
    "хорошо": 4,
    "удовлевтворительно:":3,
    "зачтено":5,
    "не зачтено":2,
    "-":"-"
}

    for x, subject in enumerate(all_subjects,start=1):
        try:
            sub = subject.find("a",class_="rpd_link_in_yp").text
            mark = subject.find("div", class_="col-6 col-md-3 col-lg px-1 d-flex align-items-center").find("span",class_="ps-2").text.strip()
            return_dict[f'{sub}({x})'] = text2marks[mark]
        except:continue

    return return_dict