# QUESTION 1
import time as ti
Seconds= ti.time()
print('The time is epoch is', Seconds)
Seconds=Seconds
local_time= ti.ctime(Seconds)
print('Local time is ',local_time)

#QOUSTION 2
Se= 3**2 +4**2
so=5**2
if Se==so:
    print('Are equal')

# QOUSTION 3 A
def triangle(a,b,c):
    We= a+b
    We2=    c
    return We, We2
v=We=1+4
v2=We2=5
triangle(a=1,b=4,c=5)
if We==We2:
    print('Yes it equal')

# QOUSTION 3 B
'''def triangle(a,b,c):
    We= a+b
    We2=    c
    return We, We2
v=We1=int(input('Input the  number'))
v=We3=int(input('Input the  number'))
We=We1+We3
v2=We2=int(input())
triangle(a=1,b=4,c=5 )
if We==We2:
    print('Yes it equal')'''

# QUESTION 4
import turtle as t
'''t.hideturtle()
t.write('Recurse')
t.penup()
t.goto(45,0)
t.pendown()
t.fd(100)
t.lt(90)
t.fd(50)
t.lt(90)
t.fd(100)
t.lt(90)
t.fd(50)
t.penup()
t.goto(60,0)
t.pendown()
t.write('n=3')
t.penup()
t.goto(45,0)
t.pendown()
t.fd(50)
t.lt(90)
t.fd(100)
t.lt(90)
t.fd(50)
t.lt(90)
t.penup()
t.goto(60,-30)
t.pendown()
t.write('n=2')
t.penup()
t.home()
t.pendown()
t.penup()
t.goto(0,-40)
t.pendown()
t.write('Recurse')
t.penup()
t.home()
t.pendown()
t.penup()
t.goto(45,-100)
t.pendown()
t.fd(100)
t.lt(90)
t.fd(50)
t.lt(90)
t.fd(100)
t.lt(90)
t.fd(50)
t.penup()
t.goto(60,-100)
t.pendown()
t.write('n=1')
t.penup()
t.home()
t.pendown()
t.penup()
t.goto(0,-80)
t.pendown()
t.write('Recurse')
t.penup()
t.home()
t.pendown()
t.penup()
t.goto(45,-150)
t.pendown()
t.fd(100)
t.lt(90)
t.fd(50)
t.lt(90)
t.fd(100)
t.lt(90)
t.fd(50)
t.penup()
t.goto(60,-150)
t.pendown()
t.write('n=0')
t.penup()
t.home()
t.pendown()
t.penup()
t.goto(0,-130)
t.pendown()
t.write('Recurse')
t.done()'''
# QOUSTION 5
def draw(t, length, n):
 if n == 0:
   return
 angle = 50
 t.fd(length*n)
 t.lt(50)
 draw(t, length, n-1)
 t.rt(2*50)
 draw(t, length, n-1)
 t.lt(50)
 t.bk(length*n)
 return
draw(t,10,5)









