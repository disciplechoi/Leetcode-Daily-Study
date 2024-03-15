"""
* Review
- 1st : 1/28/2024
- 2nd : 2/23/2024

"""


class MinStack:

    def __init__(self):
        self.minstack = []

    def push(self, val: int) -> None:

        if not self.minstack:
            self.minstack.append((val, val))
            return

        current_min = self.minstack[len(self.minstack) - 1][1]  # [-1][1]로 대체가능.

        if val < current_min:
            current_min = val

        self.minstack.append((val, current_min))

    def pop(self) -> None:
        self.minstack.pop()  # pop을 하게 되면 그 전에 쌓인 데이터 중 가장 작은 데이터에 대한 히스토리를 갖고 있는게 중요하다.

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
