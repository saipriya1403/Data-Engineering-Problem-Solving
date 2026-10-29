# Databricks notebook source
numbers = [10, 15, 20, 25, 30, 35]

total = 0

for num in numbers:
    if num % 2 == 0:
        total += num

print("Sum of even numbers:", total)