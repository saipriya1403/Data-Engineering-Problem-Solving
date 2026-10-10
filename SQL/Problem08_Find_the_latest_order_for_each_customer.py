# Databricks notebook source
# MAGIC %md
# MAGIC ## Find the latest order for each customer

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC CREATE OR REPLACE TEMP VIEW orders AS
# MAGIC SELECT * FROM VALUES
# MAGIC     (101, 1, '2026-10-01', 2000),
# MAGIC     (102, 1, '2026-10-05', 3500),
# MAGIC     (103, 2, '2026-10-02', 1500),
# MAGIC     (104, 2, '2026-10-07', 4000),
# MAGIC     (105, 3, '2026-10-03', 2500)
# MAGIC AS orders(OrderId, CustomerId, OrderDate, Amount);

# COMMAND ----------

# MAGIC %sql
# MAGIC select 
# MAGIC OrderId,CustomerId,Orderdate,amount 
# MAGIC from (
# MAGIC     select *, row_number()
# MAGIC     over(partition by CustomerID order by OrderDate desc ,OrderId desc) as rn from orders
# MAGIC )
# MAGIC where rn =1;