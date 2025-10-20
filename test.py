def task1():
    """Сумма и среднее для смешанных значений"""
    n = int(input().strip())
    tokens = input().split()
    
    total = 0
    for token in tokens:
        if token == 'True':
            total += 1
        elif token == 'False':
            total += 0
        else:
            total += float(token)
    
    average = total / n
    print(f"{total} {average:.6f}")

def format_name(last, first, middle=None):
    """Форматирование ФИО"""
    if middle:
        return f"{last} {first[0]}.{middle[0]}."
    else:
        return f"{last} {first}"

def task2():
    """Форматирование ФИО"""
    m = int(input().strip())
    for _ in range(m):
        parts = input().split()
        if len(parts) == 2:
            last, first = parts
            print(format_name(last, first))
        elif len(parts) == 3:
            last, first, middle = parts
            print(format_name(last, first, middle))

def task3():
    """Разворот подстроки по срезу"""
    s = input().strip()
    i, j = map(int, input().split())
    
    # Обрабатываем границы
    i = max(0, min(i, len(s)))
    j = max(i, min(j, len(s)))
    
    # Разворачиваем подстроку и собираем строку
    result = s[:i] + s[i:j][::-1] + s[j:]
    print(result)

def task4():
    """Объединение списков без дубликатов"""
    n = int(input().strip())
    list1 = list(map(int, input().split()))
    m = int(input().strip())
    list2 = list(map(int, input().split()))
    
    seen = set()
    result = []
    
    # Добавляем элементы из первого списка
    for num in list1:
        if num not in seen:
            result.append(num)
            seen.add(num)
    
    # Добавляем элементы из второго списка
    for num in list2:
        if num not in seen:
            result.append(num)
            seen.add(num)
    
    # Выводим результат
    print(' '.join(map(str, result)))

def task5():
    """Длина неубывающего фрагмента"""
    n = int(input().strip())
    if n == 0:
        print(0)
        return
    
    numbers = list(map(int, input().split()))
    
    max_length = 1
    current_length = 1
    
    for i in range(1, n):
        if numbers[i] >= numbers[i-1]:
            current_length += 1
            max_length = max(max_length, current_length)
        else:
            current_length = 1
    
    print(max_length)

def main():
    """Основная функция для выбора задачи"""
    print("Выберите задачу (1-5):")
    print("1 - Сумма и среднее для смешанных значений")
    print("2 - Форматирование ФИО")
    print("3 - Разворот подстроки по срезу")
    print("4 - Объединение списков без дубликатов")
    print("5 - Длина неубывающего фрагмента")
    
    choice = input().strip()
    
    if choice == '1':
        print("Введите количество элементов, затем строку с значениями:")
        task1()
    elif choice == '2':
        print("Введите количество строк, затем ФИО (Фамилия Имя или Фамилия Имя Отчество):")
        task2()
    elif choice == '3':
        print("Введите строку, затем два числа - границы среза:")
        task3()
    elif choice == '4':
        print("Введите размер первого списка, затем элементы, затем размер второго списка, затем элементы:")
        task4()
    elif choice == '5':
        print("Введите количество элементов, затем список чисел:")
        task5()
    else:
        print("Неверный выбор")

if __name__ == "__main__":
    main()
# на 2 строке добавить привет