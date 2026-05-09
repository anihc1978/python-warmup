"""
01_list_comprehensions.py
IBM Python Warm-up — List & Dict Comprehensions
"""
from typing import List, Dict


# 1. Basic list comprehension: squares of even numbers 0-19
squares: List[int] = [x**2 for x in range(20) if x % 2 == 0]
print("Even squares:", squares)

# 2. Nested comprehension: 3x3 multiplication table
table: List[List[int]] = [[row * col for col in range(1, 4)] for row in range(1, 4)]
print("3x3 table:", table)

# 3. Flatten a 2-D list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat: List[int] = [val for row in matrix for val in row]
print("Flat:", flat)

# 4. Dict comprehension: word to length
words = ["apple", "banana", "cherry", "date", "elderberry"]
word_len: Dict[str, int] = {w: len(w) for w in words}
print("Word lengths:", word_len)

# 5. Set comprehension: unique first letters
first_letters = {w[0] for w in words}
print("First letters:", first_letters)

# 6. Generator expression in sum
total_chars = sum(len(w) for w in words)
print("Total characters:", total_chars)

# 7. Conditional dict comprehension: only long words
long_words: Dict[str, int] = {w: len(w) for w in words if len(w) > 5}
print("Long words:", long_words)

# 8. Comprehension with enumerate
indexed = {i: w.upper() for i, w in enumerate(words)}
print("Indexed uppercased:", indexed)

if __name__ == "__main__":
    print("List comprehensions demo complete.")
