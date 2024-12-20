from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

email = "lamijok887@mowline.com" #change your email here
username = "dummymr136760" #chage your username here
password = "mrdummy123" #change your password here

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://x.com/i/flow/login')


time.sleep(3)


print(driver.page_source)
6
#  Input email (increased timeout)
loginField = WebDriverWait(driver, 20).until(  # increased timeout to 20 seconds
    EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input'))
)
loginField.send_keys(email)

# Click Next button after entering email
nextButton1 = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]'))
)
nextButton1.click()

# Input username
usernameField = WebDriverWait(driver, 20).until(  
    EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input'))
)
usernameField.send_keys(username)

# Click Next button after entering username
nextbutton2 = WebDriverWait(driver, 20).until(  
    EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/button'))
)
nextbutton2.click()

# Login step 3: Input password
passwordField = WebDriverWait(driver, 20).until(  
    EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input'))
)
passwordField.send_keys(password)

# Click login button after entering password
loginbutton = WebDriverWait(driver, 20).until(  
    EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button'))
)
loginbutton.click()


tweet = "Hello world"

# Wait for tweet input field to be ready
tweetInputField = WebDriverWait(driver, 20).until(  
    EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div'))
)
tweetInputField.send_keys(tweet)

# Click tweet button
tweetButton = WebDriverWait(driver, 20).until(  
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button'))
)
tweetButton.click()


time.sleep(1)

# Close the browser
driver.quit()
