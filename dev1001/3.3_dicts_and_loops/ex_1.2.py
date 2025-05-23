# **Create 1.2: Simple Word Frequency Counter**

# *   **Problem:** Given a paragraph of text (as a multi-line string), count how many times each word appears.
# *   **Task:**
#     1.  Store the following sample text in a variable:
#         ```
#         text = """
#         This is a sample text. This text is for a sample programming exercise.
#         The exercise is to count words in this text.
#         Ignore case and punctuation for simplicity.
#         """
#         ```
#     2.  Pre-process the text:
#         *   Convert it all to lowercase.
#         *   Remove common punctuation (e.g., periods `.`, commas `,`). You can use string `.replace()` method multiple times.
#         *   Split the text into a list of words using `.split()`.
#     3.  Create an empty dictionary.
#     4.  Iterate through your list of words. For each word:
#         *   If the word is already a key in your dictionary, increment its value (count).
#         *   If the word is not yet a key, add it to the dictionary with a value of 1.
#     5.  After processing all words, print the dictionary of word frequencies.
#     6.  Then, print each word and its count in a more readable format (e.g., "word: count").
# *   **Advanced Challenge 1.2:**
#     *   Modify your output to print the words sorted alphabetically.
#     *   Then, modify it again to print the words sorted by their frequency (most frequent first). If frequencies are tied, alphabetical order for those words is fine.
#     *   *(Hint: For sorting dictionary items, you might need to convert `dictionary.items()` to a list and then use `list.sort()` or the `sorted()` built-in function, possibly with a `lambda` key in the future, but for now, you might have to create lists of tuples and sort those.)*