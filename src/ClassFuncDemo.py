#coding = utf-8

class Students:
    def __init__(self, number):
        self.number = number
        self.ID_Sequence = []
    def Add(self, id):
        self.ID_Sequence.append(id)
    def __len__(self):
        self.__len__()

    def __repr__(self):
        return str(self.ID_Sequence)

# a = Students(10)
# a.Add(1101)
# b = []
# print(a.ID_Sequence)
# print(a)



class MyArry:
    def __init__(self, start,step):
        self.start = start
        self.step = step
        self.buffer = {}
    def __getitem__(self, item):
        try:
            self.CheckIndex(item)
            return self.buffer[item]
        except KeyError:
            return None
        except IndexError:
            raise IndexError
    def __setitem__(self, key, value):
        try:
            self.CheckIndex(key)
            self.buffer[key] = value
        except TypeError:
            raise TypeError
        except IndexError:
            raise IndexError

    def CheckIndex(self,index):
        if index < 0:
            raise IndexError
        elif not isinstance(index, int):
            raise TypeError

# ary = MyArry(0,1)
# ary[2] = 3
# print(ary[2])

class Mylist(list):
    def __init__(self, *args):
        super(Mylist, self).__init__(*args)
        self.__len = len(*args)
    def method(self):
        print('this is func ',self.__class__)
    @property
    def x(self):
        return self.__len
    @x.setter
    def x(self,value):
        self.__len = value
    @x.deleter
    def x(self):
        del self.__len

# mylist = Mylist('hello')
# print(mylist.x)
# print(mylist)
# mylist.method()

class Mylist2(list):
    def __init__(self, *args):
        super(Mylist2, self).__init__(*args)
        self.__len = len(*args)
    def method(self):
        print('this is func ',self.__class__)
    def __setattr__(self, key, value):
        if key == 'len':
            self.__len = value
        else:
            self.__dict__[key] = value
    def __getattr__(self, item):
        if item == 'len':
            return self.__len
        else:
            raise AttributeError

# mylst = Mylist2('hello')
# print(mylst.len)

class StaticFunc:
    it = 'f'
    def __init__(self, a):
       self.id = a
       self.it = 'g'
    def MemberFunc2(self):
        print('this is ',self.it)
    @staticmethod
    def StcFunc():
        print('this is static method')
    @classmethod
    def MemberFunc(cls):
        print('this is ',cls.it)

tmp = StaticFunc(0)
# print(tmp.it)
# tmp.StcFunc()
# tmp.MemberFunc()
# tmp.MemberFunc2()

# it = iter([1,2,3])
# print(it.__next__())

class TestIter:
    value = 0
    def __init__(self):
        self.value = 0
    def __next__(self):
        self.value += 1
        if self.value > 10:
            raise StopIteration
        # 当函数执行结束时，generator 自动抛出 StopIteration 异常，表示迭代完成。
        # 在 for 循环里，无需处理 StopIteration 异常，循环会正常结束。
        return self.value
    def __iter__(self):
        return self

# testit = TestIter()
# print(list(testit))


lister = [['12','13'],['14',['15','16']],['17']]


def funclist(lister):
    try:
        try:
            lister+' '
        except TypeError:
            pass
        else:
            raise TypeError
        for sublist in lister:
            for element in funclist(sublist):
                yield element
    except TypeError:
        yield lister

# print(list(funclist(lister)))

def reoeater(value):
    while True:
        new = (yield value)
        print('new:',new)
        if new is not None:
            value = new

r = reoeater(42)
r.__next__()
# print(r.__next__())
r.send("hello")
# r.__next__()
# print(r.__next__())

