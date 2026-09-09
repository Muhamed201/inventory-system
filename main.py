"""
Система инвентаризации: начальный сценарий проверки результата
инвентаризации одного объекта.

Сущности:
- Объект — материальная ценность, подлежащая учёту (наименование, учётное количество).
- Инвентаризация — мероприятие проверки фактического наличия объектов на дату.
- Сотрудник — материально ответственное лицо, проводящее инвентаризацию.
- Результат — итог сравнения учётного и фактического количества объекта.
"""

from datetime import date

# --- Объект инвентаризации ---
object_name = "Ноутбук Lenovo ThinkPad"
expected_quantity = 15           # учётное количество (по документам)
actual_quantity_input = "12"     # фактическое количество, введённое сотрудником (строка)

# --- Сотрудник ---
employee_name = "Иванов И.И."

# --- Инвентаризация ---
inventory_date = date(2026, 9, 9)
CRITICAL_THRESHOLD = 3           # порог, после которого расхождение считается критическим


def get_discrepancy(expected, actual):
    """Возвращает расхождение между учётным и фактическим количеством."""
    return actual - expected


def classify_result(discrepancy):
    """Определяет тип результата инвентаризации по величине расхождения."""
    if discrepancy == 0:
        return "Соответствует учёту"
    elif discrepancy > 0:
        return "Излишек"
    else:
        return "Недостача"


def is_critical(discrepancy, threshold):
    """Проверяет, является ли расхождение критическим (по модулю превышает порог)."""
    return abs(discrepancy) > threshold


def build_report(name, employee, inv_date, expected, actual):
    """Формирует текстовый отчёт по результату инвентаризации объекта."""
    discrepancy = get_discrepancy(expected, actual)
    result = classify_result(discrepancy)
    critical_note = " (КРИТИЧНО)" if is_critical(discrepancy, CRITICAL_THRESHOLD) else ""

    report = (
        f"Инвентаризация от {inv_date}\n"
        f"Объект: {name}\n"
        f"Ответственный сотрудник: {employee}\n"
        f"Учётное количество: {expected}\n"
        f"Фактическое количество: {actual}\n"
        f"Расхождение: {discrepancy}\n"
        f"Результат: {result}{critical_note}"
    )
    return report


def main():
    # преобразование типа: фактическое количество получено как строка, приводим к int
    actual_quantity = int(actual_quantity_input)

    print(build_report(object_name, employee_name, inventory_date, expected_quantity, actual_quantity))


if __name__ == "__main__":
    main()
