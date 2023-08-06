import requests
import os
from selenium import webdriver

# Set the URL of the website that displays the results
url = "http://result.bisefsd.edu.pk/ResultDetails.aspx?RollNo="

# Create a folder to store the screenshots
folder_name = "screenshots"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)

# Get a list of all students' roll numbers
# roll_numbers = [123456, 789101, 234567, 890123]

# Download the screenshots for each student
for roll_number in range(596167, 596215):
    url_with_roll_number = url + str(roll_number)
    driver = webdriver.Chrome()
    driver.get(url_with_roll_number)
    screenshot_name = f"{folder_name}/{roll_number}.png"
    driver.save_screenshot(screenshot_name)
    driver.close()

print("All screenshots have been taken.")
