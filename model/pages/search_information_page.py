from selene import browser, be, have


class SearchInformationPage:

    def should_verify_text(self, text):
        browser.element('#MainContainer').should(be.visible).should(have.text(text))

    def add_all_in_basket(self):
        browser.element('.MuiButton-sizeSmall').should(be.visible).click()
