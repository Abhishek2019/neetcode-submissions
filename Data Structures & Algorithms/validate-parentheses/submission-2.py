class Solution:
    def isValid(self, s: str) -> bool:
        
        stk = []


        open = set(['{','[',"("])
        close = set(['}',']',")"])


        def match_brac(o,c):


            if o == "[" and c =="]":
                return True

            if o == "{" and c =="}":
                return True

    
            if o == "(" and c ==")":
                return True

            return False


        for i in s:

            if not stk:
                stk.append(i)

            else:

                if i in open:

                    if stk[-1] in open:
                        stk.append(i)
                    
                    else:
                        return False

                else:
                    if not match_brac(stk.pop(),i):
                        return False



        
        if not stk:
            return True

        return False

            

