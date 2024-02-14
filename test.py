#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import time

import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
    # self.driver.delete_all_cookies()
    self.driver.get("https://darichards-main-patch-0ecb.dva0ia48yehl5.amplifyapp.com/")
    self.driver.set_window_size(974, 1050)
    self.driver.find_element(By.ID, "profile-toggle").click()
    self.driver.find_element(By.ID, "home-user-1").click()
    self.driver.find_element(By.ID, "signInFormUsername").click()
    self.driver.find_element(By.ID, "signInFormUsername").send_keys("ilaidlaw")
    self.driver.find_element(By.ID, "signInFormPassword").send_keys("!Pa55w0rd5")
    self.driver.find_element(By.ID, "signInFormPassword").send_keys(Keys.ENTER)
    # element = WebDriverWait(self.driver, timeout=5).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='home-user-1']")))
    # element.click()
    # self.driver.find_element(By.XPATH, "//*[@id='profile-toggle']").click()
    # WebDriverWait(self.driver, timeout=5).until(EC.element_to_be_clickable(self.driver.find_element(By.XPATH, "//*[@id='home-user-1']"))).click()
    self.driver.get("https://darichards-main-patch-0ecb.dva0ia48yehl5.amplifyapp.com/accountPage")
    assert self.driver.find_element(By.XPATH, "//*[@id='name']").text == "Ian Laidlaw"
    assert self.driver.find_element(By.XPATH, "//*[@id='email']").text == "ilaidlaw@radford.edu"
    assert self.driver.find_element(By.XPATH, "//*[@id='address']").text == "Somewhere Rd, Moon City"

  def test_getAdminUsersInfo(self):
    # self.driver.delete_all_cookies()

    self.driver.get("https://darichards-main-patch-0ecb.dva0ia48yehl5.amplifyapp.com/")
    self.driver.set_window_size(974, 1050)
    self.driver.find_element(By.ID, "profile-toggle").click()
    self.driver.find_element(By.ID, "home-user-1").click()
    self.driver.find_element(By.ID, "signInFormUsername").click()
    self.driver.find_element(By.ID, "signInFormUsername").send_keys("ilaidlaw")
    self.driver.find_element(By.ID, "signInFormPassword").send_keys("!Pa55w0rd5")
    self.driver.find_element(By.ID, "signInFormPassword").send_keys(Keys.ENTER)

    self.driver.get("https://darichards-main-patch-0ecb.dva0ia48yehl5.amplifyapp.com/admindashboard")

    self.driver.find_element(By.XPATH, "//a[@href='#tab-3']").click()
    # Click once to sort alphabetically
    self.driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div[1]/div/div[1]/div/div[1]/div[1]/div/div/div[2]/div").click()
    assert self.driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div[1]/div/div[2]/div/div[1]/div[1]").text == "adiazsoriano"

  def test_adminSetUserInfo(self):
    self.driver.get("https://darichards-main-patch-0ecb.dva0ia48yehl5.amplifyapp.com/")
    self.driver.set_window_size(974, 1050)
    self.driver.find_element(By.ID, "profile-toggle").click()
    self.driver.find_element(By.ID, "home-user-1").click()
    self.driver.find_element(By.ID, "signInFormUsername").click()
    self.driver.find_element(By.ID, "signInFormUsername").send_keys("ilaidlaw")
    self.driver.find_element(By.ID, "signInFormPassword").send_keys("!Pa55w0rd5")
    self.driver.find_element(By.ID, "signInFormPassword").send_keys(Keys.ENTER)

    time.sleep(1)

    self.driver.get("https://darichards-main-patch-0ecb.dva0ia48yehl5.amplifyapp.com/admindashboard")

    time.sleep(2)

    self.driver.find_element(By.XPATH, "//a[@href='#tab-3']").click()

    # WebDriverWait(self.driver, timeout=5).until(EC.element_to_be_clickable(self.driver.find_element(By.XPATH, "//*[@id='home-user-1']"))).click()

    self.driver.find_element(By.XPATH,"/html/body/div/div/div[3]/div[1]/div/div[1]/div/div[1]/div[6]/div/div/div[2]/div").click()
    assert self.driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div[1]/div/div[2]/div/div[1]/div[1]").text == "ilaidlaw"
    self.driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div[1]/div/div[2]/div/div[1]/div[1]").click()
    self.driver.find_element(By.XPATH, "//*[@id='address']").send_keys("New Address")
    self.driver.find_element(By.XPATH, "/html/body/div[2]/button[1]").click()
    self.driver.refresh()
    self.driver.find_element(By.XPATH, "//a[@href='#tab-3']").click()
    self.driver.find_element(By.XPATH,"/html/body/div/div/div[3]/div[1]/div/div[1]/div/div[1]/div[6]/div/div/div[2]/div").click()
    assert self.driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div[1]/div/div[2]/div/div[1]/div[4]").text == "New Address"

