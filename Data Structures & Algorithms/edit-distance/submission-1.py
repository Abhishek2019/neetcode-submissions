class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        dp = {}

        def dfs(i,j):

            if(i,j) in dp:
                return dp[(i,j)]
            if i==len(word1) and j==len(word2):
                return 0

            if j == len(word2) and i<len(word1):
                return len(word1)-i
            
            if i == len(word1) and j<len(word2):
                return len(word2)-j
            

            s1,s2,s3,s4 = float('inf'),float('inf'),float('inf'),float('inf')

            if word1[i] == word2[j]:
                s1 = dfs(i+1,j+1)


            else:
                
                #delete
                s2 = 1+dfs(i+1,j)

                #replace
                s3 = 1+dfs(i+1,j+1)

                #insert
                s4 = 1+dfs(i,j+1)

            dp[(i,j)] = min(s1,s2,s3,s4)
            return dp[(i,j)]
            

                



                





        out = dfs(0,0)

        return out
