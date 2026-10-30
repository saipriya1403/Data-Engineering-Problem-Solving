# Databricks notebook source
numbers = [20, 65, 40, 85, 30, 90, 45]

result = []

for num in numbers:
    if num > 50:
        result.append(num)

print("Numbers greater than 50:", result)