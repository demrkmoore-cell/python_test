import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)

try:
    # 1. Open the lesson URL (Make sure your live server link is pasted here!)
    driver.get("https://cnt-5252b3ab-c80a-458e-a92c-b0bdad46fc79.containerhub.tripleten-services.com/"
               "")

    # 2. Locate using their exact hinted XPath and click in a single statement:
    driver.find_element(By.XPATH, "//button[@class='close-button input-close-button']").click()

    # Pause 2 seconds to watch the red "Enter the address" error appear
    time.sleep(2)

finally:
    driver.quit()