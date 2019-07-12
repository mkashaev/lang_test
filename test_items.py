
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_check_button(browser):
  browser.get(link)
  browser.find_element_by_xpath('//form[@class="add-to-basket"]/button')
  time.sleep(10)