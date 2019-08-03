from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from helpers import utility
from pageobjects import strings
import logging as log, re

def add_cookie(self):
    driver = self.driver
    driver.add_cookie({
        'name': '',
        'value': ''
    })
    driver.refresh()

def wait_until_element_clicable(self, element):
    driver = self.driver
    wait = WebDriverWait(driver, 5)
    wait.until(EC.presence_of_element_located((By.XPATH, element)))

def wait_until_element_visible(self, element, time):
    driver = self.driver
    wait = WebDriverWait(driver, time)
    wait.until(EC.presence_of_element_located((By.XPATH, element)))

def page_has_loaded(self):
    log.info("Checking if {} page is loaded.".format(self.driver.current_url))
    page_state = self.driver.execute_script('return document.readyState;')
    return page_state == 'complete'

def click_first_search(self, searchbox, text, index):
    driver = self.driver
    search_box = driver.find_element_by_xpath(searchbox)
    search_box.send_keys(text)
    utility.wait_until_element_clicable(self, "//*[@class='typeahead dropdown-menu']/li[" + index + "]/a")
    driver.find_element_by_xpath("//*[@class='typeahead dropdown-menu']/li[" + index + "]/a").click()

def switch_window(self, index):
    driver = self.driver
    driver.switch_to_window(driver.window_handles[index])

def windowshandler(self):
    browser = self.driver
    windows_before = browser.current_window_handle
    print("Window Handle is : %s" % windows_before)
    WebDriverWait(browser, 10).until(EC.number_of_windows_to_be(2))
    windows_after = browser.window_handles
    new_window = [x for x in windows_after if x != windows_before][0]
    browser.switch_to_window(new_window)
    print("Page Title after Tab Switching is : %s" % browser.title)
    print("Second Window Handle is : %s" % new_window)

def windowswitcher(self):
    driver = self.driver
    default_handle = driver.current_window_handle
    handles = list(driver.window_handles)
    handles.remove(default_handle)
    driver.switch_to_window(handles[0])

def click_if_visible(self, element):
    driver = self.driver
    try:
        driver.find_element_by_id(element).click()
    except NoSuchElementException:
        pass

def click_if_clicable(self, element):
    driver = self.driver
    if driver.find_element_by_xpath(element).is_displayed():
        driver.find_element_by_xpath(element).click()

def verify_coupons(self, nameDrug):
    navigatePrescriptionSet(self, nameDrug)
    verify_coupons_no_nav(self, nameDrug)

def verify_coupons_no_nav(self, nameDrug):
    driver = self.driver
    main_page = driver.current_window_handle
    prices = driver.find_elements_by_xpath(strings.prices)
    coupons = driver.find_elements_by_xpath(strings.coupons)
    stores = driver.find_elements_by_xpath(strings.stores)
    pr = []
    coup = []
    st = []
    regex = re.compile(strings.regex)
    regex_stores = re.compile(strings.regex_stores)
    for el in prices:
        if 'after coupon' in el.text:
            pr.append(re.search(regex, el.text).group())
    for i in range(len(coupons)):
        if 'GET FREE' in coupons[i].text:
            coup.append(coupons[i])
            st.append(re.search(regex_stores, stores[i].text).group())
    for i in range(len(coup)):
        coup[i].click()
        click_if_visible(self, strings.getfreecoupon)
        click_if_visible(self, strings.proceedtodiscountid)
        # time.sleep(2)
        page_has_loaded(self)
        if "chrome" in driver.name:
            switch_window(self, i+1)
        if "firefox" in driver.name:
            windowswitcher(self)
        try:
            price = driver.find_element_by_xpath(strings.coupon_price).text
            company_name = driver.find_element_by_xpath(strings.coupon_store).text
            if price in pr[i]:
                print("<p>\n Verified founded the price: $" + price + " is same as in coupon and in coupon page \n</p>")
                assert True
            else:
                assert False
            if st[i] in company_name:
                print("<p>\n Verified founded the company name: " + st[i] + " is same as in coupon and in coupon page \n</p>")
                assert True
            else:
                print(st[i])
                assert False
        except NoSuchElementException:
            print("\n<p> Price or Company name not included for: "+nameDrug+ "\n</p>")
            pass
        driver.switch_to.window(main_page)


def navigatePrescriptionSet(self, nameDrug):
    driver = self.driver
    driver.get(strings.base_url)
    add_cookie(self)
    utility.wait_until_element_clicable(self, strings.search_box)
    click_first_search(self,strings.search_box,nameDrug,"1")
    utility.wait_until_element_clicable(self, strings.prices)
    assertIfElementDisplyed(self, strings.prices)

def assertIfElementDisplyed(self, element):
    driver = self.driver
    el = driver.find_element_by_xpath(element)
    assert el.is_displayed()

def selectOptionPresSet(self, option, index):
    driver = self.driver
    click_if_visible(self,strings.but_okgotit)
    try:
        utility.wait_until_element_clicable(self, option)
        driver.find_element_by_xpath(option).click()
        utility.wait_until_element_clicable(self, strings.option_elememnts +"["+index+"]")
        driver.find_element_by_xpath(strings.option_elememnts +"["+index+"]").click()
        utility.wait_until_element_clicable(self, strings.prices_coupons_page)
    except NoSuchElementException:
        pass

def ifdiscontinued_found_verify_coupons(self, nameDrug):
    driver = self.driver
    try:
        if 'is no longer available' in driver.find_element_by_xpath(strings.discontinued_drug).text:
            print(driver.find_element_by_xpath(strings.discontinued_drug).text)
            assert True
    except NoSuchElementException:
        verify_coupons_no_nav(self, nameDrug)

def customQuanPresSet(self, text):
    driver = self.driver
    click_if_visible(self,strings.but_okgotit)
    utility.wait_until_element_clicable(self, strings.option_quantity)
    driver.find_element_by_xpath(strings.option_quantity).click()
    utility.wait_until_element_clicable(self, strings.option_quantity_cus)
    driver.find_element_by_xpath(strings.option_quantity_cus).send_keys(text)
    utility.wait_until_element_clicable(self, strings.option_quantity_cus_set)
    driver.find_element_by_xpath(strings.option_quantity_cus_set).click()
    utility.wait_until_element_clicable(self, strings.prices_coupons_page)

def verify_coupon_custom(self, name, option, index):
    utility.navigatePrescriptionSet(self, name)
    utility.selectOptionPresSet(self, option, index)
    utility.ifdiscontinued_found_verify_coupons(self, name)

def verify_coupon_custom_quan(self, name, quan):
    utility.navigatePrescriptionSet(self, name)
    utility.customQuanPresSet(self, quan)
    utility.ifdiscontinued_found_verify_coupons(self, name)