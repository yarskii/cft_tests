from selene import browser, be, have


class SearchInformationPage:
    def verify_information_on_page(self, text, selector_priority='#MainContainer'):
        if selector_priority == '.page-title':
            browser.element(selector_priority).should(be.visible).should(have.text(text))
        browser.element(selector_priority).should(be.visible).should(have.text(text))

    def validate_home_page_elements(self):
        browser.element('[href="/presscenter"]').should(have.text('Новости и публикации'))
