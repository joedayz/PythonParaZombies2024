num_list = []  # Empty list

num_list.append(1)
num_list.append(2)
num_list.append(3)

print(num_list)  # [1, 2, 3]


num_list = [1, 2, 3, 5, 6]
num_list.insert(3, 4)
print(num_list)  # [1, 2, 3, 4, 5, 6]

#eliminar elementos
houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
last_house = houses.pop()
print(last_house)  # Slytherin
print(houses)  # ['Gryffindor', 'Hufflepuff', 'Ravenclaw']


houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
print(houses)
houses.remove("Ravenclaw") # Error si el elemento no existe
print(houses)

populations = [["Winterfell", 10000], ["King's Landing", 50000],
               ["Iron Islands", 5000]]

print(populations)
populations.remove(["Iron Islands", 5000])
print(populations)

#slicing

num_list = [1, 2, 3, 4, 5, 6, 7, 8]
print(num_list[2:5])  # [3, 4, 5]
print(num_list[0::2])

#index search
cities = ["London", "Paris", "Los Angeles", "Beirut"]

print(cities.index("Los Angeles"))  # 2

print("London" in cities)
print("Ventanilla" not in cities)

num_list = [20, 40, 10, 50.4, 30, 100, 5]
num_list.sort()
print(num_list)  # [5, 10, 20, 30, 40, 50.4, 100]