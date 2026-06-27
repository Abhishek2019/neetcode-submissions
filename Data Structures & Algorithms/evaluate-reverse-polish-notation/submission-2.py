import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def calc(a,b,opp):

            a = int(a)
            b = int(b)
            match opp:
                case '+':
                    return a+b
                case '-':
                    return a-b
                case '*':
                    return a*b
                case '/':
                    return int(a/b)

        out = []

        for i in tokens:

            print(out)
            if i.isdecimal() or i[1:].isdecimal():
                out.append(int(i))
            
            else:
                print(i)
                b = out.pop()
                a = out.pop()

                res = calc(a,b,i)

                out.append(res)

        return out[0]