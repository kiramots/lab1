# Лабораторна робота №1. Основи Python
# Варіант: _5_
# ПІБ: _Моцненко Кіра Юріївна_


# Розрахунок вартості фарбування стін кімнати

try:
    # Введення користувачем розмірів кімнати, витрат фарби та вартості 1 банки фарби
    length = float(input("Введіть довжину кімнати (м): "))
    width = float(input("Введіть ширину кімнати (м): "))
    height = float(input("Введіть висоту кімнати (м): "))
    paint_rate = float(input("Введіть витрати фарби на 1 м² (л): "))
    can_price = float(input("Введіть вартість однієї банки фарби: "))

    # Перевірка введення даних
    if length <= 0 or width <= 0 or height <= 0:
        print("Таких розмірів кімнати не може бути.")
    elif paint_rate <= 0 or can_price <= 0:
        print("Витрати фарби та вартість банки повинні бути більшими за нуль.")
    else:
        # Обчислення площі 4 стін та необхідної кількості фарби
        wall_area = 2 * (length + width) * height
        paint_needed = wall_area * paint_rate

        # Вважаємо, що 1 банка = 1 літр фарби
        cans_needed = int(paint_needed)
        if paint_needed > cans_needed:
            cans_needed += 1

        # Обчислюємо загальну вартість фарби
        total_cost = cans_needed * can_price

        # Виводимо результати
        print("\nРезультати:")
        print(f"Площа всіх стін: {wall_area:.2f} м²")
        print(f"Потрібно фарби: {paint_needed:.2f} л")
        print(f"Потрібно банок фарби: {cans_needed}")
        print(f"Загальна вартість: {total_cost:.2f}")

except ValueError:
    print("Виникла помилка, введіть правильне числове значення.")
