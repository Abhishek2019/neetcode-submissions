class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        input = "".join(["()" for _ in range(n)])

        out = []
        used = set()
        
        def dfs(arr,open,close):
            nonlocal out

            if len(arr) == len(input) and open == close:
                out.append("".join(arr.copy()))
                return
            
            
            if len(arr) > len(input):
                return

            level_used = set()

            for i in range(len(input)):
                
                if i in used:
                    continue

                if input[i] in level_used:
                    continue
                
                level_used.add(input[i])

                if not arr and input[i] != ")":
                    arr.append(input[i])
                    used.add(i)
                    
                    open+=1
                
                elif input[i] == "(":
                    arr.append(input[i])
                    used.add(i)

                    open+=1
                elif input[i] == ")" and open>close:

                    arr.append(input[i])
                    used.add(i)
                    close+=1
                else:
                    continue
                
                dfs(arr,open,close)

                ele = arr.pop()
                if i in used:
                    used.remove(i)

                if ele == "(":
                    open-=1
                else:
                    close-=1








        dfs([],0,0)

        return out
        