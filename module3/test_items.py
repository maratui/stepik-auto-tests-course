def test_page_contains_an_add_to_basket_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.implicitly_wait(20)
    browser.get(link)
    submit_button = browser.find_elements_by_css_selector("button.btn-add-to-basket")
    assert_condition = len(submit_button) == 1 and submit_button[0].get_attribute("type") == "submit"
    assert assert_condition, "The page does not contain an add to basket button"
