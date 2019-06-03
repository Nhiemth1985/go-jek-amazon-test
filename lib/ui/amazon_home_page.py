from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time


class AmazonHomePage:

    def __init__(self, driver):
        self.driver = driver

    def click_sign_in(self):
        try:
            return self.driver.find_element_by_id("nav-link-yourAccount").click()
        except:
            return None

    def wait_for_login_page(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(expected_conditions.visibility_of(self.find_element_by_id('authportal-main-section')))

    def enter_email(self, email):
        try:
            self.driver.find_element_by_id("ap_email").send_keys(email)
            return self.driver.find_element_by_id("continue").click()
        except:
            return None

    def enter_password(self, password):
        try:
            return self.driver.find_element_by_id("ap_password").send_keys(password)
        except:
            return None

    def click_login(self):
        try:
            self.driver.find_element_by_name("rememberMe").click()
            return self.driver.find_element_by_id("signInSubmit").click()
        except:
            return None

    def wait_for_shop_by_category(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(expected_conditions.visibility_of(self.driver.find_element_by_id("nav-link-shopall")))

    def hover_over_category(self):
        element_to_hover_over = self.driver.find_element_by_id("nav-link-shopall")
        hover = ActionChains(self.driver).move_to_element(element_to_hover_over)
        hover.perform()

    def hover_over_category(self):
        element_to_hover_over = self.driver.find_element_by_id("nav-link-shopall")
        hover = ActionChains(self.driver).move_to_element(element_to_hover_over)
        hover.perform()

    def hover_over_tv_appliance_electronics(self):
        # // span[contains(text(), 'TV, Appliances, Electronics')]
        element_to_hover_over = self.driver.find_element_by_xpath(
            "// span[contains(text(), 'TV, Appliances, Electronics')]")
        hover = ActionChains(self.driver).move_to_element(element_to_hover_over)
        hover.perform()

    def click_headphones(self):
        try:
            return self.driver.find_element_by_xpath("//span[contains(text(),'Headphones')]").click()
        except:
            return None

    def select_headphone(self, n=1):
        try:
            return self.driver.find_element_by_xpath(
                "(//div[@id='widgetContent']//button[@class='a-button-text a-text-center'][contains(text(),'Add to Cart')])[{}]".format(
                    n)).click()
        except:
            return None

    def go_to_amazon_home(self):
        try:
            return self.driver.find_element_by_xpath("//div[@id='nav-logo']//a[@aria-label='Amazon']").click()
        except:
            return None

    def search_item(self, item="Macbook pro"):
        try:
            return self.driver.find_element_by_id("twotabsearchtextbox").send_keys(item, Keys.ARROW_DOWN, Keys.ARROW_DOWN, Keys.ENTER)
        except:
            return None
