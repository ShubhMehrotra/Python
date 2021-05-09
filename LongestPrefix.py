class PrefixLongest:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        longest_pre=""

        #If There is no common String ,it returns an empy string 
        if not strs:
            return longest_pre
        #Finding the shortest key among the all strings present in list
        shortest=min(strs,key=len)
        
        #Checking constraints if all strings are in lower case or not
        if all (x.islower() for x in strs):

        #Iterating over the each character of the shortest string 
            for i in range(len(shortest)):
            #If all the strings in List and starting with the shortest string then return the shortest string as it is 
                 if all([x.startswith(shortest[:i+1]) for x in strs]):
                        longest_pre=shortest[:i+1]
                 else:
                     break
        return longest_pre

a=PrefixLongest()
print(a.longestCommonPrefix(["shubh","shubhi","shubham","shubhansh"]))
        
