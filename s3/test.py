from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def test_flask_app_text():
    # Set up headless Chrome options (optional)
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # run without UI

    # Initialize WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    
    try:
        # Go to the Flask app running locally
        driver.get("http://127.0.0.1:5000/")

        # Grab the page text (since your app just returns plain text)
        body_text = driver.find_element(By.TAG_NAME, "body").text
        
        assert body_text == "Hello, Docker!", f"Expected text not found, got: {body_text}"
        print("Test Passed: Flask app text is correct.")
    
    finally:
        driver.quit()

if __name__ == "__main__":
    test_flask_app_text()
