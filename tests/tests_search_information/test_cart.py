import os
import allure
from selene import browser
from model.pages.cart_page import Cart
from model.pages.search_information_page import SearchInformationPage
from model.sidebars.left_sidebar import SidebarLeft
from model.warnings.warning_handler import WarningHandler
from scripts.file_system_operations import TMP_DIR
import shutil


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
        search.add_all_in_basket()

    with allure.step('Переходим в корзину'):
        cart.select_cart()

    with allure.step('Добавляем зависимости, выгружаем Exel файл и очищаем корзину'):
        cart.add_dependencies()
        cart.export_to_excel()
        cart.clear_cart()


@allure.tag('web')
@allure.feature("Проверка загруженного файла")
@allure.label("owner", "Ярослав Гусев")
@allure.description("Тест проверки скачанного файла из корзины")
@allure.link("https://catalog.cft.ru/", name="Testing")
def test_downloaded_file():
    with allure.step('Проверяем наличие скачанных файлов'):
        assert os.path.exists(TMP_DIR), f"Директория {TMP_DIR} не существует."

        files = os.listdir(TMP_DIR)
        assert len(files) > 0, 'Нет папки, либо папка пуста!'

        for file in files:
            file_xlsx = os.path.join(TMP_DIR, file)
            assert os.path.isfile(file_xlsx), f"Файл {file} не найден или это не файл."

            file_size = os.path.getsize(file_xlsx)
            assert file_size > 0, f"Файл {file} пустой."

            print(f'Файл {file} существует и содержит информацию.')

    with allure.step('Удаляем временные файлы'):
        if os.path.exists(TMP_DIR):
            shutil.rmtree(TMP_DIR)
