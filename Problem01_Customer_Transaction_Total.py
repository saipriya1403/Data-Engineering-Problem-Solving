# Databricks notebook source
transactions = [
    ("Arun", 1000),
    ("Priya", 2000),
    ("Arun", 1500),
    ("Kumar", 3000),
    ("Priya", 1000),
    ("Arun", 500)
]

totals = {}

for customer, amount in transactions:
    if customer in totals:
        totals[customer] += amount
    else:
        totals[customer] = amount

print(totals)


# COMMAND ----------

# MAGIC %md
# MAGIC Problem:
# MAGIC Find the total transaction amount for each customer.
# MAGIC
# MAGIC Approach:
# MAGIC 1. Create an empty dictionary.
# MAGIC 2. Use customer name as the dictionary key.
# MAGIC 3. Add transaction amounts for existing customers.
# MAGIC 4. Create a new entry for new customers.
# MAGIC
# MAGIC Output:
# MAGIC Arun  -> 3000
# MAGIC Priya -> 3000
# MAGIC Kumar -> 3000

# COMMAND ----------

# MAGIC %md
# MAGIC