import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from urban_routes_main_page import UrbanRoutesPage


def test_camping():
    chrome_options = Options()
    # Tell Selenium: "The browser lives here, go find the driver for it yourself"
    chrome_options.binary_location = "/usr/bin/chromium"
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")

    # Let Selenium Manager auto-connect the driver
    driver = webdriver.Chrome(options=chrome_options)

    # Refresh this URL from your bootcamp window if your container timed out!
    driver.get('https://cnt-699c0f3b-01cc-4b93-87fc-367d723571fe.containerhub.tripleten-services.com/')

    routes_page = UrbanRoutesPage(driver)

    routes_page.choose_camping_car('East 2nd Street, 601', '1300 1st St')
    time.sleep(1)

    routes_page.adding_driver_license('DeMarko', 'Moore', '01.01.1995', '1234567890')
    time.sleep(1)

    assert routes_page.get_car_make() == "Audi A3 Sedan"

    driver.quit()