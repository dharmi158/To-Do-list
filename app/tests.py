from django.test import TestCase

# Create your tests here.


from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
import time

class TestProjectListPage(StaticLiveServerTestCase):

    def setUp(self):
        self.browser=webdriver.Chrome('chromedriver.exe')

    def tearDown(self): 
        self.browser.close()


    def login_test(self):
        self.browser.get('http://127.0.0.1:8000/signup/')
        self.browser.maximize_window() 

        self.browser.find_element_by_name("username").send_keys("dhruv6")
        time.sleep(1)
        self.browser.find_element_by_name("password1").send_keys("dhr@12341")
        time.sleep(1)
        self.browser.find_element_by_name("password2").send_keys("dhr@12341")
        time.sleep(1)
        self.browser.find_element_by_class_name("btn").click()
        time.sleep(5)


        self.browser.find_element_by_name("username").send_keys("dhruv6")
        time.sleep(1)
        self.browser.find_element_by_name("password").send_keys("dhr@12341")
        time.sleep(1)
        self.browser.find_element_by_class_name("btn").click()
        time.sleep(5)

        self.browser.find_element_by_name("title").send_keys("xyz")
        time.sleep(1)
        self.browser.find_element_by_name("status").send_keys("COMPLETED")
        time.sleep(1)
        self.browser.find_element_by_name("priority").send_keys("6️⃣")
        time.sleep(5)
        self.browser.find_element_by_class_name("btn").click()
        time.sleep(5)
