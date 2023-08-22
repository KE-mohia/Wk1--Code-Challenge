# Wk1--Code-Challenge

This repository contains Python solutions to three coding challenges. Each challenge focuses on a different problem and its solution.

## Challenge 1: Converting 12-hour time to 24-hour time

### Problem Statement

Given a 12-hour time in the format "hour:minute period" (e.g., "8:30 am" or "8:30 pm"), the task is to convert it into a 24-hour time format.

### Solution

The solution defines a function `convert_to_24_hour` that takes an hour (1-12), minute (0-59), and period ("am" or "pm") as input. It converts the time to 24-hour format and returns it as a four-digit string.

## Challenge 2: Two numbers are positive

### Problem Statement

Given three integers `a`, `b`, and `c`, the task is to determine if exactly two of them are positive.

### Solution

The solution defines a function `exactly_two_positive` that takes three integers as input. It counts the number of positive integers and returns `True` if the count is exactly 2, otherwise `False`.

## Challenge 3: Consonant value

### Problem Statement

Given a lowercase string containing only alphabetic characters, the task is to find the highest value of consonant substrings. Consonants are any letters of the alphabet except "aeiou", and their values are assigned (a=1, b=2, c=3, ..., z=26).

### Solution

The solution defines a function `solve` that takes a string as input. It iterates through the string, calculating the value of consonant substrings and finding the maximum value among them.

---

## How to Use

1. Clone this repository to your local machine.
2. Navigate to the repository directory.

### Challenge 1

1. Open a Python interpreter or your preferred IDE.
2. Import the `convert_to_24_hour` function from the `challenge_solutions` module.
3. Call the function with appropriate inputs to test the conversion of 12-hour time to 24-hour time.

### Challenge 2

1. Import the `exactly_two_positive` function from the `challenge_solutions` module.
2. Call the function with three integers as inputs to determine if exactly two of them are positive.

### Challenge 3

1. Import the `solve` function from the `challenge_solutions` module.
2. Call the function with a lowercase string as input to find the highest value of consonant substrings.





