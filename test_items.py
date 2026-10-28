from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_add_to_basket_button_on_product_page(browser):
    browser.get(link)

    buttons = browser.find_elements(By.CSS_SELECTOR, "#add_to_basket_form button.btn-add-to-basket")

    assert len(buttons) == 1, "На странице товара нет кнопки добавления в корзину"
