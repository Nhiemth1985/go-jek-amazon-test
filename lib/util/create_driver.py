from selenium.webdriver import Chrome


def get_driver_instance():
    driver = Chrome(executable_path="chromedriver.exe")
    driver.maximize_window()
    driver.get("https://www.amazon.in/")
    driver.implicitly_wait(30)
    return driver
