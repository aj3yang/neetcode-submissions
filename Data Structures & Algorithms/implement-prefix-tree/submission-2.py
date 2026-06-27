class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.end_of_word = False


class PrefixTree:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        cur = self.root
        for i in word:
            v = ord(i) - ord('a')
            if cur.children[v] == None:
                new_node = TrieNode()
                cur.children[v] = new_node
            cur = cur.children[v]
        cur.end_of_word = True

    def search(self, word: str) -> bool:
        cur = self.root
        for i in word:
            v = ord(i) - ord('a')
            if cur.children[v] == None:
                return False
            cur = cur.children[v]
        return cur.end_of_word
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for i in prefix:
            v = ord(i) - ord('a')
            if cur.children[v] == None:
                return False
            cur = cur.children[v]
        return True