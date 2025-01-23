from selene import browser, be, by


class WarningHandler:

    def close_cookie_warning(self):
        try:
            if browser.element('.cookies-message.visible').should(be.visible):
                browser.element('.cookies-message').should(be.visible).element(by.text('СОГЛАСЕН')).click()
        except Exception:
            pass

    def close_handle_snackbar_if_present(self):
        try:
            if browser.element('.MuiSnackbar-root.MuiSnackbar-anchorOriginBottomCenter').should(be.visible):
                browser.element('.MuiSnackbar-root.MuiSnackbar-anchorOriginBottomCenter').element(by.text('OK')).click()
        except Exception:
            pass
