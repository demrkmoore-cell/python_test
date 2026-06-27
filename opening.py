from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--headless=new")  # <--- CRITICAL FOR LINUX VIRTUAL MACHINES
chrome_options.add_argument("--remote-debugging-port=9222")

driver = webdriver.Chrome(options=chrome_options)

driver.get('https://google.com/')

current_url = driver.current_url
assert 'google.com' in current_url

print("SUCCESS! The page loaded and passed the assertion.")
driver.quit()