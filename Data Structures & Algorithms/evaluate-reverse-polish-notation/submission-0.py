class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        n = len(tokens)

        def opp(a,b, x:str):

            a = int(a)
            b = int(b)

            match x:

                case "+":
                    return str(a+b)
                case "*":
                    return str(a*b)
                case "-":
                    return str(a-b)
                case "/":
                    return str(int(a/b))


        for i in range(n):

            if tokens[i].lstrip("-").isdigit():

                stack.append(tokens[i])
            else:

                b = stack.pop()
                a = stack.pop()

                val = opp(a,b,tokens[i])

                stack.append(val)

        return int(stack[-1])

            