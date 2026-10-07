# Databricks notebook source
list1 = [10, 20, 30, 40, 50, 20]
list2 = [20, 30, 60, 70, 20, 30]

common_elements = list(set(list1) & set(list2))

print(common_elements)