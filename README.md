# Скрипт предназначен для генерации аналитических отчётов по CSV-файлам с информацией о продуктах.

## Структура проекта
/brand_rating_report
-data_processing.py
-reports.py
-main.py
-/tests
    -test_reports.py
-README.md

## Для запуска скрипта необходимо в терминале использовать название отчета "average-rating" командой
python main.py --files data/file1.csv data/file2.csv --report average-rating
Результатом будет как на скриншоте:

![01.png](../../Desktop/01.png)

## Для запуска тестов необходимо в терминале использовать команду pytest 
pytest

![02.png](../../Desktop/02.png)

## Чтобы добавить новый отчет, необходимо
1. реализовать новую функцию в reports.py, например:
_generate_price_summary_report(data: Iterator[dict]) -> ReportData
2. зарегистрировать отчёт в словаре REPORTS
3. добавить заголовки для вывода в словарь HEADERS