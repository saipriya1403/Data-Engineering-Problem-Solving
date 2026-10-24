# Databricks notebook source
numbers = [10, 15, 20, 30, 45, 50, 60, 75]

result = []

for num in numbers:
    if num % 3 == 0 and num % 5 == 0:
        result.append(num)

print(result)