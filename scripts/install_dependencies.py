#!/usr/bin/env python3
"""
Скрипт для установки всех зависимостей проекта
"""
import subprocess
import sys
import os


def run_command(command, description):
    """Выполнение команды с выводом результата"""
    print(f"\n{'='*50}")
    print(f"Выполнение: {description}")
    print(f"Команда: {command}")
    print(f"{'='*50}")
    
    result = subprocess.run(command, shell=True)
    
    if result.returncode != 0:
        print(f"Ошибка выполнения команды (код: {result.returncode})")
        return False
    
    return True


def main():
    print("Установка зависимостей для проекта effective-mobile.ru тестов")
    
    # Проверка версии Python
    python_version = sys.version_info
    if python_version.major != 3 or python_version.minor < 10:
        print(f"Ошибка: Требуется Python 3.10+, текущая версия: {python_version.major}.{python_version.minor}")
        sys.exit(1)
    
    print(f"Python версия: {python_version.major}.{python_version.minor}.{python_version.micro}")
    
    # Установка зависимостей из requirements.txt
    if not run_command("pip install -r requirements.txt", "Установка Python зависимостей"):
        sys.exit(1)
    
    # Установка браузеров Playwright
    if not run_command("playwright install", "Установка браузеров Playwright"):
        sys.exit(1)
    
    # Установка системных зависимостей для Playwright
    if not run_command("playwright install-deps", "Установка системных зависимостей Playwright"):
        print("Предупреждение: Не удалось установить системные зависимости Playwright")
        print("Это может потребовать sudo/администраторских прав")
    
    print("\n" + "="*50)
    print("Установка завершена успешно!")
    print("Теперь вы можете запустить тесты:")
    print("python scripts/run_tests.py")
    print("="*50)


if __name__ == "__main__":
    main()


