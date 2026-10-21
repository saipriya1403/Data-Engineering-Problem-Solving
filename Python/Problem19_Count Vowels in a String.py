# Databricks notebook source
text = "dataengineering"

vowels = "aeiou"
count = 0

for char in text:
    if char in vowels:
        count += 1

print("Total vowels:", count)