from selene import browser, be, by, have
from resources.script_os import TMP_DIR
import time
import os
import shutil


class SearchInformationPage:
    def open(self):
        browser.open('/')

        try:
            if browser.element('.cookies-message.visible').should(be.visible):
                browser.element('.cookies-message').should(be.visible).element(by.text('СОГЛАСЕН')).click()
        except Exception:
            pass

    def switch_page(self, page):
        link = browser.element('.main-nav').should(be.visible)
        link.should(be.clickable).element(by.text(page)).click()

        browser.switch_to_next_tab()

        try:
            if browser.element('.MuiSnackbar-root.MuiSnackbar-anchorOriginBottomCenter').should(be.visible):
                browser.element('.MuiSnackbar-root.MuiSnackbar-anchorOriginBottomCenter').element(by.text('OK')).click()
        except Exception:
            pass

    def should_new_link(self, link):
        browser.should(have.url_containing(f'{link}'))

    def should_search_text(self, text):
        browser.element('#MainContainer').should(be.visible).should(have.text(text))

    def open_sidebar(self):
        browser.element('.MuiIconButton-edgeStart').should(be.visible).click()

    def module_choice(self, module):
        element = browser.element('.MuiGrid-align-items-xs-flex-start')
        element.should(be.visible).element(by.text(module)).click()

        browser.execute_script("document.body.style.transform = 'scale(0.8';")
        browser.execute_script("document.body.style.transformOrigin = '0 0';")

    def process(self, process):
        if process == 'Добавить зависимости':
            browser.element(by.text('Добавить зависимости')).click()
            time.sleep(2)
        elif process == 'Выгрузить в Excel':
            browser.element(by.text('Выгрузить в Excel')).click()
            time.sleep(3)
        elif process == 'Очистить корзину':
            browser.element(by.text('Очистить')).click()
            answer = browser.element('.MuiSnackbar-anchorOriginBottomCenter').should(be.visible)
            answer.element(by.text('Да')).click()


    def add_all_in_basket(self):
        browser.element('.MuiButton-sizeSmall').should(be.visible).click()


    def user_dashboard_actions(self, actions):
        if actions == 'Избранное':
            browser.element('.MuiIconButton-label-69').should(be.visible).click()
        elif actions == 'Корзина':
            browser.element('.MuiIconButton-label-79').should(be.visible).click()
        elif actions == 'Профиль':
            (browser.element('.MuiButtonBase-root.MuiIconButton-root[aria-label="avatar"]')
             .should(be.visible).click())


    def del_temporary_folder(self):
        if os.path.exists(TMP_DIR):
            shutil.rmtree(TMP_DIR)

# def fill_language_in_search(self, language):
#     browser.element('.crUkSt').should(be.visible).type(language).press_enter()
#
# def count_vacancy(self):
#     return len(browser.all('.sc-bdvvtL>.fmUtEX'))
#
# def fill_city(self, city):
#     browser.element('.bANYmh').should(be.visible).type(city)
#     browser.element('.ftDrAW').should(be.visible).element(by.text(f'г {city}')).click()
#
# def fill_professional_area(self, area):
#     browser.element('.bSXks').should(be.visible).click()
#
#     if area == 'all':
#         for element in browser.all('.hvRHtH'):
#             element.click()
#     else:
#         browser.element('.fUuyoW').should(be.visible).element(by.text(area)).click()
#
# def should_number_vacancies(self):
#     if self.count_vacancy() > 0:
#         browser.element('.gNzDRP').should(be.visible).should(have.text(
#             f'Найдено вакансий: {self.count_vacancy()}'))
#     else:
#         browser.element('.hePNzJ').should(be.visible).should(have.text('Ничего не нашлось'))
#
# def fill_filter(self, interests):
#     if interests == 'all':
#         browser.element('.btitRc').click()
#         for element in browser.all('.hvRHtH'):
#             element.click()
#         browser.element('.hynlfB').click()
#
#     elif interests == 'clear':
#         browser.element('.gqakuA').click()
#         browser.element('.bJHLon').should(be.visible).element(by.text('Сбросить все')).click()
#
#     else:
#         browser.element('.btitRc').click()
#         for interest in interests:
#             browser.element('.bRwUWm').should(be.visible).element(by.text(interest)).click()
#         browser.element('.hynlfB').click()
#

#
# def social_button(self, link):
#     footer = browser.element('.lfGoOI')
#     telegram_button = footer.element(f'a[href="{link}"]')
#     telegram_button.should(be.visible)
#     telegram_button.should(be.clickable).click()
#
# def should_new_link(self, link):
#     browser.should(have.url_containing(f'{link}'))
#     browser.close_current_tab()
