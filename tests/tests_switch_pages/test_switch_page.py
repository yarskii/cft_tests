from selene import browser
import allure

from model.pages.search_information_page import SearchInformationPage


@allure.tag('web')
@allure.feature("Переключение между вкладками")
@allure.story("Проверка корректного переключения между вкладками пользователем")
@allure.label("owner", "Ярослав Гусев")
@allure.description("Тест для проверки перехода по выбранному пути")
@allure.link("https://www.cft.ru/", name="Testing")
def test_switch_page_catalog():
    search = SearchInformationPage()

    with allure.step('Открывает сайт "https://www.cft.ru/"'):
        search.open()

    with allure.step('Открываем "Каталоги решений и продуктов"'):
        search.switch_page('Каталоги решений')

    with allure.step('Проверяем URL новой вкладки'):
        search.should_new_link('https://catalog.cft.ru/')

    with allure.step('Проверяем количество открытых вкладок'):
        if len(browser.driver.window_handles) > 1:
            with allure.step('Закрываем новую вкладку и возвращаемся на главную страницу'):
                browser.close_current_tab()
                browser.switch_to_tab(-1)


def test_switch_page_cftbank():
    search = SearchInformationPage()

    with allure.step('Открывает сайт "https://www.cft.ru/"'):
        search.open()

    with allure.step('Открываем "ЦФТ-Банк в каталоге приложений"'):
        search.switch_page('ЦФТ-Банк в каталоге')

    with allure.step('Проверяем URL новой вкладки'):
        search.should_new_link('https://catalog.cft.ru/applications/cftbank/overview')

    with allure.step('Проверяем количество открытых вкладок'):
        if len(browser.driver.window_handles) > 1:
            with allure.step('Закрываем новую вкладку и возвращаемся на главную страницу'):
                browser.close_current_tab()
                browser.switch_to_tab(-1)


def test_switch_page_platforms():
    search = SearchInformationPage()

    with allure.step('Открывает сайт "https://www.cft.ru/"'):
        search.open()

    with allure.step('Открываем "Архитектура и платформы"'):
        search.switch_page('Архитектура')

    with allure.step('Проверяем URL новой вкладки'):
        search.should_new_link('https://www.cft.ru/platforms')

    with allure.step('Проверяем количество открытых вкладок'):
        if len(browser.driver.window_handles) > 1:
            with allure.step('Закрываем новую вкладку и возвращаемся на главную страницу'):
                browser.close_current_tab()
                browser.switch_to_tab(-1)


def test_switch_page_services():
    search = SearchInformationPage()

    with allure.step('Открывает сайт "https://www.cft.ru/"'):
        search.open()

    with allure.step('Открываем "Запуск, услуги АПК и сопровождение"'):
        search.switch_page('Запуск, услуги АПК')

    with allure.step('Проверяем URL новой вкладки'):
        search.should_new_link('https://www.cft.ru/services')

    with allure.step('Проверяем количество открытых вкладок'):
        if len(browser.driver.window_handles) > 1:
            with allure.step('Закрываем новую вкладку и возвращаемся на главную страницу'):
                browser.close_current_tab()
                browser.switch_to_tab(-1)
