import unittest
from lib.ui.amazon_home_page import *
from lib.util.create_driver import *
import time
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
        self.amazon.enter_email(email="<ENTER EMAIL ID>")

        # Enter valid password and login
        self.amazon.enter_password(password="<ENTER PASSWORD>")
        self.amazon.click_login()

        # Select Departments section > Electronics > Headphones
        self.amazon.wait_for_shop_by_category()
        self.amazon.hover_over_category()
        self.amazon.hover_over_tv_appliance_electronics()
        self.amazon.click_headphones()

        # Select first available headphone and add to cart.
        # By default it is first headphone.
        # To change, mention parameter n = XXX for specifying which headphone is required
        self.amazon.select_headphone()
        time.sleep(5)
        self.amazon.go_to_amazon_home()

        # Search for Macbook pro from Search bar and select 2nd available product
        # Add the product to cart with quantity as 2
        # To change the search item, mention item = XXX. By default it is "Macbook pro"
        self.amazon.search_item_macbook()
        self.amazon.select_macbook()
        self.amazon.select_item_quantity()
        self.amazon.add_to_cart()

        # Select cart from home and remove earlier added headphones
        # Reduce the quantity of "Macbook pro"
        # Proceed to checkout
        self.amazon.go_to_amazon_home()
        self.amazon.go_to_cart()
        self.amazon.delete_headphones_from_cart()
        self.amazon.reduce_macbook_quantity()
        self.amazon.proceed_to_checkout()

        # Go back to previous page and logout
        self.driver.back()
        self.amazon.logout_from_amazon()
