from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Replace with the path to your Edge driver
service = Service(r'D:\edge_webdriver\edgedriver.exe')
driver = webdriver.Edge(service=service)
# Start the browser and open a new tab
driver.get("https://www.baidu.com")

# Wait for user to click the start button
start_button = WebDriverWait(driver, 600).until(
    EC.presence_of_element_located((By.ID, "start"))
)
start_button.click()

# Start recording
history = []
while True:
    try:
        # Wait for user to click the stop button
        stop_button = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.ID, "stop"))
        )
        stop_button.click()
        break
    except:
        # Record the current URL and timestamp
        url = driver.current_url
        timestamp = time.time()
        history.append((timestamp, url))
        time.sleep(1)

# Save history to file
with open("history.txt", "w") as f:
    for timestamp, url in history:
        f.write(f"{timestamp}\t{url}\n")

# Close the browser
driver.quit()
