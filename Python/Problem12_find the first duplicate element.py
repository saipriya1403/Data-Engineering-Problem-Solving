# Databricks notebook source
numbers = [10, 20, 30, 20, 40, 10, 50]

seen = set()
first_duplicate = None

for num in numbers:
    if num in seen:
        first_duplicate = num
        break

    seen.add(num)

print("First duplicate:", first_duplicate)