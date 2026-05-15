def group_anagrams(words):
    anagram_map = {}

    for word in words:
        sorted_key = "".join(sorted(word))

        if sorted_key in anagram_map:
            anagram_map[sorted_key].append(word)
        else:
            anagram_map[sorted_key] = []
            anagram_map[sorted_key].append(word)

    return list(anagram_map.values())

print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))