# UnitTest is a built-in Python module that can be used for any app. Automated testing is standard in development because it lets you check your software's functionality without having to manually test so many functions
# Writing code in a procedural manner for a large website is really difficult to do (have to scroll through and look for different things)
# Separates each previously defined component into its own class - once you have that setup, it becomes much easier to test another page within it
# UnitTest built into Python
import unittest
import page
# Importing webdriver API to control the browser
from selenium import webdriver
# Service object handles browser driver, used to pass ChromeDriverManager config as chrome webdriver is initialized
from selenium.webdriver.chrome.service import Service
# Options instance defines what the browser must support and how it should behave
from selenium.webdriver.chrome.options import Options
# ChromeDriverManager automatically fetches the most recent version of chrome webdriver and installs it
from webdriver_manager.chrome import ChromeDriverManager

# App purpose: Testing Python website and seeing if its search function works

# Creating a class which represents the main test case that you want to perform on the website. You can have multiple classes (so multiple test cases)!
# unittest.TestCase is the class that PythonOrgSearch inherits from
# Whenever you'd like to make a new thing to test (such as different page, new functionality, etc.) - create a new case but inside this case you can still test multiple aspects of the webpage
# Inheriting unittest.TestCase also gives you access to methods that help you define test cases and set them up
# When you press a button, all the defined tests will be ran and it'll give you some nice output on the test status (pass, etc.)
class PythonOrgSearch(unittest.TestCase):
    # First method written inside test case
    # Almost like an init method, specific to test case. Any variables you need to define / things you need to setup before the test case gets started
    def setUp(self):
        # Configure and initializes the instance of chrome webdriver, options and service behavior defined above
        chrome_options = Options()
        # Session start
        self.driver = webdriver.Chrome(options = chrome_options, service=Service(ChromeDriverManager().install()))
        self.driver.get("http://www.python.org")
    
    # Inheritance of unittest.TestCase makes it so methods with the lowercase keyword test at the start of them are automatically ran
    def test_example(self):
        print("Test")
        assert True
        # Assert basically says "see if the condition on the right side is true", will tell you if the test case passed or failed
        # Test case methods need to end with assert or have assert inside them to tell whether the test case passed or failed
        # If true assert pass, if false assert failed

    # Due to this method not starting with the keyword test, it won't be automatically ran
    def not_a_test(self):
        print("This won't work")

    # Ran after test case is finished, clean up
    def tearDown(self):
        self.driver.close()