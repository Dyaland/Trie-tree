import os

from trie_tree import TrieTree, WordAlreadyExistsError, WordNotFoundError, PrefixNotFoundError, WordNotInTrieError


class TestTrieManual:

    def __init__(self):

        self.trie = TrieTree()

        self.menu_options = {
            '1': self.test_insert,
            '2': self.test_search,
            '3': self.test_starts_with,
            '4': self.test_prefix_matches,
            '5': self.test_delete,
            '6': self.test_all_words,
            '7': self.test_words_count,
            '8': self.test_nodes_count,
            'q': exit
        }

        self.CLEAR = 'clear' if os.name == 'posix' else 'cls'

    def clear_screen(self):
        os.system(self.CLEAR)

    def test_insert(self):

        self.clear_screen()
        print('Add a word to the trie.')
        
        while True:
            user_input = input('\nAdd word: ').lower()

            if user_input.isalpha():
                self.clear_screen()
                try:
                    self.trie.insert(user_input)
                except WordAlreadyExistsError as e:
                    print(f"{type(e).__name__}: {e}")
                    break
                else:
                    print(f"'{user_input}' added to trie object.")
                    break
            else:
                self.clear_screen()
                print('Input must be alphabetical.')

    def test_search(self):
        
        self.clear_screen()
        print('Search for a word in the trie.')
        
        while True:
            user_input = input('\nSearch word: ').lower()

            if user_input.isalpha():
                self.clear_screen()
                
                try:
                    self.trie.search(user_input)
                except WordNotFoundError as e:
                    print(f"{type(e).__name__}: {e}")
                    break
                else:
                    print(f"'{user_input}' exists.")
                    break
            else:
                self.clear_screen()
                print('Input must be alphabetical.')

    def test_starts_with(self):
        
        self.clear_screen()
        print('Check if a prefix exists in the trie.')
        
        while True:
            user_input = input('\nSearch phrase: ').lower()

            if user_input.isalpha():
                self.clear_screen()
                
                try:
                    self.trie.starts_with(user_input, strict=True)
                except PrefixNotFoundError as e:
                    print(f"{type(e).__name__}: {e}")
                    break
                else:
                    print(f"'{user_input}' exists as a prefix.")
                    break
            else:
                self.clear_screen()
                print('Input must be alphabetical.')

    def test_prefix_matches(self):
        
        self.clear_screen()
        print('List all matches for a prefix in the trie.')
        
        while True:
            user_input = input('\nEnter prefix: ').lower()

            if user_input.isalpha():
                self.clear_screen()

                try:
                    matches = self.trie.prefix_matches(user_input, strict=True)
                except PrefixNotFoundError as e:
                    print(f"{type(e).__name__}: {e}")
                    break
                else:
                    print(f"matches for '{user_input}': " + ", ".join(matches))
                    break
            else:
                self.clear_screen()
                print('Input must be alphabetical.')

    def test_delete(self):

        self.clear_screen()
        print('Delete a word in the trie.')

        while True:
            user_input = input('\nDelete word: ').lower()

            if user_input.isalpha():
                self.clear_screen()

                try:
                    self.trie.delete(user_input)
                except WordNotInTrieError as e:
                    print(f"{type(e).__name__}: {e}")
                    break
                else:
                    print(f"'{user_input} deleted.'")
                    break
            else:
                self.clear_screen()
                print('Input must be alphabetical.')

    def test_all_words(self):
        """Display all words in the trie."""
        
        self.clear_screen()
        if self.trie.root.children:
            print('All words: ', end='')
            for word in self.trie.all_words():
                print(word, end=' ', flush=True)
            print()
        
        else:
            print('No words in the trie.')

    def test_words_count(self):
        """Count the number of words in the trie."""
        
        count = self.trie.words_count()
        self.clear_screen()
        print(f'{count} words in the trie.' if count != 1 else f'{count} word stored in the trie.')

    def test_nodes_count(self):
        """Count the number of nodes in the trie."""
        
        count = self.trie.nodes_count()
        self.clear_screen()
        print(f'{count} nodes in the trie.' if count != 1 else f'{count} nodes in the trie.')


    def run(self):

        user_input = ''
        self.clear_screen()
        print('Test the TRIE data structure manually.')

        while True:
            print('\n[1] - Insert word\n[2] - Search word\n[3] - Check prefix\n[4] - All prefix matches\n[5] - Delete word\n[6] - Display all words\n[7] - Count words\n[8] - Count nodes\n[q] - quit')
            user_input = input('\nInput: ').lower()

            if user_input in self.menu_options:
                self.menu_options[user_input]()
            else:
                self.clear_screen()
                print(f"'{user_input}' not a valid choice")
                continue


if __name__ == '__main__':
    test_trie = TestTrieManual()
    test_trie.run()
