def solve(word):
    def value_of_consonant(c):
        return ord(c) - ord('a') + 1
    
    consonant_substrings = []
    current_substring = 0
    
    for char in word:
        if char not in "aeiou":
            current_substring += value_of_consonant(char)
        else:
            consonant_substrings.append(current_substring)
            current_substring = 0
    
    consonant_substrings.append(current_substring)
    
    return max(consonant_substrings)

# Test cases
print(solve("zodiacs"))   # Output: 26
print(solve("strength"))  # Output: 57
