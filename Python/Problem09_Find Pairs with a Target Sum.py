# Databricks notebook source
numbers = [2, 4, 3, 5, 7, 8, 1, 6]
target = 9

seen = set()
pairs = []

for num in numbers:
    difference = target - num

    if difference in seen:
        pair = tuple(sorted((num, difference)))

        if pair not in pairs:
           pairs.append(pair)

    seen.add(num)

print(pairs)