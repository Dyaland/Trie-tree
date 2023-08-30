# Trie Data Structure in Python  
This repository provides a Python implementation of a Trie data structure designed for efficient string storage and retrieval operations. The Trie data structure is particularly useful for operations like string matching, prefix matching, and quick insertion or deletion of words, making it ideal for use-cases like dictionaries, phone books, and auto-complete features.

## Features
1. **Insertion**: The 'insert' method allows you to insert a new word into the Trie. It throws a custom 'WordAlreadyExistsError' if the word already exists in the Trie.
2. **Search**: The 'search' method performs an exact search for a word in the Trie. If the word does not exist, a custom 'WordNotFoundError' is raised.
3. **Prefix Search**: The 'starts_with' method checks if a given prefix exists in any of the words stored in the Trie. The strict parameter allows you to control whether to include words that exactly match the prefix but have no further children. If the prefix does not exist, a custom 'PrefixNotFoundError' is raised.

4. **Prefix Matches**: The 'prefix_matches' method returns a list of all words in the Trie that start with a given prefix. The strict parameter allows you to exclude words that exactly match the prefix but have no further children.

5. **Deletion**: The 'delete' method deletes a word from the Trie, and it throws a custom 'WordNotInTrieError' if the word does not exist in the Trie.

6. **All Words**: The 'all_words' method returns a generator object that yields all words stored in the Trie.

7. **Word Count**: The 'words_count' method returns the total number of words stored in the Trie.

8. **Node Count**: The 'nodes_count' method returns the total number of nodes in the Trie.

## Exception Handling
Custom exception classes are used to make error handling more descriptive and helpful:

* **WordAlreadyExistsError**: Raised when trying to insert a word that already exists.
* **WordNotFoundError**: Raised when a search for a word returns no result.
* **PrefixNotFoundError**: Raised when a prefix search returns no result.
* **WordNotInTrieError**: Raised when trying to delete a word that doesn't exist in the Trie.

## Testing
This repository includes two testing scripts:

**Manual Testing**: The manual_test.py script provides a user interface for manually testing the Trie operations.

**Unit Testing**: The unit_testing.py script uses Python's built-in unittest framework to automatically test the Trie methods and custom exceptions.

