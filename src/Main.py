import math
x = math.sqrt(5)
print(hasattr(math,"sqrt"))

def func():
    'this is a test'
    return ""
print(func.__doc__)

name = 'wangmz'
namelist = list(name)
def func1(*p):
    # t = p[0]
    # t[1] = 'z'
    print(p)
func1(namelist,namelist)

def func2(**p):
    print(p)
func2(x = 1 , y =2 , z= 4)

# 函数参数的运用
def story(**kwds):
    return "one parement%(one)s two parement%(two)s"%kwds

def add(x,y,*others):
    if others:
        print("recived number parameter:{}".format(others))
    return pow(x,y)

def interval(start, stop=None, step=1):
    if stop==None:
        start,stop = 0,start
    result = []
    i = start
    while(i<stop):
        result.append(i)
        i+=step
    return result

parameter1 = (2,3)
print(add(*parameter1))
print(add(2,3))
print(add(3,2))
print(add(y=3,x=2))

parameter2 = {'one':'12','two':'13'}
print(story(**parameter2))
print(story(one=12, two=13))

print(interval(5))
print(interval(2,5))
print(interval(2,5,2))
tmp = add(*interval(2,5))
print(tmp)



