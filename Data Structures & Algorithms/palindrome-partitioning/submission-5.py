class Solution:
    def partition(self, s: str) -> List[List[str]]:
        out = []

        def is_palindrome(s1):
            return s1 == s1[::-1]

        def dfs(i,arr):

            if i == len(s):
                out.append(arr.copy())
                return

            for j in range(i,len(s)):

                substr = s[i:j+1]

                if is_palindrome(substr):

                    arr.append(substr)

                    dfs(j+1, arr)

                    arr.pop()


        dfs(0,[])
        return out