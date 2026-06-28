from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_fastest_mode_text():
    # 1. Create ChromeOptions object
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--headless=new")
    options.page_load_strategy = 'eager'
    options.add_argument("--window-size=1920,1080")

    # 2. Use the Service object to handle the driver automatically
    # This replaces the line: driver = webdriver.Chrome(options=options)
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    try:
        # Update with your active container URL
        driver.get("https://cnt-cdd03aca-f66f-4ac8-8ac9-cc607211ce7b.containerhub.tripleten-services.com/")

        time.sleep(2)

        driver.find_element(By.ID, "from").send_keys("East 2nd Street, 601")
        driver.find_element(By.ID, "to").send_keys("1300 1st St")

        time.sleep(2)

        mode = (
            driver.find_element(By.XPATH, "//div[@class='mode active']")
            .get_attribute("textContent")
            .strip()
        )

        time.sleep(2)

        assert mode == "Fastest"

    finally:
        driver.quit()