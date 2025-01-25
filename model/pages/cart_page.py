from selene import browser, be, by, have
import time


class Cart:

    def select_cart(self):
        browser.element('a[href="/cart"]').should(be.visible).click()

    def checking_shopping_cart(self):
        browser.all('.MuiPagination-ul').should(have.size_greater_than(1))

    def add_dependencies(self):
        browser.element(by.text('Добавить зависимости')).click()
        time.sleep(2)

    def export_to_excel(self):
        browser.element(by.text('Выгрузить в Excel')).click()
        time.sleep(3)

    def clear_cart(self):
        browser.element(by.text('Очистить')).click()
        answer = browser.element('.MuiSnackbar-anchorOriginBottomCenter').should(be.visible)
        answer.element(by.text('Да')).click()
