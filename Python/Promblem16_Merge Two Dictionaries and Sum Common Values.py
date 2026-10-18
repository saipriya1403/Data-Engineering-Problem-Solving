# Databricks notebook source
system1 = {
    "Arun": 5000,
    "Priya": 3000,
    "Kumar": 4000
                }

system2 = {
    "Arun": 2000,
    "Priya": 4500,
    "Divya": 6000
}

merged = system1.copy()

for customer, amount in system2.items():
    merged[customer] = merged.get(customer, 0) + amount

print(merged)
