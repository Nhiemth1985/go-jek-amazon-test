1- Place web driver inside Python37-32\Scripts folder
2- Main project folder "go-jek"
3- Page elements (using POM) to be kept inside lib.ui.amazon_home_page (This will be used only to capture page elements)
4- Driver related methods and any other generic methods to be kept inside lib.util.create_driver
5- Test automation TCs will be inside test-scripts/test_login_logout
6- From root directory "go-jek", open command prompt and use command >> python -m pytest -v --capture=no --html=report.html test-scripts/test_login_logout.py
7- Above will run the test script using pytest module and generates a report with TC in go-jek/report.html

Packages to be installed:
1- selenium 3.141.0
2- pytest 3.7.1
3- time  
4- Unittest
