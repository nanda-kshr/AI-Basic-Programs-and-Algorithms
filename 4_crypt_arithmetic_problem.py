def is_valid(mapping, words, result):
    # Convert words to numbers based on the mapping
    def word_to_num(word):
        num = 0
        for char in word:
            num = num * 10 + mapping[char]
        return num
    
    # Check if the first character maps to 0
    for word in words + [result]:
        if mapping[word[0]] == 0:
            return False
    
    # Check if the arithmetic works
    word_sum = sum(word_to_num(word) for word in words)
    return word_to_num(result) == word_sum

def solve_cryptarithmetic(words, result):
    # Get all unique letters
    unique_chars = set(''.join(words) + result)
    
    # Check if we have more than 10 unique characters
    if len(unique_chars) > 10:
        return None
    
    # Initialize the mapping
    mapping = {}
    
    def backtrack(chars, used_digits):
        if not chars:
            if is_valid(mapping, words, result):
                return mapping.copy()
            return None
        
        char = chars[0]
        for digit in range(10):
            if digit not in used_digits:
                mapping[char] = digit
                solution = backtrack(chars[1:], used_digits | {digit})
                if solution:
                    return solution
                mapping[char] = None
        
        return None
    
    return backtrack(list(unique_chars), set())

words = ["SEND", "MORE"]
result = "MONEY"

solution = solve_cryptarithmetic(words, result)

if solution:
    print("Solution found:")
    for char, digit in sorted(solution.items()):
        print(f"{char} = {digit}")
    
    # Verify the solution
    for word in words:
        num = 0
        for char in word:
            num = num * 10 + solution[char]
        print(f"{word} = {num}")
    
    result_num = 0
    for char in result:
        result_num = result_num * 10 + solution[char]
    print(f"{result} = {result_num}")
else:
    print("No solution found.")