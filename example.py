# 4장 파이썬의 입력과 출력

# 4-1 함수

# 매개변수와 인수
def add(a, b): # a, b는 매개변수
    return a+b
a = 3
b = 4
print(add(3, 4)) # 3, 4는 인수

# 입력값과 리턴값에 따른 함수의 형태
# 일반적인 함수
def add(a, b):
    result = a + b
    return result
a = add(3, 4)
print(a)

# 입력값이 없는 함수
def say():
    return 'Hi'
a = say()
print(a)

# 리턴값이 없는 함수
def add(a, b):
    print("%d, %d의 합은 %d입니다." % (a, b, a+b))
add(3, 4)
a = add(3, 4)
print(a) # 리턴값이 존재하지 않음

# 입력값, 리턴값이 없는 함수
def say():
    print('Hi')
say()

# 매개변수 지정하여 호출하기
def sub(a, b):
    return a - b
result = sub(a=7, b=3) # a에 7, b에 3을 전달
print(result)

# 입력값이 몇 개가 될지 모를 때?
# 여러 개의 입력값을 받는 함수 만들기
def add_many(*args):
    result = 0
    for i in args:
        result = result + i
    return result
result = add_many(1,2,3,4,5)
print(result)

def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i
        return result
# result = add_mul('add', 1,2,3,4,5)
# print(result)
result = add_mul('mul', 1,2,3,4,5)
print(result)

# 키워드 매개변수 kwargs
def print_kwargs(**kwargs):
    print(kwargs)
print_kwargs(a=1)
print_kwargs(name='foo', age=3)

# 함수의 리턴값은 언제나 하나이다
def add_and_mul(a,b):
    return a+b, a*b
result = add_and_mul(3,4)
print(result)
result1, result2 = add_and_mul(3,4)
print(result1)
print(result2)

# return의 또 다른 쓰임새
def say_nick(nick):
    if nick == '바보':
        return
    print("나의 별명은 %s 입니다." % nick)
say_nick('나나')
say_nick('바보')

# 매개변수에 초깃값 미리 설정하기
def say_myself(name, age, man=True): # 초기화시키고 싶은 매개변수는 항상 뒤쪽에 놓아야 한다!
    print("나의 이름은 %s 입니다." % name)
    print("나이는 %d살입니다." % age)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")
say_myself("나하나", 26, False)

# 함수 안에서 선언한 변수의 효력 범위
a = 3
def vartest(a):
    a = a + 1
vartest(a)
print(a) # def vartest(a)에서 입력값을 전달받는 매개변수 a는 함수 안에서만 사용하는 변수이지 함수 밖의 변수 a와는 전혀 상관이 없다.
# vartest_error
# def vartest(a):
#     a = a + 1
# vartest(3)
# print(a)

# 함수 안에서 함수 밖의 변수를 변경하는 방법
# 1. return 사용하기
a = 1
def vartest(a):
    a = a + 1
    return a
a = vartest(a)
print(a)
# 2. global 명령어 사용하기
a = 1
def vartest():
    global a
    a = a+1
vartest()
print(a)

# lambda
add = lambda a, b: a+b
result = add(3, 4)
print(result)


# 4-2 사용자 입력과 출력

# 사용자 입력
# input의 사용
# a = input()
# a

# 프롬포트를 띄워서 사용자 입력 받기
# number = input("숫자를 입력하세요: ")
# print(type(number)) # input은 입력되는 모든 것을 문자열로 취급함

# 큰따옴표로 둘러싸인 문자열은 + 연산과 동일하며, 문자열 띄어쓰기는 콤마로 한다
print("life" "is" "too short") # 1
print("life"+"is"+"too short") # 2
print("life", "is", "too short")

# 한 줄에 결과값 출력하기
for i in range(10):
    print(i, end=' ')