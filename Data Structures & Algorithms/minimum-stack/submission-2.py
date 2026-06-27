class MinStack:

    def __init__(self):

        self.st = []
        self.min_st = []
        

    def push(self, val: int) -> None:

        self.st.append(val)

        if not self.min_st:
            self.min_st.append(val)
        
        else:
            temp = []

            while self.min_st and val >self.min_st[-1]:
                temp.append(self.min_st.pop())

            self.min_st.append(val)

            while temp:
                self.min_st.append(temp.pop())

        return None
        

    def pop(self) -> None:

        ele = self.st.pop()

        if ele == self.min_st[-1]:
            self.min_st.pop()
        
        else:

            temp = []

            while self.min_st and ele != self.min_st[-1]:
                temp.append(self.min_st.pop())

            self.min_st.pop()

            while temp:
                self.min_st.append(temp.pop())

        return None
        

    def top(self) -> int:

        return self.st[-1]
        

    def getMin(self) -> int:

        return self.min_st[-1]
        
