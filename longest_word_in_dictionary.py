class TrieNode:
    def __init__(self):
        self.children = [None for i in range(26)]
        self.isEnd = False
class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str):

       
        curr = self.root
        found = 0
        for c in word:
            if not curr.children[ord(c) - ord('a')]:
                found += 1
                curr.children[ord(c) - ord('a')] = TrieNode()
            curr = curr.children[ord(c) - ord('a')]
        curr.isEnd = True
        return found == 1
        # print(self.root)

        

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            n = ord(c) - ord('a')
            if not curr.children[n]:
                
                return False
            curr = curr.children[n]
        return curr.isEnd
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            n = ord(c) - ord('a')
            if not  curr.children[n]:
                return False
            curr = curr.children[n]
        return True
    


class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        words.sort(key = lambda x : len(x))
        valid = defaultdict(bool)
        valid[""] = True
        # print(words)
        longest = ""
        for i,word in enumerate(words):
            # print(longest)
            if trie.insert(word) and valid[word[: len(word) - 1]]:
                
                valid[word] = True
                if len(longest) < len(word):
                    longest = word
                elif len(longest) == len(word) and word < longest:
                    longest = word
        return longest



        
        
