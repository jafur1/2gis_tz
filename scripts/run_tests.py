#!/usr/bin/env python3
"""
Скрипт для запуска тестов с различными опциями
"""
import subprocess
import sys
import os
import argparse
from pathlib import Path


def run_command(command, description=""):
    """Выполнение команды с выводом результата"""
    if description:
        print(f"\n{'='*50}")
        print(f"Выполнение: {description}")
        print(f"Команда: {command}")
        print(f"{'='*50}")
    
    result = subprocess.run(command, shell=True)
    return result.returncode == 0


def generate_allure_report():
    """Генерация Allure отчета"""
    print("Генерация Allure отчета...")
    
    # Проверяем наличие результатов
    results_dir = Path("allure-results")
    if not results_dir.exists() or not list(results_dir.glob("*.json")):
        print("Ошибка: Нет результатов тестов для генерации отчета")
        return False
    
    # Пытаемся использовать allure commandline
    if run_command("allure generate allure-results -o allure-report --clean", "Генерация Allure отчета"):
        print("Allure отчет сгенерирован в папке allure-report/")
        return True
    
    # Если allure не установлен, используем наш Python генератор
    print("Allure commandline не найден, используем Python генератор...")
    if Path("generate_report.py").exists():
        return run_command("python generate_report.py", "Генерация HTML отчета")
    
    print("Ошибка: Не удалось сгенерировать отчет")
    return False


def serve_allure_report():
    """Запуск сервера для просмотра Allure отчета"""
    print("Запуск сервера Allure...")
    
    # Пытаемся использовать allure serve
    if run_command("allure serve allure-results", "Запуск Allure сервера"):
        return True
    
    # Если allure не установлен, открываем HTML отчет
    print("Allure commandline не найден, открываем HTML отчет...")
    if Path("test-report.html").exists():
        if sys.platform == "win32":
            os.startfile("test-report.html")
        else:
            run_command("xdg-open test-report.html", "Открытие HTML отчета")
        return True
    
    print("Ошибка: Не удалось открыть отчет")
    return False


def main():
    parser = argparse.ArgumentParser(description="Запуск тестов для effective-mobile.ru")
    
    # Основные опции
    parser.add_argument("-m", "--mark", help="Запуск тестов с определенным маркером (smoke, regression, navigation)")
    parser.add_argument("--browser", choices=["chromium", "firefox", "webkit"], default="chromium", help="Браузер для тестов")
    parser.add_argument("--headed", action="store_true", help="Запуск в видимом режиме")
    parser.add_argument("--parallel", type=int, help="Количество параллельных процессов")
    parser.add_argument("--generate-report", action="store_true", help="Генерация отчета после тестов")
    parser.add_argument("--serve-report", action="store_true", help="Открытие отчета в браузере после тестов")
    parser.add_argument("--file", help="Запуск конкретного файла тестов")
    parser.add_argument("--test", help="Запуск конкретного теста")
    
    args = parser.parse_args()
    
    print("Запуск тестов для effective-mobile.ru")
    print(f"Браузер: {args.browser}")
    print(f"Режим: {'headed' if args.headed else 'headless'}")
    
    # Формируем команду pytest
    python_cmd = sys.executable  # Используем текущий интерпретатор Python
    cmd_parts = [python_cmd, "-m", "pytest"]
    
    # Добавляем опции
    if args.mark:
        cmd_parts.extend(["-m", args.mark])
    
    if args.browser:
        cmd_parts.extend(["--browser", args.browser])
    
    if args.headed:
        cmd_parts.append("--headed")
    
    if args.parallel:
        cmd_parts.extend(["-n", str(args.parallel)])
    
    if args.file:
        cmd_parts.append(args.file)
    elif args.test:
        cmd_parts.append(args.test)
    else:
        cmd_parts.append("tests/")
    
    # Добавляем Allure опции
    cmd_parts.extend(["--alluredir=allure-results", "--clean-alluredir"])
    
    # Запускаем тесты
    command = " ".join(cmd_parts)
    success = run_command(command, "Запуск тестов")
    
    if not success:
        print("Тесты завершились с ошибками")
        sys.exit(1)
    
    print("\nТесты завершены успешно!")
    
    # Генерируем отчет если нужно
    if args.generate_report or args.serve_report:
        if not generate_allure_report():
            print("Предупреждение: Не удалось сгенерировать отчет")
    
    # Открываем отчет если нужно
    if args.serve_report:
        if not serve_allure_report():
            print("Предупреждение: Не удалось открыть отчет")
    
    print("\nГотово!")


if __name__ == "__main__":
    main()
