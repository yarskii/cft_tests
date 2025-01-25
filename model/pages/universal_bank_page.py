from selene import browser, be, have, by


class UniversalBankPage:

    def add_all_in_basket(self):
        element = browser.element('#S111').should(have.text('Обсудить с ЦФТ'))
        browser.driver.execute_script('arguments[0].scrollIntoView();', element.locate())
        browser.element('.MuiButton-sizeSmall').should(have.text('Добавить в корзину всё')).click()
