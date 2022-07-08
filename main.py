import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver = webdriver.Chrome(executable_path="C:/Users/arunp/PycharmProjects/pythonSelenium/browserDriver/chromedriver.exe")

driver.get("https://www.octaxcol.com/taxes/about-property-tax/property-tax-search-tax-roll-download/")
driver.maximize_window()

# # searchcontent = driver.find_element(by=By.ID,value="mainContent_txtParcel")
#
# searchcontent=driver.find_element_by_xpath("//input[@id='mainContent_txtParcel']").send_keys("052128669001540")
#
#
# time.sleep(5)
# driver.quit()