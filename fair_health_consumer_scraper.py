from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


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

# input_element.click()

# Find the <i> element by class name
# i_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'i.fa.fa-chevron-square-right')))

# Print the class name
# print("Class name:", i_element.get_attribute("class"))



# i_element.click()


""" clickable_elements = driver.find_elements_by_xpath("//a | //button | //input[@type='submit'] | //input[@type='button'] | //input[@type='image'] | //input[@type='checkbox'] | //input[@type='radio'] | //select | //textarea")

# Print the clickable elements
for element in clickable_elements:
    print("Clickable Element:", element)
 """

# Set the radio button to checked
# driver.execute_script("arguments[0].checked = true;", radio_button)

# print(input_element.value)

# Find the img element by class using CSS selector
# image = driver.find_element(By.CSS_SELECTOR, "i.fa.fa-chevron-square-right")  # Replace 'class-name' with the desired class name# Click the span

# Close the browser
# driver.quit()
