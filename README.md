# Центр Финансовых Технологий

---

Этот проект содержит автоматизированные тесты для веб-сайта [Центр Финансовых Технологий](https://www.cft.ru/).

## Описание

Проект включает в себя набор автоматизированных тестов, написанных с использованием фреймворков Selene и Allure. Тесты
проверяют функциональность сайта, включая переключение между вкладками, добавление товаров в корзину и загрузку файлов.

---

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

**Selene** - это обертка над Selenium, облегчающая написание тестов и взаимодействие с веб‑элементами.

**Allure** - это инструмент для создания красочных отчетов о тестировании с поддержкой различных языков программирования.

**Pytest** - это фреймворк для написания и запуска тестов. Он предоставляет удобный синтаксис и разнообразные возможности для тестирования.

---

## Содержание

<details>
<summary>Установка</summary>

### Клонирование репозитория
   
Для начала работы, клонируйте репозиторий и перейдите в директорию проекта:
   ```sh
    git clone https://github.com/yarskii/cft_tests.git
    cd cft_tests
   ```
### Создание виртуального окружения (опционально)
   ```sh
    python -m venv venv
    source venv/bin/activate  # Для Linux/macOS
    .\venv\Scripts\activate   # Для Windows
   ```
### Установка зависимостей

Создайте файл `requirements.txt`, содержащий список всех зависимостей проекта:
   ```sh
    pip freeze > requirements.txt
   ```
Затем установите зависимости:
   ```sh
    pip install -r requirements.txt
   ```
Если у вас уже есть файл `requirements.txt`, просто выполните команду:
   ```sh
    pip install -r requirements.txt
   ```

</details>

<details>
<summary>Запуск тестов</summary>

### Локальный запуск

Чтобы запустить все тесты, выполните команду:
   ```sh
    pytest
   ```
Для запуска конкретного теста, используйте следующую команду:
   ```sh
    pytest tests/test_switch_page_catalog.py
   ```
### Параметры запуска

Вы можете использовать различные параметры для управления поведением тестов:

- `-s`: Выводить все выводы в консоль.
- `-v`: Детализированное логирование.
- `--alluredir=allure-results`: Сохранять результаты тестов для генерации отчетов Allure.

Пример команды:
   ```sh
    pytest --alluredir=allure-results
   ```
</details>


<details>
<summary>Генерация отчетов Allure</summary>

### Установка Allure Commandline

Следуйте инструкциям на официальном сайте [Allure](https://docs.qameta.io/allure/#_installing_a_commandline) для
установки Allure Commandline.

### Генерация отчета

После выполнения тестов с параметром `--alluredir`, вы можете сгенерировать отчет следующей командой:
   ```sh
    allure serve allure-results
   ```
</details>

<details>
<summary>Запуск проекта в Jenkins</summary>

1. Откройте [проект](https://jenkins.autotests.cloud/job/tests_cft/)
2. Выберите `Build with parameters`
3. Измените параметры, если требуется:
   - Укажите комментарий
   - Выберите вариант теста
   - Выберите версию браузера
4. Нажмите `Build`
5. После сборки, результат работы можно увидеть в `Allure Report`

> **Доступные параметры**:
> - Варианты тестов: `tests`, `tests/tests_switch_pages`, `tests/tests_search_information`
> - Версия браузера: `99`, `100`, `113`, `114`, `120`, `121`, `122`, `123`, `124`, `125`, `126`
---
</details>

## Диаграммы

### Последовательность действий при запуске тестов

```mermaid
sequenceDiagram
    participant Developer as Разработчик
    participant LocalEnv as Локальная Среда
    participant Jenkins as Jenkins
    participant Allure as Отчеты Allure

    Developer->>LocalEnv: Клонирование Репозитория
    LocalEnv->>Developer: Установка Зависимостей
    Developer->>LocalEnv: Активация Виртуального Окружения
    LocalEnv->>Jenkins: Пуш Кода
    Jenkins->>Jenkins: Сборка с Параметрами
    Jenkins->>Jenkins: Запуск Тестов
    Jenkins->>Allure: Генерация Отчета
    Allure-->>Developer: Просмотр Отчета
```
---

## Скриншоты

### Cтраница тестов Jenkins

   <p>
      <img src="https://github.com/yarskii/cft_tests/blob/main/docs/screenshots/jenkins_homepage.png" alt="Cтраница тестов Jenkins" width="630" height="320"/>
   </p>

### Общий отчёт Allure

   <p>
      <img src="https://github.com/yarskii/cft_tests/blob/main/docs/screenshots/allure_report.png" alt="Общий отчёт Allure" width="630" height="320"/>
   </p>

### Детальный отчёт о пройденном тесте

   <p>
      <img src="https://github.com/yarskii/cft_tests/blob/main/docs/screenshots/allure_tests.png" alt="Детальный отчёт о пройденном тесте" width="630" height="320"/>
   </p>

### Видео-отчет о прохождении теста
   
   <p>
      <img src="https://github.com/yarskii/cft_tests/blob/main/docs/screenshots/video_test.gif" alt="Видео-отчет о прохождении теста" width="630" height="320"/>
   </p>

### Отчет в Telegram

   <p>
      <img src="https://github.com/yarskii/cft_tests/blob/main/docs/screenshots/telegram.png" alt="Отчет в Telegram" width="630" height="320"/>
   </p>

---

## Лицензия

Этот проект лицензирован под MIT License. Подробности смотрите в файле [LICENSE](LICENSE).

---

Если у вас есть вопросы или предложения, пожалуйста, создайте issue на GitHub или свяжитесь со мной напрямую.

Автор: Ярослав Гусев