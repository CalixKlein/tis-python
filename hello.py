#hello.py
"""
print(1+1)


print("Hello world")
"""
"""
print(1+1)
print("Hello world")
"""

"""
a = 123
print(a)

a = 2.3
print(a)

a = 3
b = 4

print(a + b)

print (a/b) #소수점
print( 7//3) #몫을 구하는 연산자
print(2 ** 3) #2^3
print(7%3) #나머지를 구하는 연산자
"""


#"Hello world" #둘다 문자열
#'Hello world' 

#p1 = "python's good"
#p2 = 'python"s good'


#print(p1)
#print(p2)


#content = "Life is too shorte you need python"
#print(content)
#content2 = """
#Life is too short
#you need python
#"""
#print(content2)

#head = "python"
#tail = " is fun"

#print(head + tail)

#print(head + 2) #error 

#a = "pyhon"

#print(a * 2)

#print("=" * 30)
#print("Hello world")
#print("=" * 30)

#문자열 인덱싱과 슬라이싱
# a = "Life is too short, You need Python"
    #1234

#print(a[3])

#print(a[33])
#print(a[-1])

#b = a[0] + a[1] + a[2] + a[3]
#print(b)
#print(a[0:4])
#print(a[12:17])
#print(a[:17])
#print(a[19:])
#print(a[:])
#print(a[19:-7])

#a = "20010331Rainy"
#data = a[:8]
#weather = a[8:]

#print(data)
#print(weather)

#"pithon" -> "python"

#a = "pithon"
# a[1] = "y" error

#a = a[0] + "y" + a[2:]
#print(a)

#문자열 포매팅

#a = "I eat %d apples." %3

#print(a)


#number = 10
#day = "three"

#a = "i ate %d apples, so I was sick for %s day" %(number, day)
#print(a)

#a = "I have %s apples" %3
#print(a)

#a = "%10s" % "hi"  #   hi
#print(a)

#a = "%-10s" % "hi" #hi
#print(a)

#a = "%10.4f" % 3.43245
#print(a)

#a = "%-10.4f" % 3.43245
#print(a)

#a = "I eat {0} apples".format("five")
#print(a)


#number = 3

#a = "I eat {0} apples".format(number)
#print(a)

#number = 3
#day = "three"

#a = "I eat {0} apples, so I was sick for {1} days".format(number,day)

#print(a)

#a = "{0:<10}".format("hi") #hi
#print(a)

#a = "{0:>10}".format("hi") #        hi
#print(a)

#a = "{0:^10}".format("hi") #    hi
#print(a)

#a = "{0:=^10}".format("hi")#====hi====
#print(a)

#a = "{0:!>10}".format("hi")#!!!!!!!hi
#print(a)

# y = 3.234524
# a = "{0:10.4f}".format(y)#  3.2345
# print(a)

# name = "홍길동"
# age = 10

# d = {'name':'홍길동','age':30}
# print(f'나의 이름은{name}이고, 나이는 {age}입니다.')

# d = {'name':'홍길동','age':30}
# print(f'나의 이름은{d["name"]}이고, 나이는 {d["age"]}입니다.')

# a = "hobby"
# print(a.count("b")) # b의 갯수(2)

# a = "Python is the best choice"
# print(a.find("b")) #b의 인덱스 값(14)

# a = "Life is too short"
# print(a.index("t")) #첫번째 나오는 t의 인덱스 값(8) 단, 문자가 없으면 오류 발생
# print(a.index("z")) #"z"는 존재하지 않는 문자이기 때문에 에러 발생

# a = ",".join("abcd")
# print(a) #a,b,c,d

# lower()
# upper()
# lstrip()
# rstrip()
# strip()

# a = "Life is too short"
# print(a.replace("Life","Your leg")) # Your leg is too short
# print(a.split()) #['Life','is','too','short']

# b = "a:b:c:d"
# print(b.split(":")) #['a','b','c','d']


#리스트 자료형
# odd = [1,3,5,7,9]

# a = []  # a = list()
# b = [1,2,3] #
# c = ["Life",'is']
# d = [1,2,"Life"]
# e = [1,2,['Life','is']]

# a = [1,2,3,4,5]

# print(a[0:2])
# print(a[:2])
# print(a[2:])

# print(a[0]+a[1])
# print(a[-1])

# a = [1,2,3,['a','b','c']]

# print(a[0]) #1
# print(a[-1]) #['a','b','c']
# print(a[3]) #['a','b','c']
# print(a[3][0]) #a
# print(a[-1][-3]) #a
# print(a[-1][0]) #a
# print(a[-1][1]) #b
# print(a[3][2]) #a

# a = [1,2,['a','b',['Life','is']]]
# print(a[2][2][0])

# a = [1,2,3]
# b = [4,5,6]
# c = a + b  #[1,2,3,4,5,6]
# print(a + b) # [1,2,3,4,5,6]
# print("="*30)
# print(c) #[1,2,3,4,5,6]
# # print(a * b) #error

# print(a * 3) #1,2,3,1,2,3,1,2,3
# print(len(a)) #길이값(3)

# # print(a[2]+"hi") #error
# print(str(a[2])+"hi") #3hi

# a = [1,2,3] #[1,2,3]
# a[2] = 4 #[1,2,4]
# print(a) #[1,2,4]

# del a[1] #[1,4]
# print(a)

# a = [1,2,3,4,5]
# del a[2:] #[3,4,5]삭제
# print(a) #[1,2]

# a = [1,2,3] #a[1,2,3]
# a.append(4) #a[1,2,3,4]
# print(a) #a[1,2,3,4]
# a.append([5,6]) #a[1,2,3,4, [5,6]]
# print(a) #a[1,2,3,4, [5,6]]

# a = [1,4,6,3]
# a.sort()
# print(a)


# a = ['a','z','k']
# a.sort() 
# print(a)

# a = ['a','z','k']
# a.reverse()
# print(a)

# a = ['a','z','k']
# print(a.index('a'))
# # print(a.find('a')) #error
# a = [1,2,3]
# a.insert(0,4)
# print(a)

# a = [1,2,3,1,2,3]
# a.remove(3) #a[1,2,1,2,3] 첫번째 3 삭제
# print(a)
# a.remove(3) #a[1,2,1,2]두번째 3 삭제
# print(a) #[1,2,1,2]

# a = [1,2,3]
# a.pop()
# print(a)

# a = [1,2,3]
# a.pop(1) #삭제하고싶은 index번호 지정
# print(a)

# a = [1,2,3,1]
# print(a.count(1))

# a.extend([4,5]) #리스트 형태의 값만 추가 가능, 삽입시에는 각각의 값으로 분리된다.
# print(a)

#튜플 자료
# 리스트와 튜플은 사용법이 비슷하다. 단 튜플은 수정이 불가능하다.
# t1 = ()
# t2 = (1,) #튜플의 값을 하나만 초기화할 경우 값뒤에 ,를 꼭 붙인다.
# t3 = (1,2,3)
# t4 = 1,2,3,4
# t5 = ('a','b',('ab','db'))

t1 = (1,2,'a','b')
# del t1[0] 
# t1[0] = 'c'

# print(t1[0])
# print(t1[1:])

# t1 = (1,2,'a','b')
# t2 = (3,4)

# print(t1 + t2)
# print(t2 * 3)

# print(len(t1))

#딕셔너리 자료형
# a = {key:value,key:value.......}

# a = {1:'a'}
# a[2] = 'b'
# print(a)
# a['name'] = 'pey'
# print(a)
# a[3] = [1,2,3]
# print(a)

# del a[1]
# print(a)

# grade = {'pey':10,'julliet':99}
# print(grade['julliet'])
# print(grade['pey'])

# a = {1:'a',1:'b'}
#print(a)

#a = {[1,2]:'hi'}

# a = {'name':'pey', 'phone': '0119993323','birth':'1118'}
# print(a.keys())
# print(list(a.keys())) #리스트 형태로 반환

# for k in a.keys():
    # print(k)

# print(a.values())
# print(list(a.values()))
# for k in a.values():
#     print(k)

# print(a.items())
# print(list(a.items()))

# for k,v in a.items():
#     print(k,v)

# a = {'name':'pey', 'phone': '0119993323','birth':'1118'}
# print(a['name'])
# print(a.get('name'))
# print(a.get('phone'))

# print('name' in a) #True, False
# print('email' in a) #False

#집합 자료형
# s1 = set()
# s2 = set([1,2,3])
# s3 = {1,2,3}

# print(s1)

# s1 = set([1,2,3]) #index개념이 없음
# print(s1)
# list1 = list(s1)
# print(list1)
# print(list1[0])

# t1 = tuple(s1)
# print(t1)

#교집합, 합집함, 차집합 구하기

# s1 = {1,2,3,4,5,6}
# s2 = {4,5,6,7,8,9}


#교집합
# print(s1 & s2)

#합집합
# print(s1 | s2)

# s1 = {1,2,3}
# s1.add(4)
# print(s1)

# s1.update([4,5,6]) #update()는 매게 변수를 리스트 구조로 사용해야 한다.
# print(s1)

# s1.remove(6)
# print(s1)

#불 자료형
#True, False
# a = True
# print(a)
# print(type(a))

# print(1==1)

# a = [1,2,3,4,5]
# while a:
#     print(a.pop())


# if []: #값이없으면 false
#     print("참")
# else:
#     print("거짓")

# print(bool('python')) #Ture
# print(bool(a)) #Ture
# print(bool(0)) #false
# print(bool(1)) #Ture

# a = [1,2,3]
# b = a # b = a[:] -> b = a[0:3]
# print(a)

# from copy import copy   #copy import
# a = [1,2,3]
# b = copy(a) #b = [1,2,3]

# print(b)

# a,b = ('python','life')
# (a,b) = 'python','life'
# [a,b] = ['python','life']

# a = 10
# b = 20

# print(a,b)

# a,b = b,a

# print(a,b)

#Q1. 홍길동 씨의 과목별 점수는 다음과 같다. 홍길동 씨의 평균 점수를 구해보자.
# kor = 80
# eng = 75
# math = 55
# print((kor+eng+math)/3)

#Q2. 자연수 13이 홀수인지 짝수인지 판별할 수 있는 방법에 대해 말해 보자.
# result = 13%2
# print(result)

#Q3. 홍길동 씨의 주민등록번호는 881120-1068234이다. 홍길동 씨의 주민등록번호를 연월일(YYYYMMDD) 부분과 그 뒤의 숫자 부분으로 나누어 출력해 보자.
# jumin = "881120-1068234"
# fjumin = jumin[:6]
# bjumin = jumin[7:]
# print(fjumin)
# print(bjumin)

#Q4. 주민등록번호 뒷자리의 맨 첫 번째 숫자는 성별을 나타낸다. 주민등록번호에서 성별을 나타내는 숫자를 출력해 보자.
# pin = "881120-1068234"

# if int(pin[7])==1 or int(pin[7])==3:
#     print("남자")
# elif int(pin[7])==2 or int(pin[7])==4:
#     print("여자")


#Q5. 다음과 같은 문자열 a:b:c:d가 있다. 문자열의 replace 함수를 사용하여 a#b#c#d로 바꿔서 출력해 보자.
# a = "a:b:c:d"
# b = a.replace(":","#")
# print(b)

#Q6.[1, 3, 5, 4, 2] 리스트를 [5, 4, 3, 2, 1]로 만들어 보자.
# a = [1,3,5,4,2]
# a.sort()
# a.reverse()
# print(a)

#Q7. ['Life', 'is', 'too', 'short'] 리스트를 Life is too short 문자열로 만들어 출력해 보자.
# a = ['Life','is','too','short']
# result = " ".join(a)
# print(result)


#Q8.(1,2,3) 튜플에 값 4를 추가하여 (1,2,3,4)를 만들어 출력해 보자.
# a = (1,2,3)
# a = a+(4,)
# print(a)

#Q10 딕셔너리 a에서 'B'에 해당되는 값을 추출해 보자.
# a = {'A':90,'B':80,'C':70}
# result = a.pop('B') #result = 80, a에 있는 B값 삭제
# print(a)
# print(result)

#Q11. a 리스트에서 중복 숫자를 제거해 보자.
# a = [1,1,1,2,2,3,3,3,4,4,5]
# aSet = set(a)
# print(aSet)
# b = list(aSet)
# print(b)


#Q12.파이썬은 다음처럼 동일한 값에 여러 개의 변수를 선언할 수 있다. 
# 다음과 같이 a, b 변수를 선언한 후 a의 두 번째 요솟값을 변경하면 b 값은 어떻게 될까? 
# 그리고 이런 결과가 오는 이유에 대해 설명해 보자.
# a = b = [1,2,3]
# a[1] = 4
# print(a)
# print(b)


# if 조건식(True or False):
#   실행문
#else:
#   실행문

# money = True
# if money:
#     print("차타고 가라")
# else:
#     print("걸어가라")

# money = 2000
# if money >= 3000:
#     print("택시를 타라")
# else:
#     print("걸어가라")

# pocket = ['paper','cellphone','money']

# if 'money' in pocket:
#     pass  #print('택시를 타라')
# else:
#     print('걸어가라')





# pocket = ['paper','cellphone','money']

# if 'money' in pocket:
#     pass  #print('택시를 타라')
# else:
#     if card:
#         print('택시를 타라')
#     else:
#         print('걸어가라')


# print('번호선택:')
# num = int(input())
# if num == 1:
#     print('red')
# elif num == 2:
#     print('blue')
# elif num == 3:
#     print('green')
# else:
#     print('etc')

# score = 60
# if score >= 40:
#     message = "success"
# else:
#     message = "failure"
# print(message)

# #조건부 표현식
# message = ("success" if score >= 60 else "failure")
# print(message)

#while 조건식:
    # 실행문
    # 실행문

# treeHit = 0
# while treeHit < 10:
#     treeHit = treeHit +1
#     print("나무를 %d번 찍었습니다." % treeHit)
#     if treeHit == 10:
#         print("나무 넘어 갑니다.")


# prompt = """
#     1.Add
#     2.Del
#     3.List
#     4.Quit

#     Enter number
# """
# number = 0

# while number != 4:
#     print(prompt)
#     number = int(input())


# coffee = 10
# money = 300

# while money:
#     print("돈을 받았으니 커피를 건네줍니다.")
#     coffee = coffee - 1
#     print("남은 커피량은 %d개 입니다." %coffee)
#     if coffee == 0:
#         print("커피가 다 떨어졌습니다.")
#         break

# a = 0
# while a < 10:
#     a = a+1
#     if a %2 == 0:
#         continue
#     print(a)

#while True:
#    실행문

# for 변수 in (리스트 or 튜플 or 문자열):
#     실행문
#     실행분

# test_list = ['one','two','three']

# for i in test_list:
#     print(i)

# a = [(1,3),(3,4),(5,6)]
# for (first,last) in a:
#     print(first, last)

# marks = [90,25,67,45,80]

# for i in marks:
#     if i >= 60:
#         print("합격")
#     else:
#         print("불합격")


# a = range(10)  #0~9정수
# print(a)

# a = range(1,11) #1~10
# for i in range(1,11):
#     print(i)

# for i in range(2,10):
#     for j in range(1,10):
#         print(i*j,end = " ") #end = 줄바꿈 방지
#     print(' ') #줄바꿈 실행

# a = [1,2,3,4]
# result = []
# for num in a:
#     result.append(num*3)

# print(result)

# a = [1,2,3,4]
# result = [num * 3 for num in a]

# print(result)

a = [1,2,3,4]
result = [num * 3 for num in a if num % 2 == 0]
print(result)

# money = 2000
# card = True
# if money >= 3000 or card:
#     print("택시를 타라")
# else:
#     print("걸어가라")
# p = "python"
# print('a' in ('a','b','c')) #True
# print('j' not in p) #True


#Q1 : python
# a = "Life is too short, you need python"

# if "wife" in a: print("wife")
# elif "python" in a and "you" not in a: print("python")
# elif "shirt" not in a: print("shirt")
# elif "need" in a: print("need")
# else: print("none") 
# shirt 

#Q2. while문을 사용해 1부터 1000까지의 자연수 중 3배수의 합을 구해 보자.
# a = 1
# b = 0
# while a < 1000:
#     a = a+1
#     if a%3==0: 
#         b = b+a

# print(b)

#Q3. while문을 사용하여 *을 표시하는 프로그램을 작성해 보자
# a = 0
# while a < 5:
#     a = a+1
#     print("*"*a)

#Q4. for문을 사용해 1부터 100까지의 숫자를 출력해보자
# a = 0
# for a in range(100):
#     a = a+1
#     print(a)

#Q5. A학급에 총 10명의 학생이 있다. 이 학생들의 중간고사 점수로 A학급의 평균을 구해보자
# a = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
# sum = 0
# i = 0
# for a in a:
#     i = i+1
#     sum = sum + a
# avg = sum/i

# print(avg)

#Q6. 리스트 중에서 홀수에만 2를 곱하여 저장하는 코드가 있다. 내포를 사용하여 표현해보자
# numbers = [1, 2, 3, 4, 5]
# result = []
# for n in numbers:
#     if n % 2 == 1:
#         result.append(n*2)

