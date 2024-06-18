nums = [10, 20, 30, 40, 50]
nums_double = []

for n in nums:
    nums_double.append(n * 2)

print(nums_double)  # [20, 40, 60, 80, 100]


# List comprehension
nums = [10, 20, 30, 40, 50]
nums_double = []

#[expression for loop if condition]

nums_double = [n * 2 for n in nums]

print(nums_double) 


nums = [10, 20, 30, 40, 50]
nums_double = []

nums_double = [n * 2 for n in nums if n % 4 == 0]

print(nums_double)  



list1 = [30, 50, 110, 40, 15, 75]
list2 = [10, 60, 20, 50]

sum_list = [ (n1, n2) for n1 in list1 for n2 in list2 if n1 + n2 > 100]

print(sum_list)