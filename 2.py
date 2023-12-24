def load_cook_book(path):
    with open(path, "rt", encoding="utf8") as f:
        split_items = get_split_items(f.read().splitlines())
        return get_cook_book_dict(split_items)


def get_split_items(lines):
    items = []
    temp_item = []
    for l in lines:
        if l == "":
            items.append(temp_item)
            temp_item = []
            continue
        temp_item.append(l)
    items.append(temp_item)
    return items


def get_cook_book_dict(split_items):
    result = {}
    for item in split_items:
        result[item[0]] = get_ingredients(item[2:])
    return result


def get_ingredients(ingredients_list):
    result = []
    for ingr in ingredients_list:
        i = ingr.split(" | ")
        d = {"ingredient_name": i[0], "quantity": int(i[1]), "measure": i[2]}
        result.append(d)
    return result


def get_shop_list_by_dishes(dishes, person_count):
    result = {}
    cook_book = load_cook_book("cook_book.txt")
    for dish in dishes:
        d = cook_book[dish]
        for i in d:
            if i["ingredient_name"] not in result:
                result[i["ingredient_name"]] = {
                    "measure": i["measure"],
                    "quantity": i["quantity"] * person_count,
                }
            else:
                result[i["ingredient_name"]]["quantity"] += i["quantity"] * person_count
    return result


print(get_shop_list_by_dishes(["Запеченный картофель", "Омлет"], 2))
