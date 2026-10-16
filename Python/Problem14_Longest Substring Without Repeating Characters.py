# Databricks notebook source
text = "abcabcbb"

seen = set()
left = 0
max_length = 0

for right in range(len(text)):

    while text[right] in seen:
            seen.remove(text[left])
            left += 1

    seen.add(text[right])

    max_length = max(
        max_length,
        right - left + 1
)

print("Longest substring length:", max_length)