# Task 1
# Объединить списки покупок и посчитать общее количество товаров и сумму.
# Формат входных данных -- словарь, где ключи -- это продукты,
# а значения -- список [кол-во, цена].
# Формат выходных данных -- такой же.

Max = {
    "пиво": [3, 80],
    "чипсы": [1, 90],
    "орешки": [1, 65],
    "рыбка": [5, 25],
}

Den = {
    "сухарики": [2, 25],
    "пиво": [4, 65],
    "орешки": [2, 65],
    "кубики": [2, 150],
    "спички": [1, 10],
}

Ira = {
    "чипсы": [1, 110],
    "фисташки": [1, 215],
    "пиво": [2, 90],
}


def union(*shopping_lists):
    """
    Получить объединенный список покупок в формате описанном выше.
    """
    total_shopping_list = dict()
    for shopping_list in shopping_lists:
        for product_name, val in shopping_list.items():
            quantity, price = val
            product_numbers = total_shopping_list.get(product_name, [0, 0])
            product_numbers[0] += quantity
            product_numbers[1] += quantity * price
            total_shopping_list[product_name] = product_numbers

    return total_shopping_list


if __name__ == "__main__":
    total_list = union(Max, Den, Ira)
    for k, v in total_list.items():
        print("{0:10}".format(k), end=" ")
        print("{0:4} шт.".format(v[0]), end=" ")
        print("{0:5} руб.".format(v[1]))

    total_goods = 0
    total_bill = 0
    for k, v in total_list.items():
        total_goods += v[0]
        total_bill += v[1]
    print("___________________________________")
    print(f"всего {total_goods} товаров на сумму {total_bill} руб.")

    # Простейшее тестирование результатов, надо будет подчеркивать на занятиях
    assert total_goods == 25, "ошибка в кол-ве товаров"
    assert total_bill == 1775, "ошибка в общей сумме"
