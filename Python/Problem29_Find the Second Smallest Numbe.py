# Databricks notebook source
numbers = [25, 10, 5, 20, 5, 15]

unique_numbers = list(set(numbers))
unique_numbers.sort()

print("Second smallest number:", unique_numbers[1])