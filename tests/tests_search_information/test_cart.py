import os
import allure
from model.pages.search_information_page import SearchInformationPage
from selenium import webdriver
from scripts.file_system_operations import TMP_DIR


@allure.tag('web')
@allure.feature("Загрузка файла из корзины")
@allure.label("owner", "Ярослав Гусев")
@allure.description("Тест добавления файлов в корзину и проверки заказа")
@allure.link("https://catalog.cft.ru/", name="Testing")
def test_cart():
    options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": TMP_DIR,
        "download.prompt_for_download": False,
    }
    options.add_experimental_option("prefs", prefs)

    search = SearchInformationPage()

    with allure.step('Открывает сайт "https://catalog.cft.ru/"'):
        search.open()
        search.handle_snackbar_if_present()

    with allure.step('Открываем боковую панель"'):
        search.open_sidebar()

    with allure.step('Открываем вкладку "Готовые Решения"'):
        search.module_choice('Готовые Решения')

    with allure.step('Переходим на страницу "Универсальный банк"'):
        search.module_choice('Универсальный банк')

    with allure.step('Добавляем все в корзину"'):
        search.add_all_in_basket()

    with allure.step('Переходим в корзину'):
        search.select_cart()

    with allure.step('Добавляем зависимости, выгружаем Exel файл и очищаем корзину'):
        search.add_dependencies()
        search.export_to_excel()
        search.clear_cart()


@allure.tag('web')
@allure.feature("Проверка загруженного файла")
@allure.label("owner", "Ярослав Гусев")
@allure.description("Тест проверки скачанного файла из корзины")
@allure.link("https://catalog.cft.ru/", name="Testing")
def test_downloaded_file():
    search = SearchInformationPage()

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
        search.del_temporary_folder()
