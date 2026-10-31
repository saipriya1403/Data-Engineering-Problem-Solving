# Databricks notebook source
numbers = [10, -5, 20, -8, 30, -2, 15]

result = []

for num in numbers:
    if num >= 0:
        result.append(num)

print("Numbers without negatives:", result)