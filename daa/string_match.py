def naive_search(pattern, text):
    m = len(pattern)
    n = len(text)
    matches = []
    if m == 0:
        return matches
    for i in range(n - m + 1):
        if text[i:i + m] == pattern:
            matches.append(i)       
    return matches

if __name__ == "__main__":
    user_text = input("Enter the main text: ")
    user_pattern = input("Enter the pattern to search for: ")
    
    result_indices = naive_search(user_pattern, user_text)
    
    if result_indices:
        print(f"\nPattern found at indices: {result_indices}")
        print(f"Total matches found: {len(result_indices)}")
    else:
        print("\nPattern not found in the text.")