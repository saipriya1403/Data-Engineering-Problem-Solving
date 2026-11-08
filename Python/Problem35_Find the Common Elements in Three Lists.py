list1 = [10, 20, 30, 40, 50]
list2 = [20, 30, 50, 60]
list3 = [10, 20, 30, 70]

common = []

for num in list1:
    if num in list2 and num in list3:
        common.append(num)

print("Common elements:", common)
