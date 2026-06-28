from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# 1. Initialize driver (Keeping your Linux survival flags just in case!)
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

try:
    # 2. Open the page (Paste your active server link here)
    driver.get(
        "https://cnt-40315997-e928-4d4f-a8c5-d3c7c2588c80.containerhub.tripleten-services.com/"
    )

    # Step 1: Fill in "From" and "To"
    driver.find_element(By.ID, "from").send_keys("East 2nd Street, 601")
    driver.find_element(By.ID, "to").send_keys("1300 1st St")

    # Step 2: Click "Call a taxi" button
    driver.find_element(By.XPATH, "//button[@class='button round']").click()

    # Step 3: Explicit Wait of 3 seconds for the comment box to become visible
    comment_field = WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.ID, "comment"))
    )

    # Step 4: Write a comment
    my_comment = "Please don't play the radio too loud, thanks!"
    comment_field.send_keys(my_comment)

    # Step 5: Assert and verify the typed text using get_attribute("value")
    actual_comment = comment_field.get_attribute("value")

    assert actual_comment == my_comment, (
        f"Verification failed! Expected '{my_comment}', but got '{actual_comment}'"
    )

    print("Success! Driver comment was entered and verified.")

finally:
    driver.quit()