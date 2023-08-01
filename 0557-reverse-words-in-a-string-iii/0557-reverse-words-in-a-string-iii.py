class Solution:
    def reverseWords(self, s: str) -> str:
        word_list = []
        current_word = ""
        for i in s :
            if i == " ":
                word_list.append(current_word[::-1])
                current_word = ""
            else :
                current_word += i
        word_list.append(current_word[::-1])
        
        return " ".join(word_list)