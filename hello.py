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

a = [1,2,3]
a.pop()
print(a)

a = [1,2,3]
a.pop(1) #삭제하고싶은 index번호 지정
print(a)