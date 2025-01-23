import allure
from model.pages.search_information_page import SearchInformationPage
from model.sidebars.left_sidebar import SidebarLeft
from model.warnings.warning_handler import WarningHandler
from selene import browser


@allure.tag('web')
@allure.feature("Поиск информации")
@allure.label("owner", "Ярослав Гусев")
@allure.description("Тест для проверки информации на странице")
@allure.link("https://catalog.cft.ru/", name="Testing")
def test_search_about():
    search = SearchInformationPage()
    sidebar = SidebarLeft()
    warning = WarningHandler()

    with allure.step('Открывает сайт "https://catalog.cft.ru/"'):
        browser.open('https://catalog.cft.ru/')
        warning.close_handle_snackbar_if_present()

    with allure.step('Открываем боковую панель"'):
        sidebar.open_sidebar()

    with allure.step('Переходим на страницу "О Компании"'):
        sidebar.module_choice('О компании')

    with allure.step('Проверяем информацию на странице'):
        search.should_verify_text('ЗАО «Центр Финансовых Технологий» (ЗАО «ЦФТ») – '
                                  'российский разработчик программного обеспечения для финансового сектора, '
                                  'работает на рынке с 1991 года.')
