# CFT Tests

[![GitHub issues](https://img.shields.io/github/issues/yarskii/cft_tests)](https://github.com/yarskii/cft_tests/issues)
[![GitHub forks](https://img.shields.io/github/forks/yarskii/cft_tests)](https://github.com/yarskii/cft_tests/network)
[![GitHub stars](https://img.shields.io/github/stars/yarskii/cft_tests)](https://github.com/yarskii/cft_tests/stargazers)

Этот проект содержит автоматизированные тесты для веб-сайта [Центр Финансовых Технологий](https://www.cft.ru/).

## Описание

Проект включает в себя набор автоматизированных тестов, написанных с использованием фреймворков Selenium и Allure. Тесты проверяют функциональность сайта, включая переключение между вкладками, добавление товаров в корзину и загрузку файлов.

## Используемые инструменты

### Selene

<p align="center">
  <img src="https://raw.githubusercontent.com/yashaka/selene/master/docs/images/selene_logo.png" alt="Selene Logo" width="200" height="200">
</p>

Selene — это удобная библиотека для автоматизации тестирования веб-приложений на Python. Она основана на Selenium и предоставляет более простой и удобный API для написания тестов.

### Allure

<p align="center">
  <img src="https://allurereport.org/assets/images/allure-logo.svg" alt="Allure Logo" width="200" height="200">
</p>

Allure — это гибкий легкий многоязычный фреймворк для создания отчетов о тестировании. Он предоставляет подробные отчеты о результатах тестирования.

### Python

<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/200px-Python-logo-notext.svg.png" alt="Python Logo" width="200" height="200">
</p>

Python — это высокоуровневый язык программирования общего назначения, который широко используется для автоматизации и тестирования.

### Jenkins

<p align="center">
  <img src="https://www.jenkins.io/images/logos/jenkins/jenkins.png" alt="Jenkins Logo" width="200" height="200">
</p>

Jenkins — это популярный открытый сервер автоматизации, который можно использовать для автоматизации различных этапов разработки, включая сборку, тестирование и развертывание приложений. Jenkins может быть настроен для автоматического запуска ваших тестов после каждого коммита в репозиторий.

## Содержание

- [Установка](#установка)
- [Запуск тестов](#запуск-тестов)
- [Генерация отчетов Allure](#генерация-отчетов-allure)

## Установка

### Клонирование репозитория

    git clone https://github.com/yarskii/cft_tests.git
    cd cft_tests

### Создание виртуального окружения (опционально)

    python -m venv venv
    source venv/bin/activate  # Для Linux/macOS
    .\venv\Scripts\activate   # Для Windows

### Установка зависимостей

Создайте файл `requirements.txt`, содержащий список всех зависимостей проекта:

    pip freeze > requirements.txt

Затем установите зависимости:

    pip install -r requirements.txt


Если у вас уже есть файл `requirements.txt`, просто выполните команду:

    pip install -r requirements.txt

## Запуск тестов

### Локальный запуск

Для запуска всех тестов:

    pytest

Для запуска конкретного теста:

    pytest tests/test_switch_page_catalog.py

### Параметры запуска

Вы можете использовать различные параметры для управления поведением тестов:

- `-s`: Выводить все выводы в консоль.
- `-v`: Детализированное логирование.
- `--alluredir=allure-results`: Сохранять результаты тестов для генерации отчетов Allure.

Пример команды:

    pytest --alluredir=allure-results


## Генерация отчетов Allure

### Установка Allure Commandline

Следуйте инструкциям на официальном сайте [Allure](https://docs.qameta.io/allure/#_installing_a_commandline) для установки Allure Commandline.

### Генерация отчета

После выполнения тестов с параметром `--alluredir`, вы можете сгенерировать отчет следующей командой:

    allure serve allure-results

---

Если у вас есть вопросы или предложения, пожалуйста, создайте issue на GitHub или свяжитесь со мной напрямую.

Автор: Ярослав Гусев