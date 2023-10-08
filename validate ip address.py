class Solution:
    def validIPAddress(self, queryIP: str) -> str:

        def ipv4(s):
            lst = s.split('.')
            if len(lst) != 4:
                return False
            for string in lst:
                if len(string) > 3 or not string.isdigit() or len(string) != len(str(int(string))) or not (0 <= int(string) <= 255):
                    return False
            
            return True
        # print(ipv4('2001:0db8:85a3:0000:0000:8a2e:0370:7334'))
        def isHex(s):
            hexs = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                    'a', 'b', 'c', 'd', 'e', 'f', 'A', 'B', 'C', 'D', 'E', 'F']
            for char in s:
                if char not in hexs:
                    return False
            return True

        def ipv6(s):

            lst = s.split(':')
            if len(lst) != 8:
                return False
            for string in lst:
                if len(string) > 4 or len(string) == 0 or not isHex(string):
                    return False
            return True



        if ipv4(queryIP):
            return "IPv4"
        if ipv6(queryIP):
            return "IPv6"
        return "Neither"
        
