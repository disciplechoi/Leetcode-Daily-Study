# 1회독 1/27/2024
# 2nd Review 2/12/2024

# 왜 스택으로 풀어야하는건지 모르겠다. => ..이 나올 경우 마지막에 있는 값을 pop해야하기 때문에 스택이 필요한 부분임.


# Sol) 이거 leetcode에서 실행 시 오답으로 나옴 왜? 릿코드 매개변수가 뭔지 잘봐라
# strs=str.split('/')
# print(strs)

# answer = []
# new = ""

# while len(strs) > 0 :
#     current = strs.pop()

#     if current == '' or current == '.':
#         continue
#     elif current == '..':
#         strs.pop()
#     else :
#         answer.append('/'+current)


# for i in answer :
#     new = i + new


# print(new)


# Sol2)
# TC : O(N)
# MC : O(N)
str = "/home//foo/"
stack = []

for path in str.split("/"):

    if path == "..":
        stack.pop()

    elif path == "." or not path:
        continue

    else:
        stack.append(path)


answer = "/" + "/".join(stack)  # <- 이부분이 무엇을 뜻하는 것인지 공부가 필요하다.

print(answer)
