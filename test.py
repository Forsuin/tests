#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import time

import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class TestWebsite:
  # 1. Check browser configuration in browser_setup_and_teardown
  # 2. Run 'Selenium Tests' configuration
  # 3. Test report will be created in reports/ directory

  @pytest.fixture(autouse=True)
  def browser_setup_and_teardown(self):

    self.driver = webdriver.Chrome()

    self.driver.maximize_window()
    self.driver.implicitly_wait(10)
    self.driver.get("https://darichards-main-patch-0ecb.dva0ia48yehl5.amplifyapp.com/")
    self.driver.delete_all_cookies()

    yield

    self.driver.close()
    self.driver.quit()


  def test_getUserInfo(self):
    self.driver.implicitly_wait(2)

    self.driver.get("https://darichards-main-patch-0ecb.dva0ia48yehl5.amplifyapp.com/")
    self.driver.set_window_size(974, 1050)
    self.driver.find_element(By.ID, "profile-toggle").click()
    self.driver.find_element(By.ID, "home-user-1").click()
    self.driver.find_element(By.ID, "signInFormUsername").click()
    self.driver.find_element(By.ID, "signInFormUsername").send_keys("ilaidlaw")
    self.driver.find_element(By.ID, "signInFormPassword").send_keys("!Pa55w0rd5")
    self.driver.find_element(By.ID, "signInFormPassword").send_keys(Keys.ENTER)

    time.sleep(0.5)

    self.driver.find_element(By.ID, "profile-toggle").click()
    time.sleep(0.4)
    self.driver.find_element(By.ID, "home-user-1").click()

    time.sleep(1)

    assert self.driver.find_element(By.ID, "name").get_attribute('value') == "Ian Laidlaw"
    assert self.driver.find_element(By.ID, "email").get_attribute("value") == "ilaidlaw@radford.edu"
    assert self.driver.find_element(By.ID, "address").get_attribute("value") == "Somewhere Rd, Moon City"

  def test_modifyUserInfo(self):
    self.driver.implicitly_wait(2)

    self.driver.get("https://darichards-main-patch-0ecb.dva0ia48yehl5.amplifyapp.com/")
    self.driver.set_window_size(974, 1050)
    self.driver.find_element(By.ID, "profile-toggle").click()
    self.driver.find_element(By.ID, "home-user-1").click()
    self.driver.find_element(By.ID, "signInFormUsername").click()
    self.driver.find_element(By.ID, "signInFormUsername").send_keys("ilaidlaw")
    self.driver.find_element(By.ID, "signInFormPassword").send_keys("!Pa55w0rd5")
    self.driver.find_element(By.ID, "signInFormPassword").send_keys(Keys.ENTER)

    time.sleep(0.5)

    self.driver.find_element(By.ID, "profile-toggle").click()
    time.sleep(0.4)
    self.driver.find_element(By.ID, "home-user-1").click()

    time.sleep(1)

    self.driver.find_element(By.ID, "name").clear()
    self.driver.find_element(By.ID, "name").send_keys("New Name")
    self.driver.find_element(By.ID, "email").clear()
    self.driver.find_element(By.ID, "email").send_keys("john@new.mail")
    self.driver.find_element(By.ID, "address").clear()
    self.driver.find_element(By.ID, "address").send_keys("New Home. CT")

    self.driver.find_element(By.XPATH, "//button[@class='btn btn-primary shadow flex-grow-1 text-nowrap']").click()
    self.driver.find_element(By.XPATH, "//button[@onclick='updateUserInfo();']").click()

    time.sleep(3)

    self.driver.refresh()

    result = False

    try:
      assert self.driver.find_element(By.ID, "name").get_attribute('value') == "New Name"
      assert self.driver.find_element(By.ID, "email").get_attribute("value") == "john@new.mail"
      assert self.driver.find_element(By.ID, "address").get_attribute("value") == "New Home. CT"
      result = True
    except:
      result = False
    finally:
      self.driver.find_element(By.ID, "name").clear()
      self.driver.find_element(By.ID, "name").send_keys("Ian Laidlaw")
      self.driver.find_element(By.ID, "email").clear()
      self.driver.find_element(By.ID, "email").send_keys("ilaidlaw@radford.edu")
      self.driver.find_element(By.ID, "address").clear()
      self.driver.find_element(By.ID, "address").send_keys("Somewhere Rd, Moon City")

      self.driver.find_element(By.XPATH, "//button[@class='btn btn-primary shadow flex-grow-1 text-nowrap']").click()
      self.driver.find_element(By.XPATH, "//button[@onclick='updateUserInfo();']").click()

      time.sleep(3)
      return result


  def test_setUserInfoEmpty(self):
    self.driver.implicitly_wait(2)

    self.driver.get("https://darichards-main-patch-0ecb.dva0ia48yehl5.amplifyapp.com/")
    self.driver.set_window_size(974, 1050)
    self.driver.find_element(By.ID, "profile-toggle").click()
    self.driver.find_element(By.ID, "home-user-1").click()
    self.driver.find_element(By.ID, "signInFormUsername").click()
    self.driver.find_element(By.ID, "signInFormUsername").send_keys("ilaidlaw")
    self.driver.find_element(By.ID, "signInFormPassword").send_keys("!Pa55w0rd5")
    self.driver.find_element(By.ID, "signInFormPassword").send_keys(Keys.ENTER)

    time.sleep(0.5)

    self.driver.find_element(By.ID, "profile-toggle").click()
    time.sleep(0.4)
    self.driver.find_element(By.ID, "home-user-1").click()

    time.sleep(1)

    self.driver.find_element(By.ID, "email").clear()
    self.driver.find_element(By.ID, "email").send_keys("")

    self.driver.find_element(By.XPATH, "//button[@class='btn btn-primary shadow flex-grow-1 text-nowrap']").click()
    self.driver.find_element(By.XPATH, "//button[@onclick='updateUserInfo();']").click()

    time.sleep(3)

    self.driver.refresh()

    assert self.driver.find_element(By.ID, "email").get_attribute("value") != ""

    self.driver.find_element(By.ID, "email").clear()
    self.driver.find_element(By.ID, "email").send_keys("ilaidlaw@radford.edu")

    self.driver.find_element(By.XPATH, "//button[@class='btn btn-primary shadow flex-grow-1 text-nowrap']").click()
    self.driver.find_element(By.XPATH, "//button[@onclick='updateUserInfo();']").click()

    time.sleep(3)

  def test_getAdminUsersInfo(self):
    # self.driver.delete_all_cookies()

    self.driver.implicitly_wait(2)

    self.driver.get("https://darichards-main-patch-0ecb.dva0ia48yehl5.amplifyapp.com/")
    self.driver.set_window_size(974, 1050)
    self.driver.find_element(By.ID, "profile-toggle").click()
    self.driver.find_element(By.ID, "home-user-1").click()
    self.driver.find_element(By.ID, "signInFormUsername").click()
    self.driver.find_element(By.ID, "signInFormUsername").send_keys("ilaidlaw")
    self.driver.find_element(By.ID, "signInFormPassword").send_keys("!Pa55w0rd5")
    self.driver.find_element(By.ID, "signInFormPassword").send_keys(Keys.ENTER)

    time.sleep(0.5)

    self.driver.find_element(By.ID, "profile-toggle").click()
    time.sleep(0.4)
    self.driver.find_element(By.ID, "home-user-1").click()

    # self.driver.get("https://darichards-main-patch-0ecb.dva0ia48yehl5.amplifyapp.com/admindashboard")
    self.driver.find_element(By.ID, "manageUsers").click()

    # give time for auth to work
    time.sleep(2)


    self.driver.find_element(By.XPATH, "//a[@href='#tab-3']").click()

    time.sleep(1)

    # Click once to sort alphabetically
    self.driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div[1]/div/div[1]/div/div[1]/div[1]/div/div/div[2]/div").click()
    assert self.driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div[1]/div/div[2]/div/div[1]/div[1]").text == "adiazsoriano"

  def test_nonAdminUserAccessDashboard(self):
    self.driver.implicitly_wait(2)

    self.driver.get("https://darichards-main-patch-0ecb.dva0ia48yehl5.amplifyapp.com/")
    self.driver.set_window_size(974, 1050)
    self.driver.find_element(By.ID, "profile-toggle").click()
    self.driver.find_element(By.ID, "home-user-1").click()
    self.driver.find_element(By.ID, "signInFormUsername").click()
    self.driver.find_element(By.ID, "signInFormUsername").send_keys("superGreatHacker123")
    self.driver.find_element(By.ID, "signInFormPassword").send_keys("Hacked123!")
    self.driver.find_element(By.ID, "signInFormPassword").send_keys(Keys.ENTER)

    time.sleep(0.5)

    self.driver.find_element(By.ID, "profile-toggle").click()
    time.sleep(0.4)
    self.driver.find_element(By.ID, "home-user-1").click()

    self.driver.find_element(By.ID, "manageUsers").click()

    # give time for auth to work
    time.sleep(2)

    try:
      self.driver.switch_to.alert.accept()
      return True
    except:
      return False
  def test_adminSetUserInfo(self):
    # self.driver.delete_all_cookies()

    self.driver.implicitly_wait(2)

    self.driver.get("https://darichards-main-patch-0ecb.dva0ia48yehl5.amplifyapp.com/")
    self.driver.set_window_size(974, 1050)
    self.driver.find_element(By.ID, "profile-toggle").click()
    self.driver.find_element(By.ID, "home-user-1").click()
    self.driver.find_element(By.ID, "signInFormUsername").click()
    self.driver.find_element(By.ID, "signInFormUsername").send_keys("ilaidlaw")
    self.driver.find_element(By.ID, "signInFormPassword").send_keys("!Pa55w0rd5")
    self.driver.find_element(By.ID, "signInFormPassword").send_keys(Keys.ENTER)

    time.sleep(0.5)

    self.driver.find_element(By.ID, "profile-toggle").click()
    time.sleep(0.4)
    self.driver.find_element(By.ID, "home-user-1").click()

    # self.driver.get("https://darichards-main-patch-0ecb.dva0ia48yehl5.amplifyapp.com/admindashboard")
    self.driver.find_element(By.ID, "manageUsers").click()

    self.driver.set_window_size(1100, 1050)
    # give time for auth to work
    time.sleep(2)

    self.driver.find_element(By.XPATH, "//a[@href='#tab-3']").click()

    time.sleep(1)

    self.driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div[1]/div/div[1]/div/div[1]/div[6]/div").click()
    self.driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div[1]/div/div[2]/div/div[1]/div[2]").click()
    self.driver.find_element(By.XPATH, "//*[@id='address']").clear()
    self.driver.find_element(By.XPATH, "//*[@id='address']").send_keys("New Address")
    self.driver.find_element(By.XPATH, "/html/body/div[3]/button[1]").click()

    self.driver.refresh()

    self.driver.find_element(By.XPATH, "//a[@href='#tab-3']").click()

    time.sleep(1)

    self.driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div[1]/div/div[1]/div/div[1]/div[6]/div").click()
    assert self.driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div[1]/div/div[2]/div/div[1]/div[4]").text == "New Address"

    self.driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div[1]/div/div[2]/div/div[1]/div[2]").click()
    self.driver.find_element(By.XPATH, "//*[@id='address']").clear()
    self.driver.find_element(By.XPATH, "//*[@id='address']").send_keys("Somewhere Rd, Moon City")
    self.driver.find_element(By.XPATH, "/html/body/div[3]/button[1]").click()

  def test_adminDeleteUser(self):
    self.driver.implicitly_wait(2)

    self.driver.get("https://darichards-main-patch-0ecb.dva0ia48yehl5.amplifyapp.com/")
    self.driver.set_window_size(974, 1050)
    self.driver.find_element(By.ID, "profile-toggle").click()
    self.driver.find_element(By.ID, "home-user-1").click()
    self.driver.find_element(By.ID, "signInFormUsername").click()
    self.driver.find_element(By.ID, "signInFormUsername").send_keys("ilaidlaw")
    self.driver.find_element(By.ID, "signInFormPassword").send_keys("!Pa55w0rd5")
    self.driver.find_element(By.ID, "signInFormPassword").send_keys(Keys.ENTER)

    time.sleep(0.5)

    self.driver.find_element(By.ID, "profile-toggle").click()
    time.sleep(0.4)
    self.driver.find_element(By.ID, "home-user-1").click()

    # self.driver.get("https://darichards-main-patch-0ecb.dva0ia48yehl5.amplifyapp.com/admindashboard")
    self.driver.find_element(By.ID, "manageUsers").click()

    # give time for auth to work
    time.sleep(2)


    self.driver.find_element(By.XPATH, "//a[@href='#tab-3']").click()

    time.sleep(1)

    self.driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div[1]/div/div[1]/div/div[1]/div[1]/div/div/div[2]/div").click()
    assert self.driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div[1]/div/div[2]/div/div[1]/div[1]").text == "aaaa"
    self.driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div[1]/div/div[2]/div/div[1]/div[2]").click()
    self.driver.find_element(By.XPATH, "/html/body/div[3]/button[1]").click()
    self.driver.refresh()

    self.driver.find_element(By.XPATH, "//a[@href='#tab-3']").click()

    self.driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div[1]/div/div[1]/div/div[1]/div[1]/div/div/div[2]/div").click()
    assert self.driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div[1]/div/div[2]/div/div[1]/div[1]").text != "aaaa"
