class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:

        max_bit_len = 0
        for n in nums:
            max_bit_len =  max(n.bit_length(), max_bit_len)

       
        trie = {}
        
        max_xor = 0

        for num in nums:
            cur_xor = 0
            cur_node = trie
            xor_node = trie
            for j in range(max_bit_len, -1, -1):
                bit = num >> j & 1

                if bit not in cur_node:
                    cur_node[bit] = {}
                cur_node = cur_node[bit]
                if 1 - bit in xor_node:
                    cur_xor = cur_xor | (1 << j)
                    xor_node = xor_node[1-bit]
                else:
                    xor_node = xor_node[bit]

            
            max_xor = max(cur_xor, max_xor)

        return max_xor
