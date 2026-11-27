numbers = [0, 5, 0, 3, 8, 0, 2]

non_zeros = []
zeros = []

for num in numbers:
    if num == 0:
        zeros.append(num)
    else:
        non_zeros.append(num)

result = non_zeros + zeros

print("Result:", result)
