from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize driver
driver = webdriver.Chrome()
driver.implicitly_wait(5)

try:
    # 1. Open the lesson URL (Paste your active bootcamp server URL here)
    driver.get("https://cnt-35e21127-c9d6-42fe-9d60-4a111b1bcb5d.containerhub.tripleten-services.com/")

    # 2. Locate the "From" and "To" input fields
    # (In Urban Routes, these standardly use the 'id' attributes "from" and "to")
    from_field = driver.find_element(By.ID, "from")
    to_field = driver.find_element(By.ID, "to")

    # 3. Extract the placeholder text from the HTML tags
    actual_from_placeholder = from_field.get_attribute("placeholder")
    actual_to_placeholder = to_field.get_attribute("placeholder")

    # 4. Assert both fields match the exact assignment instructions
    assert actual_from_placeholder == "East 2nd Street, 601", (
        f"From field failed! Expected 'East 2nd Street, 601', got '{actual_from_placeholder}'"
    )

    assert actual_to_placeholder == "1300 1st St", (
        f"To field failed! Expected '1300 1st St', got '{actual_to_placeholder}'"
    )

    print("Success! Both input placeholders passed verification.")

finally:
    # 5. Safely close the browser
    driver.quit()