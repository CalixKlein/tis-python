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
a = "Life is too short, You need Python"
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

a = ",".join("abcd")
print(a) #a,b,c,d

# lower()
# upper()
# lstrip()
# rstrip()
# strip()

a = "Life is too short"
print(a.replace("Life","Your leg")) # Your leg is too short
print(a.split()) #['Life','is','too','short']

b = "a:b:c:d"
print(b.split(":")) #['a','b','c','d']
