# CFT Tests

[![GitHub issues](https://img.shields.io/github/issues/yarskii/cft_tests)](https://github.com/yarskii/cft_tests/issues)
[![GitHub forks](https://img.shields.io/github/forks/yarskii/cft_tests)](https://github.com/yarskii/cft_tests/network)
[![GitHub stars](https://img.shields.io/github/stars/yarskii/cft_tests)](https://github.com/yarskii/cft_tests/stargazers)

Этот проект содержит автоматизированные тесты для веб-сайта [Центр Финансовых Технологий](https://www.cft.ru/).

## Описание

Проект включает в себя набор автоматизированных тестов, написанных с использованием фреймворков Selenium и Allure. Тесты проверяют функциональность сайта, включая переключение между вкладками, добавление товаров в корзину и загрузку файлов.

## Используемые инструменты

<p align="center">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original-wordmark.svg" alt="Python Logo" height="40" width="40" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/selenium/selenium-original.svg" height="40" width="40" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/chrome/chrome-original-wordmark.svg" alt="Chrome Logo" height="40" width="40" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/jenkins/jenkins-original.svg" alt="Jenkins Logo" height="40" width="40" />
  <img src="https://avatars.githubusercontent.com/u/5879127?s=200&v=4" alt="Allure Logo" height="40" width="40" />
  <img src="https://upload.wikimedia.org/wikipedia/commons/8/83/Telegram_2019_Logo.svg" alt="Telegram Logo" height="40" width="40" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pytest/pytest-original.svg" alt="Pytest Logo" height="40" width="40" />
</p>

### Selene

Selene — это удобная библиотека для автоматизации тестирования веб-приложений на Python. Она основана на Selenium и предоставляет более простой и удобный API для написания тестов.

### Allure

Allure — это гибкий легкий многоязычный фреймворк для создания отчетов о тестировании. Он предоставляет подробные отчеты о результатах тестирования.

### Python

Python — это высокоуровневый язык программирования общего назначения, который широко используется для автоматизации и тестирования.

### Jenkins

Jenkins — это популярный открытый сервер автоматизации, который можно использовать для автоматизации различных этапов разработки, включая сборку, тестирование и развертывание приложений. Jenkins может быть настроен для автоматического запуска ваших тестов после каждого коммита в репозиторий.

### Pytest

Pytest — это мощный и удобный фреймворк для написания и запуска тестов на Python. Он поддерживает множество плагинов и интеграций, что делает его идеальным выбором для автоматизированного тестирования.

## Содержание

- [Установка](#установка)
- [Запуск тестов](#запуск-тестов)
- [Генерация отчетов Allure](#генерация-отчетов-allure)
- [Лицензия](#лицензия)

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

## Лицензия

Этот проект лицензирован под MIT License. Подробности смотрите в файле [LICENSE](LICENSE).

---

Если у вас есть вопросы или предложения, пожалуйста, создайте issue на GitHub или свяжитесь со мной напрямую.

Автор: Ярослав Гусев