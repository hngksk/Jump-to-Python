# 4-3 파일 읽고 쓰기

# 파일 생성하기
f = open("새파일.txt", 'w')
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    print(data)

# 파일을 읽는 여러 가지 방법
# readline 함수 이용하기
f = open("새파일.txt", 'r')
line = f.readline()
print(line)
f.close()

# f = open("새파일.txt", 'r')
# while True:
#     line = f.readline()
#     if not line:
#         break
#     print(line, end='')
# f.close()

# readlines 함수 사용하기
f = open("새파일.txt", 'r')
lines = f.readlines()
for line in lines:
    line = line.strip() # 줄 끝의 줄 바꿈 문자를 제거한다.
    print(line)
f.close()

# read 함수 사용하기
f = open("새파일.txt", 'r')
data = f.read()
print(data)
f.close()

# 파일 객체를 for문과 함께 사용하기
f = open("새파일.txt", 'r')
for line in f:
    print(line)
f.close()

# 파일에 새로운 내용 추가하기
f = open("새파일.txt", 'a')
for i in range(11, 20):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

# with문과 함께 사용하기
with open("새파일.txt", 'a') as f:
    f.write("Life is too short, you need python")