"""
* Review
- 1st : 1/28/2024
- 2nd : 2/23/2024

"""

# 질문
# 스택에 값을 두개씩 넣었는데 왜 첫번째 인자만 출력이 되는거지?


class MinStack:

    def __init__(self):
        self.minstack = []

    def push(self, val: int) -> None:

        if not self.minstack:
            self.minstack.append((val, val))
            return

        current_min = self.minstack[len(self.minstack) - 1][1]

        if val < current_min:
            current_min = val

        self.minstack.append((val, current_min))

    def pop(self) -> None:
        self.minstack.pop()

    def top(self) -> int:
        return self.minstack[len(self.minstack) - 1][0]

    def getMin(self) -> int:
        return self.minstack[len(self.minstack) - 1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
