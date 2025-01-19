from selene import browser, be, by


class SwitchPage:
    def open(self):
        browser.open('/')

    def close_cookie_warning(self):
        try:
            if browser.element('.cookies-message.visible').should(be.visible):
                browser.element('.cookies-message').should(be.visible).element(by.text('СОГЛАСЕН')).click()
        except Exception:
            pass

    def open_and_close_cookie_warning(self):
        self.open()
        self.close_cookie_warning()

    def switch_to_page(self, page_name):
        link = browser.element('.main-nav').should(be.visible)
        link.should(be.clickable).element(by.text(page_name)).click()

        browser.switch_to_next_tab()

    def handle_snackbar_if_present(self):
        try:
            if browser.element('.MuiSnackbar-root.MuiSnackbar-anchorOriginBottomCenter').should(be.visible):
                browser.element('.MuiSnackbar-root.MuiSnackbar-anchorOriginBottomCenter').element(by.text('OK')).click()
        except Exception:
            pass
