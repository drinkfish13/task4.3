def get_cook_book():
    cook_book = {
    'салат': [
        {'ingridient_name': 'сыр', 'quantity': 50, 'measure': 'гр'},
        {'ingridient_name': 'томаты', 'quantity': 20, 'measure': 'гр'},
        {'ingridient_name': 'огурцы', 'quantity': 20, 'measure': 'гр'},
        {'ingridient_name': 'маслины', 'quantity': 10, 'measure': 'гр'},
        {'ingridient_name': 'оливковое масло', 'quantity': 20, 'measure': 'мл'},
        {'ingridient_name': 'салат', 'quantity': 10, 'measure': 'гр'},
        {'ingridient_name': 'перец', 'quantity': 20, 'measure': 'гр'}
        ],
    'пицца': [
        {'ingridient_name': 'сыр', 'quantity': 20, 'measure': 'гр'},
        {'ingridient_name': 'колбаса', 'quantity': 30, 'measure': 'гр'},
        {'ingridient_name': 'бекон', 'quantity': 30, 'measure': 'гр'},
        {'ingridient_name': 'оливки', 'quantity': 10, 'measure': 'гр'},
        {'ingridient_name': 'томаты', 'quantity': 20, 'measure': 'гр'},
        {'ingridient_name': 'тесто', 'quantity': 100, 'measure': 'гр'},
        ],
    'лимонад': [
        {'ingridient_name': 'лимон', 'quantity': 1, 'measure': 'шт'},
        {'ingridient_name': 'вода', 'quantity': 200, 'measure': 'мл'},
        {'ingridient_name': 'сахар', 'quantity': 10, 'measure': 'гр'},
        {'ingridient_name': 'лайм', 'quantity': 20, 'measure': 'гр'},
        ]
    }
    return cook_book

def get_shop_list_by_dishes(dishes, person_count, dishes_dict):
    shop_list = {}
    cook_book = dishes_dict
    for dish in dishes:
        for ingridient in cook_book[dish]:
            new_shop_list_item = dict(ingridient)
            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingridient_name'] not in shop_list:
                shop_list[new_shop_list_item
                ['ingridient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
    return shop_list


def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print(f"{shop_list_item['ingridient_name']} {shop_list_item['quantity']} {shop_list_item['measure']}")


def user_input_person_count():
    return int(input('Введите количество человек: '))


def input_list_dishes():
    dishes = input('Введите блюда в расчете на одного человека (через пробел):').split(' ')
    return dishes


if __name__ == '__main__':
    print_shop_list(get_shop_list_by_dishes(input_list_dishes(), user_input_person_count(), get_cook_book()))


