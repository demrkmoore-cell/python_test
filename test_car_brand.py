import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from urban_routes_main_page import UrbanRoutesPage


def test_drive_custom_camping_option():
    # Chrome Container Setup
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=chrome_options)

    # Grab a fresh URL from your bootcamp tab if this one expired!
    driver.get('https://cnt-de257e2a-a78d-46b7-b94e-97bef00e0045.containerhub.tripleten-services.com/')

    routes_page = UrbanRoutesPage(driver)

    routes_page.set_from('East 2nd Street, 601')
    routes_page.set_to('1300 1st St')

    time.sleep(2)
    routes_page.click_custom_button()
    routes_page.click_drive_button()

    time.sleep(1)
    routes_page.click_book_button()

    time.sleep(1)
    routes_page.select_camping_tariff()

    assert routes_page.get_car_make() == "Audi A3 Sedan"

    driver.quit()