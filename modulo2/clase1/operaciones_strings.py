print('a' < 'b')  # 'a' has a smaller Unicode value


house = "Gryffindor"
house_copy = "Gryffindor"

print(house == house_copy)  # True

new_house = "Slytherin"

print(house == new_house)  # False

print(new_house <= house)  # False


print(new_house >= house)  # False