import allure
from model.pages.search_information_page import SearchInformationPage


@allure.tag('web')
@allure.feature("Поиск информации")
@allure.label("owner", "Ярослав Гусев")
@allure.description("Тест для проверки информации на странице")
@allure.link("https://www.cft.ru/", name="Testing")
def test_search_():
    search = SearchInformationPage()

    with allure.step('Открывает сайт "https://www.cft.ru/"'):
        search.open()

    with allure.step('Открываем "Каталоги решений и продуктов"'):
        search.switch_page('Каталоги решений')

    with allure.step('Открываем боковую панель"'):
        search.open_sidebar()

    with allure.step('Переходим на страницу "О Компании"'):
        search.module_choice('О компании')

    with allure.step('Проверяем информацию на странице'):
        search.should_search_text('ЗАО «Центр Финансовых Технологий» (ЗАО «ЦФТ») – '
                                  'российский разработчик программного обеспечения для финансового сектора, '
                                  'работает на рынке с 1991 года.')
