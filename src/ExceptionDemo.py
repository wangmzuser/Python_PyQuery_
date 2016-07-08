#coding utf- 8

class MyException(NameError):
    def __init__(self, arg):
        self.arg = arg

def func(i):
    if i<1:
        raise MyException("Error")


try:
    func(0)                    #正常逻辑
except (NameError, Exception) as e:
    print(e)                #触发异常的处理
    # raise
else:
    print('22')                #不出现异常的处理
finally:
    print('33')                #最后收尾（无论是否触发异常，这里都会处理）

