from selene import browser, be, by


class WarningHandler:

    def close_cookie_warning(self):
        cookie_message = browser.element('.cookies-message.visible').with_(timeout=5)
        if cookie_message.wait_until(be.visible):
            cookie_message.element(by.text('СОГЛАСЕН')).click()

    def close_handle_snackbar_if_present(self):
        snackbar = browser.element('.MuiSnackbar-root.MuiSnackbar-anchorOriginBottomCenter').with_(timeout=5)
        if snackbar.wait_until(be.visible):
            snackbar.element(by.text('OK')).click()
