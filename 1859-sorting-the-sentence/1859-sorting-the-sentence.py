class Solution:
    def sortSentence(self, s):
        
        my_List=s.split()
   
        original_sentence=""
        for i in range(1,len(my_List)+1):
            for string in my_List:
                if int(string[-1])==i:
                    original_sentence+=string[:-1]
                    original_sentence+=" "


        return original_sentence[:-1]


                
        