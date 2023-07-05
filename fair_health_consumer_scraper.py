import time 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


# Create a new instance of the web driver
driver = webdriver.Chrome()  # Replace with the appropriate web driver (e.g., Chrome, Firefox, etc.)

# Navigate to the webpage
url = 'https://www.fairhealthconsumer.org/'  # Replace with the URL of the webpage
driver.get(url)

# Find the button element by text using XPath
button = driver.find_element(By.XPATH, "//button[contains(text(), 'Medical and Hospital Costs')]")  # Replace 'Button Text' with the desired text

# Click the button
button.click()

# Get the current URL
url = driver.current_url

# Print or use the URL as needed
print("Current URL:", url)

# Find the input element by ID
input_element = driver.find_element(By.ID, 'radio3')  # Replace 'example-id' with the desired ID
 
# Print the ID of the input element
print("Input element ID:", input_element.get_attribute('id'))

# Create an ActionChains instance
actions = ActionChains(driver)

# Perform the mouseover action on the radio button
actions.move_to_element(input_element).perform()

# Click on the current element
actions.click().perform()

# Get the current URL
url = driver.current_url

# Print or use the URL as needed
print("Current URL:", url)

# Find the input element by ID or any other suitable locator
input_element = driver.find_element(By.ID, 'location')  # Replace 'example-id' with the desired ID

# Enter text into the input element
input_element.send_keys('60053')

# Find the <div> element by class name
div_element = driver.find_element(By.CLASS_NAME, 'step2Btn')

class_name = div_element.get_attribute('class')
print("Class name:", class_name)

# Find the <a> element by class name
# a_element = driver.find_element(By.CLASS_NAME, 'next')

wait = WebDriverWait(driver, 10)
a_element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'next')))

class_name = a_element.get_attribute('class')
print("Class name:", class_name)

a_element.click()

# Wait for 10 seconds
time.sleep(10)

# Get the current URL
url = driver.current_url

# Print or use the URL as needed
print("Current URL:", url)

# Close the browser
# driver.quit()
