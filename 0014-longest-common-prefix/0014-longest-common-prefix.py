class Solution:
    def longestCommonPrefix(self, strs=["flower","flow","flight"]) -> str:

        self.temp_list = []
        self.letter_count = 0
        self.prefix = ""

        def reps(self):
            for word in strs :
                try:
                    self.temp_list.append(word[self.letter_count])
                except :
                    return "Blow"
            
            try :
                if([self.temp_list[0]]*len(self.temp_list) == self.temp_list):
                    return("Equal")
                else:
                    return("Not equal")
            except :
                return ("Blow")


        self.signal = True
        while self.signal == True :
            reps(self)
            if reps(self) == "Equal" :
                self.prefix+=self.temp_list[0]
                self.temp_list = []
                self.letter_count +=1 
            elif reps(self) == "Not equal" or reps(self)=="Blow":
                self.signal = False

        return(self.prefix)
            