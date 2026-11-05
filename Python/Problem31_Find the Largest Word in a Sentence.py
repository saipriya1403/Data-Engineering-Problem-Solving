sentence = "Python SQL PySpark Databricks"

words = sentence.split()

largest_word = ""

for word in words:
    if len(word) > len(largest_word):
        largest_word = word

print("Longest word:", largest_word)
