class Solution:
    def countVowels(self, word: str) -> int:

        cnt = 0
        vowels = ['a', 'e', 'i', 'o', 'u']
        n = len(word)
        for i in range(len(word)):
            if word[i] in vowels:
                cnt += ((i + 1) * (n - i) )
        return cnt

        
