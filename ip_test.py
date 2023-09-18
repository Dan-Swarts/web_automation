from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Configuration for the process using tun5
chrome_options_tun5 = Options()
chrome_options_tun5.add_argument('--proxy-server="http://10.23.0.6:8081')


# Start the WebDriver with tun5
driver_tun5 = webdriver.Chrome(options=chrome_options_tun5)

# Now you have a Selenium WebDriver instance using the tun5 network interface.
# You can use 'driver_tun5' to control the browser connected to tun5.

# Example usage:
driver_tun5.get('https://whatismyipaddress.com/')  # This will open the URL using tun5 interface

input()

# Don't forget to close the WebDriver instance when you are done.
driver_tun5.quit()