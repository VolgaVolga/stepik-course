# -- coding: utf-8 --
from selenium import webdriver
import time
import math
from selenium.webdriver.support import expected_conditions

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
    
try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #wait = WebDriverWait(driver, 12)
    inpPrice = wait.until(expected_conditions.text_to_be_present_in_element((By.Id, 'price'), '$100'))

    button = browser.find_element_by_css_selector("button.btn.btn-primary")
    button.click()    

    time.sleep(2)
    
    alert = browser.switch_to.alert
    alert.accept()
    

  
finally:

    # ��������� ������� ����� ���� �����������
    browser.quit()