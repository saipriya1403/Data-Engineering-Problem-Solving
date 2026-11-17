numbers = [10, 20, 10, 30, 40, 20, 50]

result = []

for num in numbers:
    if numbers.count(num) == 1:
        result.append(num)

print(result)
