# Makefile для управления проектом тестов effective-mobile.ru

.PHONY: help install test test-smoke test-navigation test-regression test-parallel test-headed test-report test-serve clean docker-build docker-run docker-compose-up docker-compose-down

# Цвета для вывода
GREEN=\033[0;32m
YELLOW=\033[1;33m
RED=\033[0;31m
NC=\033[0m # No Color

help: ## Показать справку
	@echo "$(GREEN)Доступные команды:$(NC)"
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  $(YELLOW)%-20s$(NC) %s\n", $$1, $$2}' $(MAKEFILE_LIST)

install: ## Установить все зависимости
	@echo "$(GREEN)Установка зависимостей...$(NC)"
	python scripts/install_dependencies.py

test: ## Запустить все тесты
	@echo "$(GREEN)Запуск всех тестов...$(NC)"
	python scripts/run_tests.py

test-smoke: ## Запустить только smoke тесты
	@echo "$(GREEN)Запуск smoke тестов...$(NC)"
	python scripts/run_tests.py -m smoke

test-navigation: ## Запустить только навигационные тесты
	@echo "$(GREEN)Запуск навигационных тестов...$(NC)"
	python scripts/run_tests.py -m navigation

test-regression: ## Запустить только регрессионные тесты
	@echo "$(GREEN)Запуск регрессионных тестов...$(NC)"
	python scripts/run_tests.py -m regression

test-parallel: ## Запустить тесты в параллельном режиме
	@echo "$(GREEN)Запуск тестов в параллельном режиме...$(NC)"
	python scripts/run_tests.py --parallel 4

test-headed: ## Запустить тесты в видимом режиме
	@echo "$(GREEN)Запуск тестов в видимом режиме...$(NC)"
	python scripts/run_tests.py --headed

test-report: ## Запустить тесты с генерацией отчета
	@echo "$(GREEN)Запуск тестов с генерацией отчета...$(NC)"
	python scripts/run_tests.py --generate-report

test-serve: ## Запустить тесты и открыть отчет в браузере
	@echo "$(GREEN)Запуск тестов с открытием отчета...$(NC)"
	python scripts/run_tests.py --serve-report

clean: ## Очистить результаты тестов
	@echo "$(GREEN)Очистка результатов тестов...$(NC)"
	rm -rf allure-results/
	rm -rf allure-report/
	rm -rf test-results/
	rm -rf .pytest_cache/
	rm -rf __pycache__/
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

docker-build: ## Собрать Docker образ
	@echo "$(GREEN)Сборка Docker образа...$(NC)"
	docker build -t effective-mobile-tests .

docker-run: ## Запустить тесты в Docker контейнере
	@echo "$(GREEN)Запуск тестов в Docker...$(NC)"
	docker run --rm -v $(PWD)/allure-results:/app/allure-results effective-mobile-tests

docker-compose-up: ## Запустить тесты через docker-compose
	@echo "$(GREEN)Запуск тестов через docker-compose...$(NC)"
	docker-compose up --build

docker-compose-down: ## Остановить docker-compose
	@echo "$(GREEN)Остановка docker-compose...$(NC)"
	docker-compose down

check-env: ## Проверить окружение
	@echo "$(GREEN)Проверка окружения...$(NC)"
	@python --version
	@pip list | grep -E "(playwright|pytest|allure)"
	@playwright --version

lint: ## Проверить код линтером
	@echo "$(GREEN)Проверка кода...$(NC)"
	@python -m flake8 pages/ tests/ scripts/ --max-line-length=120 --ignore=E203,W503
	@python -m black --check pages/ tests/ scripts/

format: ## Форматировать код
	@echo "$(GREEN)Форматирование кода...$(NC)"
	@python -m black pages/ tests/ scripts/

# Комбинированные команды
full-test: clean test-report ## Полный цикл тестирования с очисткой и отчетом
	@echo "$(GREEN)Полный цикл тестирования завершен!$(NC)"

docker-full-test: docker-build docker-run ## Полный цикл тестирования в Docker
	@echo "$(GREEN)Полный цикл тестирования в Docker завершен!$(NC)"

# Информационные команды
info: ## Показать информацию о проекте
	@echo "$(GREEN)Информация о проекте:$(NC)"
	@echo "Проект: Тесты для effective-mobile.ru"
	@echo "Технологии: Python 3.10, Playwright, Allure, Docker"
	@echo "Структура: Page Object Pattern"
	@echo "Тесты: UI тесты навигации и функциональности"


