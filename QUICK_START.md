# 🚀 Быстрый старт

## Минимальные требования
- Python 3.10+
- Git

## Установка и запуск (5 минут)

### 1. Клонирование проекта
```bash
git clone <repository-url>
cd effective-mobile-tests
```

### 2. Создание виртуального окружения
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/macOS
python3 -m venv venv
source venv/bin/activate
```

### 3. Установка зависимостей
```bash
python scripts/install_dependencies.py
```

### 4. Запуск тестов
```bash
python scripts/run_tests.py
```

### 5. Просмотр отчета
```bash
python generate_report.py
# Откройте test-report.html в браузере
```

## Альтернативные способы запуска

### Запуск конкретных тестов
```bash
# Только smoke тесты
python scripts/run_tests.py -m smoke

# Только навигационные тесты
python scripts/run_tests.py -m navigation

# Конкретный файл
python scripts/run_tests.py --file tests/test_main_page_navigation.py
```

### Запуск с отчетами
```bash
# С автоматической генерацией отчета
python scripts/run_tests.py --generate-report

# С автоматическим открытием отчета
python scripts/run_tests.py --serve-report
```

### Запуск в видимом режиме
```bash
python scripts/run_tests.py --headed
```

## Прямой запуск через pytest
```bash
# Все тесты
python -m pytest

# Конкретный файл
python -m pytest tests/test_main_page_navigation.py

# С маркерами
python -m pytest -m smoke
```

## Возможные проблемы

### 1. Ошибка "python не найден"
**Решение:** Используйте полный путь к Python или установите Python

### 2. Ошибка установки браузеров Playwright
**Решение:** 
```bash
playwright install-deps
# На Linux/macOS может потребоваться sudo
```

### 3. Ошибки импорта
**Решение:** Убедитесь, что виртуальное окружение активировано

### 4. Тесты не запускаются
**Решение:** Проверьте, что все зависимости установлены:
```bash
pip list | grep -E "(playwright|pytest|allure)"
```

## Структура результатов

После запуска тестов вы получите:
- `allure-results/` - результаты тестов в формате Allure
- `test-results/` - дополнительные результаты (видео, скриншоты)
- `test-report.html` - HTML отчет (после генерации)

## Что тестируется

- ✅ Навигация по всем разделам сайта
- ✅ Функциональность кнопок и ссылок
- ✅ Адаптивность для мобильных устройств
- ✅ Производительность загрузки
- ✅ Отсутствие критических ошибок в консоли

## Поддержка

При возникновении проблем:
1. Проверьте раздел "Возможные проблемы"
2. Изучите логи выполнения тестов
3. Создайте Issue в репозитории

---
**Готово! Теперь вы можете запускать тесты для effective-mobile.ru** 🎉
