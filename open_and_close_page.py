from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 1. Configure Linux environment stability options
options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--headless=new")  # Essential for containerized/VM grading environments

# 2. Initialize the Chrome driver
driver = webdriver.Chrome(options=options)

# 3. Open the Urban Routes homepage
# IMPORTANT: Replace this placeholder string with your live server link from the platform!
urban_routes_url = "https://cnt-281127a8-89e9-439e-a7ec-2262b73fdf61.containerhub.tripleten-services.com/"
driver.get(urban_routes_url)

# 4. Verify that the URL contains 'tripleten-services.com'
current_url = driver.current_url
assert "tripleten-services.com" in current_url

# 5. Close the browser
driver.quit()