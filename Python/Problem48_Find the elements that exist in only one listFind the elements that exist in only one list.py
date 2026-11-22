list1 = [10, 20, 30, 40]
list2 = [30, 40, 50, 60]

result = []

for num in list1:
    if num not in list2:
        result.append(num)

for num in list2:
    if num not in list1:
        result.append(num)

print(result)
