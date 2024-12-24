# WhatsApp Web Automation Bot

This project is a **WhatsApp Web Automation Bot** that utilizes **Selenium** to automate interactions with WhatsApp Web. Below is a guide to understanding how the project works, including the necessary imports, environment setup, and commands to run the project.

## 1. **Required Libraries and Imports**

Before running the script, you'll need to install the necessary Python libraries. Below is a list of all the imports used in the project and a brief explanation of each:

```python
# WebDriver Manager: Manages the ChromeDriver for Selenium automatically.
from webdriver_manager.chrome import ChromeDriverManager

# Selenium WebDriver: The main tool for controlling the browser.
from selenium import webdriver

# Chrome Service: Allows for configuration and execution of the Chrome WebDriver.
from selenium.webdriver.chrome.service import Service

# Chrome Options: Allows customization of browser settings.
from selenium.webdriver.chrome.options import Options

# Locators: Used to find elements in the web page (e.g., By.CLASS_NAME, By.XPATH).
from selenium.webdriver.common.by import By

# Keys: To simulate keyboard inputs.
from selenium.webdriver.common.keys import Keys

# Desired Capabilities: Used for setting up specific browser configurations.
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# Time: Used for adding delays (e.g., time.sleep()) to simulate waiting.
import time

# OS: For interacting with the operating system, such as getting the current directory.
import os
