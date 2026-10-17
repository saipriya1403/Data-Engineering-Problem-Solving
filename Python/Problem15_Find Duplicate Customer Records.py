# Databricks notebook source
customers = [
    (101, "Arun", "Chennai"),
    (102, "Priya", "Bangalore"),
    (103, "Kumar", "Salem"),
    (101, "Arun", "Coimbatore"),
    (104, "Divya", "Trichy"),
    (102, "Priya", "Chennai")
]

frequency = {}

for customer_id, name, city in customers:
    frequency[customer_id] = frequency.get(customer_id, 0) + 1

    duplicates = []

    for customer_id, count in frequency.items():
        if count > 1:
            duplicates.append(customer_id)

print("Duplicate Customer IDs:", duplicates)
