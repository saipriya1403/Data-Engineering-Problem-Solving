numbers = [12, 456, 78, 1234, 9]

result = max(numbers, key=lambda x: len(str(x)))

print(result)
