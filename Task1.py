def find_second_minimum(nums):
    # Инициализация минимального и второго минимального значений
    min_val = float('inf')
    second_min = float('inf')

    for num in nums:
        if num < min_val:  # Найден новый минимум
            second_min = min_val  # Старый минимум становится вторым минимумом
            min_val = num  # Обновляем минимум
        elif min_val < num < second_min:  # Элемент больше минимума, но меньше второго минимума
            second_min = num  # Обновляем второй минимум
    
    # Если второй минимум не был найден, возвращаем None
    return second_min if second_min != float('inf') else None

# Пример использования
nums = [4, 2, 5, 1, 3, 1]
result = find_second_minimum(nums)
print(result)

nums = [7, 7, 7, 7]
result = find_second_minimum(nums)
print(result)  # Вывод: None

nums = [3, 1, 4, 1, 5, 9, 2]
result = find_second_minimum(nums)
print(result)  # Вывод: 2