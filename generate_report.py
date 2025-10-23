#!/usr/bin/env python3
"""
Простой генератор HTML отчета для результатов тестов
"""
import json
import os
from datetime import datetime
from pathlib import Path

def load_test_results():
    """Загружает результаты тестов из allure-results"""
    results = []
    results_dir = Path("allure-results")
    
    if not results_dir.exists():
        print("Папка allure-results не найдена")
        return results
    
    for file_path in results_dir.glob("*-result.json"):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                results.append(data)
        except Exception as e:
            print(f"Ошибка при чтении {file_path}: {e}")
    
    return results

def generate_html_report(results):
    """Генерирует HTML отчет"""
    total_tests = len(results)
    passed = sum(1 for r in results if r.get('status') == 'passed')
    failed = sum(1 for r in results if r.get('status') == 'failed')
    skipped = sum(1 for r in results if r.get('status') == 'skipped')
    
    html_content = f"""
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Отчет о тестировании</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 20px;
            background-color: #f5f5f5;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}
        .header {{
            text-align: center;
            margin-bottom: 30px;
            padding-bottom: 20px;
            border-bottom: 2px solid #eee;
        }}
        .stats {{
            display: flex;
            justify-content: space-around;
            margin-bottom: 30px;
        }}
        .stat {{
            text-align: center;
            padding: 20px;
            border-radius: 8px;
            color: white;
            min-width: 150px;
        }}
        .stat.passed {{ background-color: #28a745; }}
        .stat.failed {{ background-color: #dc3545; }}
        .stat.skipped {{ background-color: #ffc107; color: #333; }}
        .stat.total {{ background-color: #007bff; }}
        .test-item {{
            margin-bottom: 15px;
            padding: 15px;
            border-radius: 5px;
            border-left: 4px solid;
        }}
        .test-item.passed {{ border-left-color: #28a745; background-color: #d4edda; }}
        .test-item.failed {{ border-left-color: #dc3545; background-color: #f8d7da; }}
        .test-item.skipped {{ border-left-color: #ffc107; background-color: #fff3cd; }}
        .test-name {{
            font-weight: bold;
            margin-bottom: 5px;
        }}
        .test-details {{
            font-size: 0.9em;
            color: #666;
        }}
        .timestamp {{
            text-align: center;
            color: #666;
            margin-top: 30px;
            font-size: 0.9em;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Отчет о тестировании</h1>
            <p>effective-mobile.ru</p>
        </div>
        
        <div class="stats">
            <div class="stat total">
                <h3>{total_tests}</h3>
                <p>Всего тестов</p>
            </div>
            <div class="stat passed">
                <h3>{passed}</h3>
                <p>Пройдено</p>
            </div>
            <div class="stat failed">
                <h3>{failed}</h3>
                <p>Провалено</p>
            </div>
            <div class="stat skipped">
                <h3>{skipped}</h3>
                <p>Пропущено</p>
            </div>
        </div>
        
        <h2>Детали тестов</h2>
        <div class="tests">
"""
    
    for result in results:
        status = result.get('status', 'unknown')
        name = result.get('name', 'Неизвестный тест')
        full_name = result.get('fullName', name)
        duration = result.get('time', {}).get('duration', 0) / 1000  # в секундах
        
        # Извлекаем информацию о шагах
        steps = []
        if 'steps' in result:
            for step in result['steps']:
                if 'name' in step:
                    steps.append(step['name'])
        
        html_content += f"""
            <div class="test-item {status}">
                <div class="test-name">{name}</div>
                <div class="test-details">
                    <strong>Статус:</strong> {status.upper()}<br>
                    <strong>Время выполнения:</strong> {duration:.2f}с<br>
                    <strong>Полное имя:</strong> {full_name}
        """
        
        if steps:
            html_content += f"<br><strong>Шаги:</strong><ul>"
            for step in steps[:5]:  # Показываем только первые 5 шагов
                html_content += f"<li>{step}</li>"
            if len(steps) > 5:
                html_content += f"<li>... и еще {len(steps) - 5} шагов</li>"
            html_content += "</ul>"
        
        html_content += """
                </div>
            </div>
        """
    
    html_content += f"""
        </div>
        
        <div class="timestamp">
            Отчет сгенерирован: {datetime.now().strftime('%d.%m.%Y %H:%M:%S')}
        </div>
    </div>
</body>
</html>
"""
    
    return html_content

def main():
    """Основная функция"""
    print("Загрузка результатов тестов...")
    results = load_test_results()
    
    if not results:
        print("Результаты тестов не найдены")
        return
    
    print(f"Найдено {len(results)} результатов тестов")
    
    print("Генерация HTML отчета...")
    html_content = generate_html_report(results)
    
    # Сохраняем отчет
    report_path = "test-report.html"
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"Отчет сохранен в файл: {report_path}")
    print("Откройте файл в браузере для просмотра отчета")

if __name__ == "__main__":
    main()
