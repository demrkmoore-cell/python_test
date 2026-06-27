from selenium import webdriver
import time

# 1. Initialize the Chrome driver
driver = webdriver.Chrome()

# 2. Navigate to a test webpage
driver.get("https://www.google.com")

# 3. Pause for 5 seconds so you can see it working
time.sleep(5)

# 4. Close the browser cleanly
driver.quit()