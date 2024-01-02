import math

history = []

def add_history(num1, num2, operator, result):
    history.append((num1, num2, operator, result))

def clear_history():
    global history
    history = []

def calculate(num1, num2, operator):
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            raise ZeroDivisionError("Невозможно делать на ноль")
        result = num1 / num2
    else:
        raise ValueError("Невозможный оператор")
    add_history(num1, num2, operator, result)
    return result

def print_history():
    if not history:
        print("Пустая история")
    else:
        print("История:")
        for i, (num1, num2, operator, result) in enumerate(history):
            print(f"{i+1}. {num1} {operator} {num2} = {result}")

while True:
    try:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        operator = input("Введите оператор (+, -, *, /): ")
        result = calculate(num1, num2, operator)
        print(f"Результат: {result}")
    except (ValueError, ZeroDivisionError) as e:
        print(f"Error: {e}")
    choice = input("Хотите произвести еще одну операцию? (y/n): ")
    if choice.lower() != "y":
        break

print_history()
choice = input("Хотите очистить историю? (y/n): ")
if choice.lower() == "y":
    clear_history()
    print("История очищена")
