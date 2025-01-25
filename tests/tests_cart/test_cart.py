import allure
from selene import browser

from model.download.download_files import DownloadFiles
from model.pages.cart_page import Cart
from model.pages.search_information_page import SearchInformationPage
from model.pages.universal_bank_page import UniversalBankPage
from model.sidebars.left_sidebar import SidebarLeft
from model.warnings.warning_handler import WarningHandler


@allure.tag('web')
@allure.feature("Загрузка файла из корзины")
@allure.label("owner", "Ярослав Гусев")
@allure.description("Тест добавления файлов в корзину и проверки заказа")
@allure.link("https://catalog.cft.ru/", name="Testing")
def test_cart():
    search = SearchInformationPage()
    warning = WarningHandler()
    sidebar = SidebarLeft()
    cart = Cart()
    universal_bank_page = UniversalBankPage()

    with allure.step('Открывает сайт "https://catalog.cft.ru/"'):
        browser.open('https://catalog.cft.ru/')
        warning.close_handle_snackbar_if_present()

    with allure.step('Открываем боковую панель"'):
        sidebar.open_sidebar()

    with allure.step('Открываем вкладку "Готовые Решения"'):
        sidebar.module_choice('Готовые Решения')

    with allure.step('Переходим на страницу "Универсальный банк"'):
        sidebar.module_choice('Универсальный банк')

    with allure.step('Добавляем все в корзину"'):
        universal_bank_page.add_all_in_basket()

    with allure.step('Переходим в корзину'):
        cart.select_cart()

    with allure.step('Проверяем, что корзина не пустая'):
        cart.checking_shopping_cart()

    with allure.step('Добавляем зависимости, выгружаем Exel файл и очищаем корзину'):
        cart.add_dependencies()
        cart.export_to_excel()
        cart.clear_cart()

    with allure.step('Проверяем, что корзина очищена'):
        search.verify_information_on_page("Суммарная стоимость комплектации: 0 тыс.у.е.")


@allure.tag('web')
@allure.feature("Проверка загруженного файла")
@allure.label("owner", "Ярослав Гусев")
@allure.description("Тест проверки скачанного файла из корзины")
@allure.link("https://catalog.cft.ru/", name="Testing")
def test_downloaded_file():
    file = DownloadFiles()

    with allure.step('Проверяем наличие скачанных файлов'):
        file.checking_download_file()

    with allure.step('Удаляем временные файлы'):
        file.delete_file()
