str1 = "python"
str2 = "pyspark"

common = []

for char in str1:
    if char in str2 and char not in common:
        common.append(char)

print("Common characters:", common)
