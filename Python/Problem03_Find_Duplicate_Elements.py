# Databricks notebook source
numbers = [10, 20, 10, 30, 40, 20, 50, 30, 60]

frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

duplicates = []

for num, count in frequency.items():
    if count > 1:
      duplicates.append(num)

print(duplicates)