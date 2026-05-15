import string

def word_frequency_count(word):
    word_count = {}
    for w in word:
        if w in word_count:
            word_count[w] += 1
        else:
            word_count[w] = 1
    word_count = dict(sorted(word_count.items(), key=lambda item: item[1], reverse=True))
    return word_count

def longest_and_average_length(word):
    total_length = 0
    max_word = word[0]
    for w in word:
        total_length += len(w)
        if len(w) > len(max_word):
            max_word = w
    average_length = total_length / len(word)
    return max_word, average_length

def palindrome(word):
    palindromes = []
    for w in word:
        if len(w) > 1 and w == w[::-1]:
            palindromes.append(w)
    return palindromes
            

def anagram_pairs(word):
    anagram_map = {}
    for w in word:
        sorted_key = "".join(sorted(w))
        if sorted_key in anagram_map:
            anagram_map[sorted_key].append(w)
        else:
            anagram_map[sorted_key] = [w]
    return list(anagram_map.values())


text = input("Enter the text: ")

# Text cleaning
text = text.lower()

for char in string.punctuation:
    text = text.replace(char, "")

word = text.split() 

word_count = word_frequency_count(word)
longest_word, average_length = longest_and_average_length(word)
palindrome_words = palindrome(word)

while True:

    print("======= WORD ANALYZER ========")
    print("1. Word frequency count")
    print("2. Most common word")
    print("3. Longest Word")
    print("4. Palindrome words")
    print("5. Anagram pairs")
    print("6. Unique words count")
    print("7. Average word length")
    print("8. Quit")

    choice = input("Enter your choice: ")

    if choice == "8":
        print("Goodbye!")
        break
        
    elif choice == "1":
        for key, value in list(word_count.items())[:5]:
            print(f"{key}: {value}")

    elif choice == "2":
        print("Most common word")
        print(f"{next(iter(word_count))}")

    elif choice == "3":
        print(f"{longest_word} | length:{len(longest_word)}")

    elif choice == "4":
        print(palindrome_words)

    elif choice == "5":
        pairs = [group for group in anagram_pairs(set(word)) if len(group) > 1]
        print(pairs)

    elif choice == "6":
        print(len(set(word)))

    elif choice == "7":
        print("\n7. Average word length")
        print(f"{average_length:.2f}")

    else:
        print("Invalid choice!")
        break