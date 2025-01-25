import allure

from model.pages.search_information_page import SearchInformationPage
from model.pages.navigation_helper import NavigationHelper
from model.warnings.warning_handler import WarningHandler

switch = NavigationHelper()
search = SearchInformationPage()
warning = WarningHandler()


@allure.tag('web')
@allure.feature("Переключение между вкладками")
@allure.story("Проверка корректного переключения между вкладками пользователем")
@allure.label("owner", "Ярослав Гусев")
@allure.description("Тест для проверки перехода по выбранному пути")
@allure.link("https://www.cft.ru/", name="Testing")
def test_switch_page_catalog():
    with allure.step('Открывает сайт "https://www.cft.ru/"'):
        switch.open()
        warning.close_cookie_warning()

    with allure.step('Проверяем содержимое домашней страницы'):
        search.validate_home_page_elements()

    with allure.step('Открываем "Каталоги решений и продуктов"'):
        switch.navigate_to_page('Каталоги решений')
        warning.close_handle_snackbar_if_present()

    with allure.step('Проверяем, что открыта страница "Каталоги решений и продуктов" '
                     'и отображается заголовок "Готовые Решения"'):
        search.verify_information_on_page('Готовые Решения')

    with allure.step('Закрываем новую вкладку и возвращаемся на главную страницу'):
        switch.close_new_page()

    with allure.step('Проверяем, что произошёл возврат на домашнюю страницу.'):
        search.validate_home_page_elements()


@allure.tag('web')
@allure.feature("Переключение между вкладками")
@allure.story("Проверка корректного переключения между вкладками пользователем")
@allure.label("owner", "Ярослав Гусев")
@allure.description("Тест для проверки перехода по выбранному пути")
@allure.link("https://www.cft.ru/", name="Testing")
def test_switch_page_cftbank():
    with allure.step('Открывает сайт "https://www.cft.ru/"'):
        switch.open_and_close_cookie_warning()

    with allure.step('Проверяем содержимое домашней страницы'):
        search.validate_home_page_elements()

    with allure.step('Открываем "ЦФТ-Банк в каталоге приложений"'):
        switch.navigate_to_page('ЦФТ-Банк в каталоге')
        warning.close_handle_snackbar_if_present()

    with allure.step('Проверяем, что открыта страница "Каталоги решений и продуктов" '
                     'и отображается заголовок "ЦФТ-Банк"'):
        search.verify_information_on_page('ЦФТ-Банк')

    with allure.step('Закрываем новую вкладку и возвращаемся на главную страницу'):
        switch.close_new_page()

    with allure.step('Проверяем, что произошёл возврат на домашнюю страницу.'):
        search.validate_home_page_elements()


@allure.tag('web')
@allure.feature("Переключение между вкладками")
@allure.story("Проверка корректного переключения между вкладками пользователем")
@allure.label("owner", "Ярослав Гусев")
@allure.description("Тест для проверки перехода по выбранному пути")
@allure.link("https://www.cft.ru/", name="Testing")
def test_switch_page_platforms():
    with allure.step('Открывает сайт "https://www.cft.ru/"'):
        switch.open_and_close_cookie_warning()

    with allure.step('Проверяем содержимое домашней страницы'):
        search.validate_home_page_elements()

    with allure.step('Открываем "Архитектура и платформы"'):
        switch.navigate_to_page('Архитектура')
        warning.close_handle_snackbar_if_present()

    with allure.step('Проверяем, что открыта страница "Каталоги решений и продуктов" '
                     'и отображается заголовок "Архитектура и платформы"'):
        search.verify_information_on_page('Архитектура и платформы', '.page-title')


@allure.tag('web')
@allure.feature("Переключение между вкладками")
@allure.story("Проверка корректного переключения между вкладками пользователем")
@allure.label("owner", "Ярослав Гусев")
@allure.description("Тест для проверки перехода по выбранному пути")
@allure.link("https://www.cft.ru/", name="Testing")
def test_switch_page_services():
    with allure.step('Открывает сайт "https://www.cft.ru/"'):
        switch.open_and_close_cookie_warning()

    with allure.step('Проверяем содержимое домашней страницы'):
        search.validate_home_page_elements()

    with allure.step('Открываем "Запуск, услуги АПК и сопровождение"'):
        switch.navigate_to_page('Запуск, услуги АПК')
        warning.close_handle_snackbar_if_present()

    with allure.step('Проверяем, что открыта страница "Каталоги решений и продуктов" '
                     'и отображается заголовок "Запуск, услуги АПК и сопровождение"'):
        search.verify_information_on_page('Запуск, услуги АПК и сопровождение', '.page-title')
