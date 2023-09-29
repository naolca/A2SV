class TrieNode:
    def __init__(self):
        self.children = [None for i in range(26)]
        self.isEnd = False
        # how many words have the path leading to this node as a prefix
        self.ending = 0
class Trie:

    def __init__(self):
        self.root = TrieNode()
        self.words = defaultdict(int)
        

    def insert(self, word: str, val: int):

        
        curr = self.root
        
        for c in word:
            if not curr.children[ord(c) - ord('a')]:
                curr.children[ord(c) - ord('a')] = TrieNode()
            curr = curr.children[ord(c) - ord('a')]
            curr.ending += (val - self.words[word])
        self.words[word] = val
        curr.isEnd = True
        
        # print(self.root)

        

    
        

    def startsWith(self, prefix: str) -> int:
        
        curr = self.root
        valid = True
        for c in prefix:
            n = ord(c) - ord('a')
            if not  curr.children[n]:
                valid = False
                break
            curr = curr.children[n]
        # print(curr.ending)
        if valid:
            return int(curr.ending)
        return 0
    


class MapSum:

    def __init__(self):
        self.trie = Trie()
        

    def insert(self, key: str, val: int) -> None:
        # if key in self.trie.words:
        #     self.trie.insert(key, val - self.trie.words[key])
        #     self.trie.word[key] = val - self.trie.words[key]
        #     return
        self.trie.insert(key, val)

        

    def sum(self, prefix: str) -> int:
        return self.trie.startsWith(prefix)
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
