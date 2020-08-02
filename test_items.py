import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_verify_add_to_basket_button(browser):
    browser.get(link)
    time.sleep(10)
    add_to_basket_button = browser.find_element_by_xpath("//*[@id='add_to_basket_form']/button")
    assert add_to_basket_button, "There is no Add to Basket button!"