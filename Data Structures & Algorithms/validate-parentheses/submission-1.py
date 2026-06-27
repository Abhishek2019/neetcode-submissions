class Solution:
    def isValid(self, s: str) -> bool:
        
        openBrac = set(["(","[","{"])

        def close_brac(x:str):

            match x:
                case "]":
                    return "["
                
                case ")":
                    return "("
                
                case "}":
                    return "{"
        
        stack = []

        n = len(s)

        for i in range(n):

            if s[i] in openBrac:
                stack.append(s[i])
            
            else:
                if stack and stack[-1] == close_brac(s[i]):

                    stack.pop()

                else:
                    return False

        if stack:
            return False
        
        return True


