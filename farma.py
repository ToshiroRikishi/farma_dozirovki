import pandas as pd

# Функция для чтения данных из Excel-файла и создания DataFrame для каждого листа
def read_excel_file(file_path):
    xls = pd.ExcelFile(file_path)
    data = {sheet: xls.parse(sheet) for sheet in xls.sheet_names}
    return data

# Функция для обработки данных из листа "Задание 1"
def process_task1(data):
    task1 = data["Задание 1 \"Модель\""]
    # Пример обработки данных
    # task1_processed = ... (здесь можно добавить конкретные шаги обработки)
    return task1

# Функция для обработки данных из листа "Задание 2 (Нагрузочная доза)"
def process_task2_loading(data):
    task2_loading = data["Задание 2 \"Нагрузочная доза\""]
    # Пример обработки данных
    # task2_loading_processed = ... (здесь можно добавить конкретные шаги обработки)
    return task2_loading

# Функция для обработки данных из листа "Задание 2 (Поддерживающая доза)"
def process_task2_maintenance(data):
    task2_maintenance = data["\"Задание 2\"Поддерживающая доза"]
    # Пример обработки данных
    # task2_maintenance_processed = ... (здесь можно добавить конкретные шаги обработки)
    return task2_maintenance

# Основная функция для выполнения проекта
def main():
    file_path = 'path_to_your_file.xlsx'
    data = read_excel_file(file_path)
    
    task1_processed = process_task1(data)
    task2_loading_processed = process_task2_loading(data)
    task2_maintenance_processed = process_task2_maintenance(data)
    
    # Сохранение обработанных данных в новые файлы
    task1_processed.to_csv('task1_processed.csv', index=False)
    task2_loading_processed.to_csv('task2_loading_processed.csv', index=False)
    task2_maintenance_processed.to_csv('task2_maintenance_processed.csv', index=False)

if __name__ == "__main__":
    main()

