from random import choice

items = []

def show_items(): #1. Vi tri, 2. ten item
    # 1. Rau muống luộc cao cấp
    # 2. Bánh bao chiên bình dân
    pass


def item_after_combat():
    new_item = generate_item()
    print("Một", new_item["NAME"], "vừa rơi ra")
    while True:
        print("1. Xem")
        print("2. Nhặt")
        print("3. Bỏ qua")
        option = input(">>>")
        if option == "1":
            show_item(new_item)
        elif option == "2":
            add_item(new_item)
            print("Bạn đã nhặt", new_item["NAME"], "vào hòm đồ")
            count_items()
            break
        elif option == "3":
            print("Bạn đã bỏ qua món đồ")
            break

def add_item(item):
    items.append(item)


def count_items():
    count = len(items) # len ~ length
    print("Bạn có", count, "đồ trong hòm")


food_types = [
    "Bánh bao",
    "Cơm",
    "Mỳ tôm",
    "Trứng",
    "Rau muống",
]

cook_types = [
    "hấp",
    "chiên",
    "luộc"
]

food_levels = [
    "bình dân",
    "cao cấp",
    "xa xỉ"
]


def generate_item_name():
    ft = choice(food_types)
    ct = choice(cook_types)
    fl = choice(food_levels)
    item_name = ft + " " + ct + " " + fl
    return item_name


def generate_item():
    name = generate_item_name()
    item = {
        "NAME": name,
        "AGI": 3,
        "HP": -1,
        "DEF": 2,
        "STR": 2,
    }
    return item


def show_item(game_item):
    print("* " * 15)

    for key, value in game_item.items():
        print("*", key, ":", value)

    print("* " * 15)

#
#
# steel_gauntlet = {
#     "NAME": "STEEL GAUNLET",
#     "HP": 10,
#     "AGI": 5,
#     "LUCK": 1,
# }
#
# bronze_shield = {
#     "NAME": "BRONZE SHIElD",
#     "HP": 5,
#     "AGI": 1,
# }
#
# golden_stick = {
#     "NAME": "GOLDEN STICK",
#     "AGI": 15,
#     "HP": 20,
#     "STR": 100,
# }
#
# inventory = [steel_gaunlet, bronze_shield, golden_stick]
# for item in inventory:
#     show_item(item)