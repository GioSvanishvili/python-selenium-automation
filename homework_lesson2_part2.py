from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get('https://www.target.com/')

driver.find_element(By.XPATH, "//span[text()='Sign in']").click()
sleep(5)
driver.find_element(By.XPATH, "//a[@href='/account']//span[text()='Sign in']").click()
sleep(5)
driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']")

driver.find_element(By.ID, 'login')
