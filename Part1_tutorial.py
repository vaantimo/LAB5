Python 3.12.1 (v3.12.1:2305ca5144, Dec  7 2023, 17:23:38) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #A: if statements
>>> x = 2
>>> if x < 3:
...     print("Small")
... 
...     
Small
>>> X = 5
>>> if x < 3:
...     print("Small")
... 
...     
Small
>>> 
>>> score = 8 #A score on a 10 point quiz
>>> if score > 6:
...     print("Nice work!")
... 
...     
Nice work!
>>> 
>>> for i in range(1,16):
...     if i % 3 == 0:
...         print(i, "is divisble by 3.")
... 
...         
3 is divisble by 3.
6 is divisble by 3.
9 is divisble by 3.
12 is divisble by 3.
15 is divisble by 3.
>>> 
>>> for i in range(1,10):
...     if i % 2 == 0:
...         print(i, "is even.")
... 
...         
2 is even.
4 is even.
6 is even.
8 is even.

#B: elif and else Statements

x = 2
if x < 3:
    print("Small")
else:
    print("Large")

    
Small

x = 5
if x < 3:
    print("Small")
else:
    print("Large")

    
Large

score = 8 #A score on a 10 point quiz
if score < 6:
    print("Needs improvement")
elif score < 9:
    print("Nice work!")
else:
    print("Excellent!")

    
Nice work!

for i in range(-2,3):
    if i < 0:
        print(i, "is negative.")
elif i == 0:
    
SyntaxError: invalid syntax
elif i == 0:
    
SyntaxError: invalid syntax

for i in range(-2,3):
    if i < 0:
        print(i, "is negative.")
    elif i == 0:
        print(i, "is zero.")
    else:
        print(i, "is positive.")

        
-2 is negative.
-1 is negative.
0 is zero.
1 is positive.
2 is positive.

for i in range(1,20):
    if i % 2 == 0:
        print(i, "is even.")
    else:
        print(i, "is odd.")

        
1 is odd.
2 is even.
3 is odd.
4 is even.
5 is odd.
6 is even.
7 is odd.
8 is even.
9 is odd.
10 is even.
11 is odd.
12 is even.
13 is odd.
14 is even.
15 is odd.
16 is even.
17 is odd.
18 is even.
19 is odd.

print(3 < 4)
True
print(4 > 2)
True
type(True)
<class 'bool'>

if True:
    print("This text will always appear.")
if False:
    
SyntaxError: invalid syntax
if False:
    print("This text will not appear.")

    
type(False)
<class 'bool'>
print(3 == 5)
False

def the_number(n):
    if n > 10:
        return True
    else:
        return False

    
the_number(13)
True
