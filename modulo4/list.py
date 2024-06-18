jon_snow = ["Jon Snow", "Winterfell", 30]

print(jon_snow[0])  # Jon Snow

print(len(jon_snow))  # 3

print(jon_snow[2]+ 3)


num_seq = range(0, 10)
num_list = list(num_seq)

print(num_list)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

num_seq = range(3, 20, 3)
print(list(num_seq))  # [3, 6, 9, 12, 15, 18]

world_cup_winners = [[2006, "Italy"], [2010, "Spain"],
                     [2014, "Germany"], [2018, "France"]]
print(world_cup_winners)  # [2006, 'Italy']
print(world_cup_winners[1])
print(world_cup_winners[1][1])
print(world_cup_winners[1][1][0])

#merge

part_A = [1, 2, 3, 4, 5]
part_B = [6, 7, 8, 9, 10]
merged_list = part_A + part_B
print(merged_list)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


part_A.extend(part_B)
print(part_A)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]