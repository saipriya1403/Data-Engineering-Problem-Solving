numbers = [1, 2, 2, 3, 3, 3, 4, 4]

frequency = {}

for num in numbers:
    frequency[num] = frequency.get(num, 0) + 1

sorted_frequency = sorted(
    frequency.items(),
    key=lambda x: x[1],
    reverse=True
)

print(sorted_frequency[1][0])
