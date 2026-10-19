# Анализатор логов

Программа принимает файл server.log вида
```
2026-10-15 09:12:01 INFO 192.168.1.10 User login
```

И создает/изменяет файл analyze_reslult.json
```
{
    "levels": {
        "INFO": 3,
        "WARNING": 1,
        "ERROR": 3
    },
    "top_error_ip": "192.168.1.22",
    "errors_by_hour": {
        "09": 1,
        "10": 2
    },
    "broken_lines": 1
}
```
___
## Установка
В консоле выполните 
```
pip install -r requirements.txt
```
## Запуск программы

Запуститеп файл log_analyzer.py
```
python log_analyzer.py
```
## Запуск тестов

В консоле выполните 
```
pytest
```