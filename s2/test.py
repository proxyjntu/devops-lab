from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# 💡 Set path to your local HTML file
html_file_path = r"C:\Student\devops lab\s2\index.html"

# ✅ Convert to file:// URL
file_url = 'file:///' + html_file_path.replace('\\', '/').replace(' ', '%20')

# Start Chrome browser
driver = webdriver.Chrome()  # assumes chromedriver is in PATH

try:
    # Open local HTML file
    driver.get(file_url)

    # Wait for the counter and button elements to load
    wait = WebDriverWait(driver, 5)
    counter = wait.until(EC.presence_of_element_located((By.ID, "counter")))
    button = wait.until(EC.presence_of_element_located((By.ID, "increment-btn")))

    # Get initial value
    initial_value = counter.text
    print("Initial counter value:", initial_value)

    # Click the increment button
    button.click()

    # Wait for the counter to become "1"
    wait.until(EC.text_to_be_present_in_element((By.ID, "counter"), "1"))
    new_value = counter.text
    print("Counter value after click:", new_value)

    # Test result
    if new_value == '1':
        print("✅ Test passed!")
    else:
        print("❌ Test failed.")
finally:
    time.sleep(2)  # optional, just to see the result before browser closes
    driver.quit()
