from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def extract_tweet_text(tweet_url):
    # Set up Selenium WebDriver
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode (without GUI)
    path = r"C:\Users\JAYDEEP\chromedriver\chromedriver.exe"

    service = Service(path)  # Path to chromedriver executable
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        # Load tweet URL
        driver.get(tweet_url)

        # Wait for tweet text to load (adjust wait time as needed)
        wait = WebDriverWait(driver, 10) 
        nested_tweet_text_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.css-1rynq56.r-bcqeeo.r-qvutc0.r-37j5jr.r-1inkyih.r-16dba41.r-bnwqim.r-135wba7')))

        # Extract the text of the nested tweet element
        nested_tweet_text = nested_tweet_text_element.text
        return nested_tweet_text.strip()
    except Exception as e:
        print("Error:", e)
        return None
    finally:
        driver.quit()

if __name__ == "__main__":
    
    tweet_url = "https://x.com/sagarcasm/status/1765717264152858730?s=20" # Replace with your tweet URL
    tweet_text = extract_tweet_text(tweet_url)
    if tweet_text:
        print("Tweet Text:", tweet_text)
    else:
        print("Failed to extract tweet text.")
