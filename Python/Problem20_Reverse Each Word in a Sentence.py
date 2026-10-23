# Databricks notebook source
text = "Python SQL Spark"

words = text.split()
result = []

for word in words:
    result.append(word[::-1])

    print(" ".join(result))