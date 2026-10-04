# Databricks notebook source
# MAGIC %md
# MAGIC ### Latest Order for Each Customer

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC CREATE OR REPLACE TEMP VIEW orders AS
# MAGIC SELECT * FROM VALUES
# MAGIC     (1001, 1, '2026-09-01', 5000),
# MAGIC     (1002, 2, '2026-09-02', 3000),
# MAGIC     (1003, 1, '2026-09-05', 4000),
# MAGIC     (1004, 3, '2026-09-03', 7000),
# MAGIC     (1005, 2, '2026-09-06', 2000),
# MAGIC     (1006, 1, '2026-09-08', 6000)
# MAGIC AS orders(OrderId, CustomerId, OrderDate, Amount);

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC SELECT
# MAGIC     OrderId,
# MAGIC     CustomerId,
# MAGIC     OrderDate,
# MAGIC     Amount
# MAGIC FROM (
# MAGIC     SELECT *,
# MAGIC     ROW_NUMBER() OVER (
# MAGIC     PARTITION BY CustomerId                              
# MAGIC     ORDER BY OrderDate DESC                                            
# MAGIC     )AS row_num 
# MAGIC     From Orders
# MAGIC ) where row_num =1                                                     
# MAGIC                                                                
# MAGIC                                                                      
# MAGIC                                                                         
# MAGIC                                                                        