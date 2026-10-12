# Databricks notebook source
transactions = [
    ("Arun", 1000),
    ("Priya", 2000),
    ("Arun", 1500),
    ("Kumar", 3000),
    ("Priya", 2500),
    ("Arun", 500)
                           
]

# COMMAND ----------

customer_transactions = {}

for customer, amount in transactions:
    if customer not in customer_transactions:
            customer_transactions[customer] = []

    customer_transactions[customer].append(amount)

print(customer_transactions)