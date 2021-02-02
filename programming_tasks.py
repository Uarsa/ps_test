# 1) Объединить списки покупок и посчитать общие колличество товаров и сумму.

Max = {
    "пиво": [3, 80],
    "чипсы": [1, 90],
    "орешки": [1, 65],
    "рыбка": [5, 25],
}

Den = {
    "сухарики": [2, 25],
    "пиво": [4, 65],
    "кубики": [2, 150],
    "орешки": [2, 65],
}

Ira = {
    "чипсы": [1, 110],
    "бокалы": [3, 200],
    "салфетки": [1, 30],
    "пиво": [3, 90],
}


def to_buy(*shopping_lists):
    common_shopping_list = dict()
    for l in shopping_lists:
        for goods, val in l.items():
            if goods in common_shopping_list:
                common_shopping_list[goods][0] += val[0]
                common_shopping_list[goods][1] += val[0] * val[1]
            else:
                common_shopping_list[goods] = val
            # чувстсвуется, что тут можно как-то изящно через dict.get() сделать, но
            # у меня пока не вышло. что-то как-то близко, но не то:
            # common_shopping_list[goods] = common_shopping_list.get(goods, val) + [val[0], val[1]]

    total_goods = 0
    total_bill = 0
    for goods, val in common_shopping_list.items():
        total_goods += val[0]
        total_bill += val[1]

    total_list = []
    for goods, val in common_shopping_list.items():
        total_list.append([val[0], goods, val[1]])

    for i in sorted(total_list, reverse=True):
        print("{0:12}".format(i[1]), "{0:6} шт.".format(i[0]), "{0:9} руб.".format(i[2]))
    print("______________________________________")
    print(f"ВСЕГО {total_goods} ТОВАРА(ОВ) НА СУММУ {total_bill} руб.")


to_buy(Max, Den, Ira)


