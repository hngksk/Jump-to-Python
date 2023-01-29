# 연습문제
# 1. 주어진 자연수가 홀수인지 짝수인지 판별해주는 함수(is_odd)
def is_odd(number):
    if number % 2 == 1:
        print(True)
    else:
        print(False)

is_odd(5)
is_odd(6)

is_odd = lambda x: True if x % 2 == 1 else False
is_odd(3)

# 2. 입력으로 들어오는 모든 수의 평균 값을 계산해주는 함수
#    (단, 입력으로 들어오는 수의 개수는 정해져 있지 않다.)
def avg_num(*args):
    result = 0
    for i in args:
        result += i
    print(result/len(args))
avg_num(1,2,3,4,5)

# 3. 프로그램(두 개의 숫자를 입력받아 더하여 돌려주는 프로그램) 오류 수정
input1 = input("첫 번째 숫자를 입력하세요:")
input2 = input("두 번째 숫자를 입력하세요:")

# total = input1 + input2
total = int(input1) + int(input2)
print("두 수의 합은 %s입니다." % total)

