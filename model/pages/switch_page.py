from selene import browser, be, by

from model.warnings.warning_handler import WarningHandler


class SwitchPage:

    def open(self):
        browser.open('/')

    def open_and_close_cookie_warning(self):
        self.open()
        WarningHandler().close_cookie_warning()

    def switch_to_page(self, page_name):
        link = browser.element('.main-nav').should(be.visible)
        link.should(be.clickable).element(by.text(page_name)).click()
        browser.switch_to_next_tab()
