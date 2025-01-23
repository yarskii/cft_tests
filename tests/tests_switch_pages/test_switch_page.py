from selene import browser
import allure
from model.pages.switch_page import SwitchPage
from model.warnings.warning_handler import WarningHandler


@allure.tag('web')
@allure.feature("Переключение между вкладками")
@allure.story("Проверка корректного переключения между вкладками пользователем")
@allure.label("owner", "Ярослав Гусев")
@allure.description("Тест для проверки перехода по выбранному пути")
@allure.link("https://www.cft.ru/", name="Testing")
def test_switch_page_catalog():
    search = SwitchPage()
    warning = WarningHandler()

    with allure.step('Открывает сайт "https://www.cft.ru/"'):
        search.open()
        warning.close_cookie_warning()

    with allure.step('Открываем "Каталоги решений и продуктов"'):
        search.switch_to_page('Каталоги решений')
        warning.close_handle_snackbar_if_present()

    with allure.step('Проверяем количество открытых вкладок'):
        if len(browser.driver.window_handles) > 1:
            with allure.step('Закрываем новую вкладку и возвращаемся на главную страницу'):
                browser.close_current_tab()
                browser.switch_to_tab(-1)


@allure.tag('web')
@allure.feature("Переключение между вкладками")
@allure.story("Проверка корректного переключения между вкладками пользователем")
@allure.label("owner", "Ярослав Гусев")
@allure.description("Тест для проверки перехода по выбранному пути")
@allure.link("https://www.cft.ru/", name="Testing")
def test_switch_page_cftbank():
    search = SwitchPage()
    warning = WarningHandler()

    with allure.step('Открывает сайт "https://www.cft.ru/"'):
        search.open_and_close_cookie_warning()

    with allure.step('Открываем "ЦФТ-Банк в каталоге приложений"'):
        search.switch_to_page('ЦФТ-Банк в каталоге')
        warning.close_handle_snackbar_if_present()

    with allure.step('Проверяем количество открытых вкладок'):
        if len(browser.driver.window_handles) > 1:
            with allure.step('Закрываем новую вкладку и возвращаемся на главную страницу'):
                browser.close_current_tab()
                browser.switch_to_tab(-1)


@allure.tag('web')
@allure.feature("Переключение между вкладками")
@allure.story("Проверка корректного переключения между вкладками пользователем")
@allure.label("owner", "Ярослав Гусев")
@allure.description("Тест для проверки перехода по выбранному пути")
@allure.link("https://www.cft.ru/", name="Testing")
def test_switch_page_platforms():
    search = SwitchPage()
    warning = WarningHandler()

    with allure.step('Открывает сайт "https://www.cft.ru/"'):
        search.open_and_close_cookie_warning()

    with allure.step('Открываем "Архитектура и платформы"'):
        search.switch_to_page('Архитектура')
        warning.close_handle_snackbar_if_present()

    with allure.step('Проверяем количество открытых вкладок'):
        if len(browser.driver.window_handles) > 1:
            with allure.step('Закрываем новую вкладку и возвращаемся на главную страницу'):
                browser.close_current_tab()
                browser.switch_to_tab(-1)


@allure.tag('web')
@allure.feature("Переключение между вкладками")
@allure.story("Проверка корректного переключения между вкладками пользователем")
@allure.label("owner", "Ярослав Гусев")
@allure.description("Тест для проверки перехода по выбранному пути")
@allure.link("https://www.cft.ru/", name="Testing")
def test_switch_page_services():
    search = SwitchPage()
    warning = WarningHandler()

    with allure.step('Открывает сайт "https://www.cft.ru/"'):
        search.open_and_close_cookie_warning()

    with allure.step('Открываем "Запуск, услуги АПК и сопровождение"'):
        search.switch_to_page('Запуск, услуги АПК')
        warning.close_handle_snackbar_if_present()

    with allure.step('Проверяем количество открытых вкладок'):
        if len(browser.driver.window_handles) > 1:
            with allure.step('Закрываем новую вкладку и возвращаемся на главную страницу'):
                browser.close_current_tab()
                browser.switch_to_tab(-1)
