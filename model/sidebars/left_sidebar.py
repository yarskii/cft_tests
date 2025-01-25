from selene import browser, be, by


class SidebarLeft:

    def open_sidebar(self):
        browser.element('.MuiIconButton-edgeStart').should(be.visible).click()

    def module_choice(self, module):
        element = browser.element('.MuiGrid-align-items-xs-flex-start')
        element.should(be.visible).element(by.text(module)).click()
