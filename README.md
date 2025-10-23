# Тесты для главной страницы effective-mobile.ru

Этот проект содержит автоматизированные тесты для главной страницы сайта [effective-mobile.ru](https://effective-mobile.ru), написанные с использованием Playwright, Page Object паттерна и Allure для отчетности.

## 🚀 Возможности

- ✅ **UI тесты** для проверки навигации по всем блокам главной страницы
- ✅ **Page Object паттерн** для удобного управления элементами страницы
- ✅ **Allure отчеты** с подробной информацией о выполнении тестов
- ✅ **Docker поддержка** для запуска тестов в контейнере
- ✅ **Параллельное выполнение** тестов для ускорения процесса
- ✅ **Адаптивное тестирование** для различных устройств
- ✅ **Проверка производительности** и консольных ошибок

## 📋 Требования

- **Python 3.10+**
- **Docker** (опционально, для контейнерного запуска)
- **Git** для клонирования репозитория

## 🚀 Быстрый старт

> 📖 **Подробная инструкция**: [QUICK_START.md](QUICK_START.md)

```bash
# 1. Клонирование репозитория
git clone <repository-url>
cd effective-mobile-tests

# 2. Создание виртуального окружения
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/macOS

# 3. Установка зависимостей
python scripts/install_dependencies.py

# 4. Запуск тестов
python scripts/run_tests.py

# 5. Просмотр отчета
python generate_report.py
# Откройте test-report.html в браузере
```

## 🛠 Установка и настройка

### Локальная установка

1. **Клонирование репозитория:**
   ```bash
   git clone <repository-url>
   cd effective-mobile-tests
   ```

2. **Создание виртуального окружения:**
   ```bash
   python -m venv venv
   
   # Windows
   venv\\Scripts\\activate
   
   # Linux/macOS
   source venv/bin/activate
   ```

3. **Автоматическая установка зависимостей:**
   ```bash
   python scripts/install_dependencies.py
   ```

   Или ручная установка:
   ```bash
   pip install -r requirements.txt
   playwright install
   playwright install-deps
   ```

### Docker установка

1. **Сборка образа:**
   ```bash
   docker build -t effective-mobile-tests .
   ```

2. **Или использование docker-compose:**
   ```bash
   docker-compose build
   ```

## 🧪 Запуск тестов

### Локальный запуск

#### Базовые команды

```bash
# Запуск всех тестов
python scripts/run_tests.py

# Запуск с определенным браузером
python scripts/run_tests.py --browser firefox

# Запуск в видимом режиме
python scripts/run_tests.py --headed

# Запуск с генерацией отчета
python scripts/run_tests.py --generate-report

# Запуск с открытием отчета в браузере
python scripts/run_tests.py --serve-report
```

#### Запуск по маркерам

```bash
# Только smoke тесты
python scripts/run_tests.py -m smoke

# Только навигационные тесты
python scripts/run_tests.py -m navigation

# Только регрессионные тесты
python scripts/run_tests.py -m regression

# Комбинация маркеров
python scripts/run_tests.py -m "smoke and navigation"
```

#### Параллельный запуск

```bash
# Запуск в 4 потока
python scripts/run_tests.py --parallel 4

# Запуск в 2 потока с определенным браузером
python scripts/run_tests.py --parallel 2 --browser chromium
```

#### Прямой запуск через pytest

```bash
# Все тесты
pytest

# Конкретный файл
pytest tests/test_main_page_navigation.py

# Конкретный тест
pytest tests/test_main_page_navigation.py::TestMainPageNavigation::test_navigate_to_about_page

# С маркерами
pytest -m smoke

# С браузером
pytest --browser firefox

# В видимом режиме
pytest --headed
```

### Docker запуск

#### Одиночный контейнер

```bash
# Запуск всех тестов
docker run --rm -v $(pwd)/allure-results:/app/allure-results effective-mobile-tests

# Запуск с определенными параметрами
docker run --rm -v $(pwd)/allure-results:/app/allure-results effective-mobile-tests python scripts/run_tests.py -m smoke
```

#### Docker Compose

```bash
# Запуск всех тестов
docker-compose up effective-mobile-tests

# Запуск только smoke тестов
docker-compose up effective-mobile-smoke-tests

# Запуск в headless режиме
docker-compose up effective-mobile-tests-headless
```

## 📊 Отчеты

### HTML отчеты (рекомендуется)

После выполнения тестов результаты сохраняются в директории `allure-results/`.

#### Генерация HTML отчета

```bash
# Генерация HTML отчета (встроенный генератор)
python generate_report.py

# Открытие отчета в браузере
# Windows: автоматически откроется в браузере по умолчанию
# Linux/macOS: xdg-open test-report.html
```

#### Автоматическая генерация

```bash
# Запуск тестов с автоматической генерацией отчета
python scripts/run_tests.py --generate-report

# Запуск тестов с автоматическим открытием отчета
python scripts/run_tests.py --serve-report
```

### Allure отчеты (опционально)

Если у вас установлен Allure commandline:

```bash
# Генерация статического отчета
allure generate allure-results -o allure-report --clean

# Запуск сервера для просмотра отчета
allure serve allure-results

# Открытие сгенерированного отчета
allure open allure-report
```

## 📁 Структура проекта

```
effective-mobile-tests/
├── pages_selector/               # Page Object классы и селекторы
│   ├── __init__.py
│   ├── base_page.py             # Базовый класс для всех страниц
│   ├── main_page.py             # Класс главной страницы
│   └── main_selector.py         # Селекторы элементов
├── tests/                       # Тестовые файлы
│   ├── __init__.py
│   ├── test_main_page_navigation.py    # Тесты навигации
│   └── test_main_page_functionality.py # Тесты функциональности
├── scripts/                     # Вспомогательные скрипты
│   ├── run_tests.py            # Скрипт запуска тестов
│   └── install_dependencies.py # Скрипт установки зависимостей
├── utils/                       # Утилиты
│   ├── __init__.py
│   └── config.py               # Конфигурация проекта
├── allure-results/             # Результаты Allure (создается автоматически)
├── test-results/               # Дополнительные результаты тестов
├── requirements.txt            # Python зависимости
├── pytest.ini                 # Конфигурация pytest
├── conftest.py                 # Фикстуры pytest
├── allure.properties          # Конфигурация Allure
├── Dockerfile                 # Docker образ
├── docker-compose.yml         # Docker Compose конфигурация
├── Makefile                   # Make команды
├── .dockerignore             # Исключения для Docker
├── .gitignore                # Исключения для Git
├── generate_report.py        # Генератор HTML отчетов
├── README.md                 # Документация
└── PROJECT_INFO.md           # Информация о проекте
```

## 🎯 Тестовые сценарии

### Навигационные тесты

- ✅ Переход на страницу "О нас"
- ✅ Переход на страницу "Контакты"
- ✅ Переход на страницу "Услуги"
- ✅ Переход на страницу "Портфолио"
- ✅ Переход на страницу "Блог"
- ✅ Переход на страницу "Карьера"

### Функциональные тесты

- ✅ Проверка кнопки "Связаться"
- ✅ Проверка кнопки "Заказать"
- ✅ Проверка телефонных ссылок
- ✅ Проверка email ссылок
- ✅ Адаптивность для мобильных устройств
- ✅ Производительность загрузки страницы
- ✅ Проверка консольных ошибок

### Структурные тесты

- ✅ Проверка наличия основных секций (header, footer, hero)
- ✅ Проверка навигационного меню
- ✅ Проверка контактной информации
- ✅ Проверка мета-информации страницы

## 🏷 Маркеры тестов

- `@pytest.mark.smoke` - Критически важные тесты
- `@pytest.mark.regression` - Регрессионные тесты
- `@pytest.mark.navigation` - Тесты навигации

## ⚙️ Конфигурация

### pytest.ini

Основные настройки pytest находятся в файле `pytest.ini`:

- Пути к тестам
- Маркеры
- Опции по умолчанию
- Настройки Allure

### conftest.py

Глобальные фикстуры и настройки:

- Настройки браузера
- Фикстуры для Page Object
- Обработка ошибок и скриншотов

## 🐛 Отладка

### Запуск в отладочном режиме

```bash
# Запуск в видимом режиме с замедлением
pytest --headed --slowmo 1000

# Запуск одного теста с подробным выводом
pytest -v -s tests/test_main_page_navigation.py::TestMainPageNavigation::test_navigate_to_about_page

# Запуск с остановкой на первой ошибке
pytest -x
```

### Просмотр логов

```bash
# Запуск с подробными логами
pytest --log-cli-level=DEBUG

# Сохранение логов в файл
pytest --log-file=test.log --log-cli-level=INFO
```

## 🔧 Устранение неполадок

### Частые проблемы

1. **Ошибка установки браузеров Playwright:**
   ```bash
   # Установка системных зависимостей
   playwright install-deps
   ```

2. **Проблемы с правами доступа (Linux/macOS):**
   ```bash
   sudo playwright install-deps
   ```

3. **Ошибки в Docker:**
   ```bash
   # Пересборка образа
   docker build --no-cache -t effective-mobile-tests .
   ```

4. **Проблемы с Allure:**
   ```bash
   # Установка Allure
   npm install -g allure-commandline
   ```

### Проверка окружения

```bash
# Проверка версии Python
python --version

# Проверка установленных пакетов
pip list

# Проверка браузеров Playwright
playwright --version
```

## 📈 Производительность

### Оптимизация скорости

- Используйте параллельный запуск: `--parallel 4`
- Запускайте только нужные тесты: `-m smoke`
- Используйте headless режим (по умолчанию)

### Мониторинг ресурсов

- Тесты автоматически измеряют время загрузки страниц
- Проверяются консольные ошибки
- Создаются скриншоты при падении тестов

## 🤝 Вклад в проект

1. Форкните репозиторий
2. Создайте ветку для новой функции
3. Внесите изменения
4. Добавьте тесты для новой функциональности
5. Убедитесь, что все тесты проходят
6. Создайте Pull Request

## 📝 Лицензия

Этот проект создан для демонстрации навыков автоматизации тестирования.

## 📞 Поддержка

При возникновении вопросов или проблем:

1. Проверьте раздел "Устранение неполадок"
2. Изучите логи выполнения тестов
3. Создайте Issue в репозитории

---

**Удачного тестирования! 🚀**

