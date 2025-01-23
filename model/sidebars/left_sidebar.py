from selene import browser, be, by


class SidebarLeft:

    def open_sidebar(self):
        browser.element('.MuiIconButton-edgeStart').should(be.visible).click()

    def module_choice(self, module):
        element = browser.element('.MuiGrid-align-items-xs-flex-start')
        element.should(be.visible).element(by.text(module)).click()

        browser.execute_script("document.body.style.transform = 'scale(0.8';")
        browser.execute_script("document.body.style.transformOrigin = '0 0';")
