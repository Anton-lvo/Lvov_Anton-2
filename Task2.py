def binary_search(arr, target):
    # Инициализация границ и счетчика операций
    left, right = 0, len(arr) - 1
    operations = 0
    
    while left <= right:
        # Находим середину
        mid = (left + right) // 2
        operations += 1  # Увеличиваем счетчик операций
        
        # Сравниваем значение в середине с искомым
        if arr[mid] == target:
            return mid, operations  # Возвращаем индекс и количество операций
        elif arr[mid] < target:
            left = mid + 1  # Сдвигаем левую границу
        else:
            right = mid - 1  # Сдвигаем правую границу
    
    # Если значение не найдено
    return -1, operations

# Пример использования
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 13

index, operations = binary_search(arr, target)
print(f"Индекс элемента {target}: {index}")
print(f"Количество операций: {operations}")

arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
target = 5

index, operations = binary_search(arr, target)
print(f"Индекс элемента {target}: {index}")  # Вывод: Индекс элемента 5: -1
print(f"Количество операций: {operations}")  # Вывод: Количество операций: 4