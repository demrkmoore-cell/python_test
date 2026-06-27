import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_custom_scooter():
    driver = webdriver.Chrome()

    try:
        # Go to the URL
        driver.get(
            ''
        )

        # Enter From
        driver.find_element(By.ID, 'from').send_keys('East 2nd Street, 601')

        # Enter To
        driver.find_element(By.ID, 'to').send_keys('1300 1st St')

        # Click Custom
        driver.find_element(By.XPATH, '//div[text()="Custom"]').click()
        time.sleep(2)

        # Click Scooter Icon (Safely ignoring dynamic build hashes!)
        driver.find_element(By.XPATH, '//img[contains(@src, "scooter")]').click()
        time.sleep(2)

        # Verify Scooter Text exists
        actual_value = driver.find_element(
            By.XPATH, '//div[@class="results-text"]//div[@class="text"]'
        ).text
        expected_value = "Scooter"

        assert (
            expected_value in actual_value
        ), f"Expected '{expected_value}', but got '{actual_value}'"

        time.sleep(2)

    finally:
        # This will now close Chrome whether the test passes OR fails.
        driver.quit()