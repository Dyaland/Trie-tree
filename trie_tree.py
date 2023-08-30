class WordAlreadyExistsError(ValueError):
    def __init__(self, word:str):
        super().__init__(f"'{word}' already exists in the trie.")

class WordNotFoundError(ValueError):
    def __init__(self, word):
        super().__init__(f"'{word}' not found in the trie.")

class PrefixNotFoundError(ValueError):
    def __init__(self, prefix):
        super().__init__(f"'{prefix}' is not a prefix in the trie.")

class WordNotInTrieError(ValueError):
    def __init__(self, word):
        super().__init__(f"'{word}' is not in the trie.")


class TrieNode:
    """Node containing a character and bool for end of word."""

    def __init__(self):
        """Instantiate a trie node"""

        self.children = {}
        self.end_of_word = False


class TrieTree:

    def __init__(self):
        """Create the empty tree root"""

        self.root = TrieNode()

    def insert(self, word: str):
        """Insert a word into the trie tree."""

        cur = self.root

        for c in word.lower():
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]

        if cur.end_of_word == True:
            raise WordAlreadyExistsError(word)

        cur.end_of_word = True

    def search(self, word: str):
        """Returns whether a word is in the trie tree."""

        cur = self.root

        for c in word.lower():
            if c not in cur.children:
                raise WordNotFoundError(word)
            cur = cur.children[c]

        if not cur.end_of_word:
            raise WordNotFoundError(word)

        return True

    def starts_with(self, prefix: str, strict: bool=False):
        """Check if the input phrase exist. Set strict=True to not count words with no children as prefixes."""

        cur = self.root

        for c in prefix.lower():
            if c not in cur.children:
                raise PrefixNotFoundError(prefix)

            cur = cur.children[c]

        # strict logic
        if strict == False:
            return True  # Partial and complete matches count.
        else:
            if cur.children:
                return True  # Only partial matches count.
            else:
                raise PrefixNotFoundError(prefix)

    def prefix_matches(self, prefix: str, strict: bool=False):
        """Find all words in the trie that start with the input prefix. Set strict=True to not count words with no children as prefixes."""

        matching_words = []

        def traverse(node, current_word):
            if node.end_of_word:
                matching_words.append(current_word)

            for char, child_node in node.children.items():
                traverse(child_node, current_word + char)

        cur = self.root
        for c in prefix.lower():
            if c not in cur.children:
                raise PrefixNotFoundError(prefix)
            cur = cur.children[c]

        traverse(cur, prefix)

        # strict logic
        if strict == True:
            if cur.end_of_word:
                matching_words.pop(0)  # Count only partial matches, removing the first word if input was a stored word.

        return matching_words

    def delete(self, word: str):
        """Delete a word from the trie tree."""

        def delete_recursive(node, chars: str):
            if len(chars) == 0:
                node.end_of_word = False
                return len(node.children) == 0

            char = chars[0]
            can_delete_child = char in node.children and delete_recursive(node.children[char], chars[1:])

            if can_delete_child:
                node.children.pop(char, None)

            return len(node.children) == 0 and not node.end_of_word

        try:
            self.search(word)
        except WordNotFoundError:
            raise WordNotInTrieError(word)
        else:
            delete_recursive(self.root, word.lower())
            return True

    def all_words(self):
        """Generate all words in the trie."""

        def traverse(node, current_word):
            if node.end_of_word:
                yield current_word

            for char, child_node in node.children.items():
                yield from traverse(child_node, current_word + char)

        yield from traverse(self.root, "")

    def words_count(self):
        """Count words in trie"""

        def traverse(node):
            count = 0
            if node.end_of_word:
                count += 1

            for child in node.children.values():
                count += traverse(child)
            return count

        return traverse(self.root)

    def nodes_count(self):
        """Count the number of nodes in the trie."""

        def traverse(node):
            count = 1
            for child in node.children.values():
                count += traverse(child)
            return count

        return traverse(self.root)