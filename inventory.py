
#
#
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