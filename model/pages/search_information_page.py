from selene import browser, be, by, have
from scripts.file_system_operations import TMP_DIR
import time
import os
import shutil


class SearchInformationPage:
    def open(self):
        browser.open('https://catalog.cft.ru/')

    def close_cookie_warning(self):
        try:
            if browser.element('.cookies-message.visible').should(be.visible):
                browser.element('.cookies-message').should(be.visible).element(by.text('СОГЛАСЕН')).click()
        except Exception:
            pass

    def open_and_close_cookie_warning(self):
        self.open()
        self.close_cookie_warning()


    def handle_snackbar_if_present(self):
        try:
            if browser.element('.MuiSnackbar-root.MuiSnackbar-anchorOriginBottomCenter').should(be.visible):
                browser.element('.MuiSnackbar-root.MuiSnackbar-anchorOriginBottomCenter').element(by.text('OK')).click()
        except Exception:
            pass

    def should_verify_text(self, text):
        browser.element('#MainContainer').should(be.visible).should(have.text(text))

    def open_sidebar(self):
        browser.element('.MuiIconButton-edgeStart').should(be.visible).click()

    def module_choice(self, module):
        element = browser.element('.MuiGrid-align-items-xs-flex-start')
        element.should(be.visible).element(by.text(module)).click()

        browser.execute_script("document.body.style.transform = 'scale(0.8';")
        browser.execute_script("document.body.style.transformOrigin = '0 0';")

    def add_dependencies(self):
        browser.element(by.text('Добавить зависимости')).click()
        time.sleep(2)

    def export_to_excel(self):
        browser.element(by.text('Выгрузить в Excel')).click()
        time.sleep(3)

    def clear_cart(self):
        browser.element(by.text('Очистить')).click()
        answer = browser.element('.MuiSnackbar-anchorOriginBottomCenter').should(be.visible)
        answer.element(by.text('Да')).click()

    def add_all_in_basket(self):
        browser.element('.MuiButton-sizeSmall').should(be.visible).click()

    def select_favorite(self):
        browser.element('[aria-label="archive"]').should(be.visible).click()

    def select_cart(self):
        browser.element('a[href="/cart"]').should(be.visible).click()

    def select_profile(self):
        (browser.element('.MuiButtonBase-root.MuiIconButton-root[aria-label="avatar"]')
         .should(be.visible).click())

    def del_temporary_folder(self):
        if os.path.exists(TMP_DIR):
            shutil.rmtree(TMP_DIR)
