To do list:
1- Place web driver inside Python37-32\Scripts folder
2- Main project folder "go-jek-amazon-test"
3- Page elements (using POM) to be kept inside lib.ui.amazon_home_page (This will be used only to capture page elements)
4- Driver related methods and any other generic methods to be kept inside lib.util.create_driver
5- Test automation TCs will be inside test-scripts/test_login_logout
6- From root directory "go-jek-amazon-test", open command prompt and use command >> python -m pytest -v --capture=no --html=report.html test-scripts/test_login_logout.py
7- Above will run the test script using pytest module and generates a report with TC in go-jek-amazon-test/report.html

Packages to be installed:
1- selenium 3.141.0
2- pytest 3.7.1
3- time  
4- Unittest


Note:
I couldnt create new Amazon user id as it required new mobile number. And I have already registered with mine.
Please fill user-email and user-password in test_login_logout.py script