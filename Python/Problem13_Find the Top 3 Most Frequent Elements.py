# Databricks notebook source
numbers = [10, 20, 10, 30, 20, 10, 40, 20, 30, 30, 30, 50]

frequency = {}

for num in numbers:
    frequency[num] = frequency.get(num, 0) + 1

sorted_numbers = sorted(
        frequency.items(),
            key=lambda x: (-x[1], x[0])
            )

top_3 = sorted_numbers[:3]

print(top_3)