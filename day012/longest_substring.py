# Longest substring without repeating characters
def longest_substring(word):
    left, max_length = 0, 0
    char_set = set()
    for right in range(len(word)):
        while word[right] in char_set:
            char_set.remove(word[left])
            left += 1

        char_set.add(word[right])
        current_length = right - left + 1
        max_length = max(max_length, current_length)
    return max_length

print(longest_substring("abcabcbb"))  # returns 3 ("abc")
print(longest_substring("bbbbb"))     # returns 1 ("b")