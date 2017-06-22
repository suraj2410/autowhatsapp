from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


# Logging into Whatsapp web
def login():
    driver.get("https://web.whatsapp.com/")
    print("Waiting for Login using Web whatsapp barcode scan...")
    time.sleep(10)


# Method that does the actual work of finding and sending messages
def findanddeliver():
    # Finding Element based on the name of the contact
    name_element = driver.find_element_by_xpath('//span[contains(text(),"Wiki")]')
    name_element.click()

    # Going into an unlimited loop to send message after sleeping for mentioned number of seconds
    while True:
        # Finding the input field and populating it with message and sending return keys
        input_field = driver.find_element_by_xpath("//div[@contenteditable='true']")
        input_field.send_keys(msg)
        input_field.send_keys(Keys.RETURN)
        time.sleep(int(aftertime))

if __name__ == "__main__":
    # Message to send
    msg = "test"
    # Number of seconds to wait before sending another message
    aftertime = 60

    try:
        driver = webdriver.Firefox()
        driver.implicitly_wait(30)
        driver.maximize_window()
    except Exception as exp:
        print("Error occurred opening Firefox...")
        print("The exact cause for this is " + str(exp))

    login()
    findanddeliver()
