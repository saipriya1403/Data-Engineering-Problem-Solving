# Databricks notebook source
numbers = [10, 15, 20, 25, 30, 35, 40]

even = []
odd = []

for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print("Even Numbers:", even)
print("Odd Numbers:", odd)