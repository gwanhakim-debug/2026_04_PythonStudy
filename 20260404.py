#!/usr/bin/env python
# coding: utf-8

# In[1]:


print(200)


# In[ ]:





# In[2]:


print(200)


# In[ ]:


print('123')


# In[ ]:


print(123+1)


# In[ ]:


print(123+1)


# In[ ]:


print(123+1)


# In[9]:


input('입력하세요.')


# In[10]:


a=100b
print(a+10)


# In[ ]:





# In[11]:


b='가나다'
print(b)


# In[1]:


print(123+1)


# In[16]:


s=input('숫자 입력하세요=>')
type(s)
print('출력:',int(s)+10)


# In[17]:


s=input('숫자 입력하세요=>')
type(s)
print('출력:',int(s)+10)


# In[18]:


print('100'+'30')


# In[19]:


a=[1,2,3]
id(a)


# In[20]:


a=[1,2,3]
b=a


# In[21]:


a is b


# In[22]:


a[1]=4


# In[23]:


a


# In[2]:


monye=True


# In[3]:


if money:
    print('있다')


# In[4]:


money=True
type(money)
if money:
    print('있다')


# In[1]:


money=true
type(money)
if money:
    print('OK')
else:
    print('나온다')


# In[2]:


money=true
type(money)
if money:
    print('OK')
else:
    print('나온다')


# In[4]:


money=True
type(money)
if money:
    print('OK')
else:
    print('나온다')


# In[8]:


money=true
print(type(money))
if money:
    print('Yes')
else:
    print('No')


# In[9]:


money=true
print(type(money))
if money:
    print('Yes')
else:
    print('No')


# In[10]:


money=True
print(type(money))
if money:
    print('Yes')
else:
    print('No')


# In[11]:


input('금액 입력:')
money=100
print(type(money))
if money >= 100:
    print('Yes')
else:
    print('No')


# In[12]:


money=input('금액 입력:') #문자열 입력
print(type(money))
if money >= 100: #문자열은 비교 연산 불가능
    print('Yes')
else:
    print('No')


# In[13]:


money=input('금액 입력:') #문자열 입력
print(type(money))
if int(money) >= 100: #문자열은 비교 연산 불가능
    print('Yes')
else:
    print('No')


# In[24]:


num=int(input('점수 입력:'))
if int(num) >= 90 and int(num) <=100: 
    print('수')
elif int(num) >= 80 and int(num) <=90:
    print('우')
elif int(num) >= 70 and int(num) <=80:
    print('미')
else:
    print('No')
print(type(num))


# number=0
# while True:
#     print("무한루프")

# In[ ]:


dd


# In[ ]:


number = 0
while number == 4: #반복문을 빠져나갈 조건
    print("무한루프")


# In[28]:


number = 0
while number !=4: #반복문을 빠져나갈 조건
    number = number + 1
    print(number)


# In[3]:


number = 0
while number !=4: #반복문을 빠져나갈 조건
    print('1.더하기')
    print('2.빼기')
    print('3.곱하기')
    print('4.종료')
    number = int(input("번호>>"))
print('종료!!')


# In[ ]:


number='0'
while number !='4':
    print('1.더하기')
    print('2.빼기')
    print('3.곱하기')
    print('4.종료')
    number = input("번호>>")

    if number == '1':
        num1=int(input('첫번째 숫자:'))
        num2=int(input('두번째 숫자:'))
        print(f"합계: {num1+num2}")
    elif number == '2':
        num1=int(input('첫번째 숫자:'))
        num2=int(input('두번째 숫자:'))
        print(f"차이: {num1-num2}")
    elif number == '3':
        num1=int(input('첫번째 숫자:'))
        num2=int(input('두번째 숫자:'))
        print(f"곱셈: {num1*num2}")
    else:
        print('종료')


# In[ ]:


i = 0 #변수초기화
total = 0 #합계 저장할 변수
while i <=10:
    total = total + i #누적
    i=i+1 #1씩 증가
print(f"합계: {total}")


# In[16]:


i = 0 #변수초기화
tot = 0 #합계 저장할 변수
while i <=10:
    tot += i # #tot = tot + x 누적
    i+=1 # i=i+1 #1씩 증가
print(f"합계: {tot}")


# In[29]:


si=0 #변수초기화
for i in range(1,11):
    si += i
print("합계:",si)


# for i in ['사과','배','바나나']:
#     print(i)

# In[30]:


for i in ['사과', '배', '바나나']:
    print(i)


# In[31]:


for i in (2,10):
    for j in range(1,10):
            print(i,j)


# In[32]:


for i in range(2,10):
    for j in range(1,10):
        print(f"i={i} x j={j} = {i*j}")


# In[37]:


for i in range(2,10):
    for j in range(1,10):

        print(f"i={i} x j={j} = {i*j}", end="\t")
    print('\n')


# In[39]:


prompt = """
    1. 국어 점수 입력
    2. 영어 점수 입력
    3. 수학 점수 입력
    4. 총점 및 평균 출력
    5. 종료

    번호선택>>"""
print(prompt)


# In[ ]:


number='0'
kor=0
eng=0
math=0

prompt = """
    1. 국어 점수 입력
    2. 영어 점수 입력
    3. 수학 점수 입력
    4. 총점 및 평균 출력
    5. 종료

    번호선택>>"""

while number != "5":
    print(prompt)
    number = input("번호>>")

    if number == "1":
        kor=int(input("국어 점수:"))
    elif number == "2":
        eng=int(input("영어 점수:"))
    elif number == "3":
        math=int(input("수학 점수:"))
    elif number == "4":
        total = kor + eng + math
        average = total / 3
        print(f"국:{kor}, 영:{eng}, 수:{math}, 총점: {total}, 평균: {average}")
    elif number == "5":
        print("프로그램을 종료합니다.")
    else:
        print("잘못된 번호입니다. 다시 선택해주세요.")


# In[ ]:


exit()


# In[ ]:




