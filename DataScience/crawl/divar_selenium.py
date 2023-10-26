from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))

driver.get("https://divar.ir")

# print(driver.title)

city_search_box = driver.find_element(
    By.XPATH, "//div[@class='kt-textfield kt-textfield--has-start-icon']/input")
city_search_box.send_keys("تهران")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.CLASS_NAME, "kt-search-result-row"))).click()
kala_search_box = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, "input[placeholder='جستجو در همهٔ آگهی‌ها']")))
kala_search_box.send_keys("برنامه نویسی")
kala_search_box.send_keys(Keys.ENTER)
time.sleep(2)

card_list = driver.find_element(
    By.ID, "post-list-container-id").find_elements(By.XPATH, "//div[contains(@class, 'post-card-item')]")

for item in card_list:
    try:
        print(item.find_element(
            By.CSS_SELECTOR, "h2.kt-post-card__title").text)
    except:
        pass
driver.quit()
