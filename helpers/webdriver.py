from selenium import webdriver
import platform, os
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def driver(self, browser):
    if browser=="chrome" or browser=="Chrome" or browser=="CHROME":
        options = webdriver.ChromeOptions()
        # options.add_argument('--disable-extensions')
        # options.add_argument("--no-sandbox")
        # options.add_argument("--disable-gpu")
        # options.add_argument("--screen-size=1200x800")
        # options.add_argument('--headless')
        # options.add_argument("--remote-debugin-port=9222")
        if "Darwin" in platform.system():
            self.driver = webdriver.Chrome('../drivers/chrome75/chromedriver', chrome_options=options)
        elif "Windows" in platform.system():
            self.driver = webdriver.Chrome('../drivers/chrome75/chromedriver.exe', chrome_options=options)
        elif "Linux" in platform.system():
            self.driver = webdriver.Chrome('../drivers/chrome75/chromedriverlinux', chrome_options=options)
    if browser == "firefox" or browser == "FIREFOX" or browser == "Firefox":
        cap = DesiredCapabilities.FIREFOX
        cap['marionette'] = True
        options = webdriver.FirefoxOptions()
        # options.add_argument('--disable-extensions')
        # options.add_argument("--no-sandbox")
        # options.add_argument("--disable-gpu")
        # options.add_argument("--screen-size=1200x800")
        options.add_argument('--headless')
        # options.add_argument("--remote-debugin-port=9222")
        if "Darwin" in platform.system():
            self.driver = webdriver.Firefox(executable_path='../drivers/firefox67/geckodriver', firefox_options=options, capabilities=cap)
        elif "Windows" in platform.system():
            self.driver = webdriver.Firefox(executable_path='../drivers/firefox67/geckodriver.exe', firefox_options=options, capabilities=cap)
        elif "Linux" in platform.system():
            self.driver =webdriver.Firefox(executable_path='../drivers/firefox67/geckodriver_linux32', firefox_options=options, capabilities=cap)
    self.driver.implicitly_wait(3)

def closeDriver(self):
    self.driver.stop_client()
    self.driver.close()
    if "Darwin" in platform.system():
        if "firefox" in self.driver.name:
            os.system("pkill 'firefox'")
        if "chrome" in self.driver.name:
            os.system("pkill 'Chrome'")