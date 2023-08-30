import unittest

from trie_tree import TrieTree, WordAlreadyExistsError, WordNotFoundError, PrefixNotFoundError, WordNotInTrieError


class TestTrieUnittest(unittest.TestCase):

    def test_insert_and_search(self):
        trie = TrieTree()
        trie.insert('factorial')
        
        with self.assertRaises(WordAlreadyExistsError):
            trie.insert('factorial')
        
        self.assertTrue(trie.search('factorial'))
        
        with self.assertRaises(WordNotFoundError):
            trie.search('factor')
            
        trie.insert('factor')
        self.assertTrue(trie.search('factor'))

    def test_starts_with_and_prefix_matches(self):
        trie = TrieTree()
        trie.insert('tungsten')
        trie.insert('tundra')

        # starts_with
        self.assertTrue(trie.starts_with('tung'))
        
        with self.assertRaises(PrefixNotFoundError):
            trie.starts_with('tug')

        #prefix_matches
        assert(len(trie.prefix_matches('tun')) == 2)
        assert(len(trie.prefix_matches('tung')) == 1)
        with self.assertRaises(PrefixNotFoundError):
            trie.prefix_matches('pol')

    def test_delete(self):
        trie = TrieTree()
        trie.insert('mistake')
        
        with self.assertRaises(WordNotInTrieError):
            trie.delete('mistak')

        self.assertTrue(trie.delete('mistake'))

    def test_all_names(self):
        trie = TrieTree()
        trie.insert('article')
        trie.insert('calendar')
        trie.insert('franchise')
        expected_words = ['franchise', 'article', 'calendar']
        self.assertCountEqual(trie.all_words(), expected_words)

    def test_words_count_and_nodes_count(self):
        trie = TrieTree()
        trie.insert('sign')

        # nodes_count
        assert(trie.nodes_count() == 5)
        trie.insert('signal')
        assert(trie.nodes_count() == 7)

        # words_count
        assert(trie.words_count() == 2)
        

if __name__ == '__main__':
    unittest.main()
