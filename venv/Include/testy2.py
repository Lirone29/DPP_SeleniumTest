import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'C:\Windows\chromedriver.exe')

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source
        link = driver.find_element_by_link_text("PSF PyCon Trademark Usage Policy")
        link.click()
        assert "\"PyCon\" Trademark Policy" in driver.page_source


    def test_fail_to_add_user(self):
        driver = self.driver
        driver.get("http://thedemosite.co.uk/addauser.php")
        self.assertIn("Add a user - FREE PHP code and SQL", driver.title)
        usernameField = driver.find_element_by_name("username")
        passwordField = driver.find_element_by_name("password")
        assert "username:" in driver.page_source
        assert "password:" in driver.page_source
        usernameField.send_keys("DPP")
        passwordField.send_keys("DPP")
        driver.find_element_by_name("FormsButton2").click()
        assert "User was not added correctly, noe enought letters!!" in driver.page_source

    def test_add_user(self):
        driver = self.driver
        driver.get("http://thedemosite.co.uk/addauser.php")
        self.assertIn("Add a user - FREE PHP code and SQL", driver.title)
        usernameField = driver.find_element_by_name("username")
        passwordField = driver.find_element_by_name("password")
        assert "username:" in driver.page_source
        assert "password:" in driver.page_source
        usernameField.send_keys("DPPtest2")
        passwordField.send_keys("DPPtest2")
        driver.find_element_by_name("FormsButton2").click()
        assert "User was added correctly" in driver.page_source

    def test_sign_in(self):
        driver = self.driver
        driver.get("http://thedemosite.co.uk/login.php")
        self.assertIn("Login", driver.title)
        usernameField = driver.find_element_by_name("username")
        passwordField = driver.find_element_by_name("password")
        assert "Username:" in driver.page_source
        assert "Password:" in driver.page_source
        usernameField.send_keys("DPPtest2")
        passwordField.send_keys("DPPtest2")
        driver.find_element_by_name("FormsButton2").click()
        assert "The username and/or password you specified are correct." in driver.page_source

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
