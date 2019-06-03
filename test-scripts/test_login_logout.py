import unittest
from lib.ui.amazon_home_page import *
from lib.util.create_driver import *
import time
import selenium
from selenium import webdriver
import pytest


class TestAmazon(unittest.TestCase):

    def setUp(self):
        self.driver = get_driver_instance()
        self.amazon = AmazonHomePage(self.driver)

    def tearDown(self):
        self.driver.close()

    def test_sign_in(self):
        # Sign-in to Amazon site
        self.amazon.click_sign_in()
        time.sleep(5)
        # Enter valid email
        self.amazon.enter_email(email="XXXX")
        # Enter valid password and login
        self.amazon.enter_password(password="XXXX")
        self.amazon.click_login()
        # Select Departments section > Electronics > Headphones
        self.amazon.wait_for_shop_by_category()
        self.amazon.hover_over_category()
        self.amazon.hover_over_tv_appliance_electronics()
        self.amazon.click_headphones()
        # Select first available headphone and add to cart. By default it is first headphone. To change, mention parameter n = XXX for specifying which headphone is required
        self.amazon.select_headphone()
        time.sleep(5)
        self.amazon.go_to_amazon_home()
        # Search for Macbook pro from Search bar and select 2nd available product
        self.amazon.search_item()
        time.sleep(5)
