# librarii gratuite care ne trebuie sa exersam selenium si acces la chrome

# intitializam chrome - un tab gol de chrome sau ce alt browser vrem
#  #salvam in variabila chrome
# from time import sleep
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver.chrome import webdriver
# from selenium.webdriver.common.by import 
# 
# chrome = webdriver.Chrome(service=Service(webdriver().install()))
# sleep(5)


from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

#initializam chrome - un tab gol de chrome sau ce alt browser vrem
#salvam in variabila chrome tabul gol de chrome

chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
sleep(5)

#marit fereastra
chrome.maximize_window()
chrome.get("Https://the-internet.herokuapp.com/login")
username_input = chrome.find_element(By.ID,"username")
username_input.send_keys("tom")
chrome.find_element(By.ID,"password").send_keys("SuperSecretPassword!")
chrome.find_element(By.CSS_SELECTOR, "#password").send_keys("SuperSecretPassword!")
sleep(10)
#ne inchide fereastra
chrome.quit()
