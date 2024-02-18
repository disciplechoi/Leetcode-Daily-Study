
# 1. 두개의 리스트의 길이가 다른데 언제가지 for 문을 돌려야 하는 건지 모르겠다.
# 2. 덧셈을 했을 떄 10 이상의 숫자가 나올 수 있는데 두개의 digit을 배열 한자리에 따로 넣어야 하는것이 중요하다.
# 3. 배열 크기를 미리 선언할 수 없다.
# 4. 배열을 마지막에 리버스 해야한다. => 거꾸로 된 것이 좋음. 어차피 덧셈은 뒤에서 시작함.


l1 = [2,4,3]
l2 = [5,6,4]

number1,number2 = 0,0
j = 0

for i in l1 :
    number1 = number1 + i*pow(10,j)
    #print(pow(10,2))
    #print(number1)
    j +=1

j=0 
for i in l2 :
    number2 = number2 + i*pow(10,j)
    #print(pow(10,2))
    #print(number1)
    j +=1

print(number1)
print(number2)
        