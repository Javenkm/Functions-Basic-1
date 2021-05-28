#1.
def a():
    return 5
print(a())

# My prediction = 5 --- Actual output is 5


#2.
def a():
    return 5
print(a()+a())

# My prediction = 10 --- Actual output is 10


#3.
def a():
    return 5
    return 10
print(a())

# My prediction = 5, 10 --- Actual output is 5


#4.
def a():
    return 5
    print(10)
print(a())

# My prediction = 5 --- Actual output is 5


#5.
def a():
    print(5)
x = a()
print(x)

# My prediction = 5 --- Actual output is 5, None


#6.
def a(b, c):
    print(b+c)
print(a(1, 2) + a(2, 3))

# My prediction = 3, 5 --- Actual output is 3, 5


#7
def a(b,c):
    return str(b)+str(c)
print(a(2,5))

# My prediction is (25) --- Actual output is 25

#8
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a())

# My prediction is 100 --- Actual output is 100, 10

#9
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))

# My prediction is 7, 14, 21 --- Actual output is 7, 14, 21

#10
def a(b,c):
    return b+c
    return 10
print(a(3,5))

# My prediction is 8 --- Actual output is 8

#11
b = 500
print(b)
def a():
    b = 300
    print(b)
print(b)
a()
print(b)

# My prediction is 500, 300, 300, 300 --- Actual output is 500, 500, 300, 500

#12
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
a()
print(b)

# My prediction is 500, 500, 300, 500 --- Actual output is 500, 500, 300, 500

#13
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
b=a()
print(b)

# My predictionis 500, 500, 300, 300 --- Actual output is 500, 500, 300, 300

#14
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()

# My prediction is 1, 2, 3 --- Actual output is 1, 3, 2

#15
def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)

# My prediction is 1, 10, 3, 5, 1 --- Actual output is 1, 3, 5, 10