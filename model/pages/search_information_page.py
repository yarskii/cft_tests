from selene import browser, be, have


class SearchInformationPage:
    def verify_information_on_page(self, text):
        browser.element('#MainContainer').should(be.visible).should(have.text(text))

    def validate_home_page_elements(self):
        browser.element('[href="/presscenter"]').should(have.text('Новости и публикации'))

    def verify_information_on_page_title(self, text):
        browser.element('.page-title').should(be.visible).should(have.text(text))
