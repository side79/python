# class foo:
#     bar = True
    
#     def echo_name(self):
#         print(self.__class__.__name__)

#     @classmethod
#     def echo_name_2(cls):
#         print(cls.__name__)
    
#     #no args get, useless metod
#     @staticmethod
#     def ehco_name_3():
#         print(foo.__name__)


# f = foo()
# print(foo, foo.__class__)
# print(f, f.__class__)

# print('echo_name: ',f.echo_name())
# print('echo_name_2: ',f.echo_name_2())
# print('echo_name_3: ',f.ehco_name_3())

# print(f.bar, foo.bar)
# f.bar = False
# print(f.bar, foo.bar)

# f.bar = True

# foo.bar = False
# f2 = foo()

# print('f.bar: ', f.bar, 'foo.bar: ', foo.bar, 'f2.bar: ', f2.bar)


def test_fun(klass):
    f = klass()
    print(klass, klass.__class__, type(klass))
    print(f, f.__class__, type(f))
    
    print('class:', klass.echo_name())
    print('instans:', f.echo_name())
    
    print(klass.bar, f.bar)
    f.bar = False
    print(klass.bar, f.bar)
    
    f.bar = True
    klass.bar = False
    f2 = klass()
    print(klass.bar, f.bar, f2.bar)

@classmethod
def echo_name(cls):
    print(cls.__name__)
    
def echo_bar(self):
    print(self.bar)


# Foo = type('Foo', (), {'bar': True, 'echo_name': echo_name, 'echo_bar': echo_bar})

# # print(Foo)

# # test_fun(Foo)

# NewFoo = type('NewFoo', (Foo, ), {'spam':'eggs'})

# print(NewFoo)
# fn = NewFoo()
# print(fn)
# print(fn.spam)


class MyMettaclass(type):
    def __new__(cls, name, bases, dct, *args, **kwargs):
        
        print('New class', name)
        print('Bases:', bases)
        #print('New attrs:', dct)
        dct['SPAM'] = 'EGGS'
        #print('New attrs_2:', dct)
        
        for k in list(dct.keys()):
            if k.startswith('_'):
                v = dct.pop(k)
                dct[k.upper()] = v

        new_cls = super().__new__(cls, name, bases, dct, *args, **kwargs)
        # class new_cls:
        #     bar = True

        # print('created new cls:', new_cls)
        return new_cls
    
    
class Foo(metaclass = MyMettaclass):
    bar = True
    _secret_attr = 'secret value'
    
    @classmethod
    def echo_name(cls):
        print(cls.__name__)
        
    def echo_bar(self):
        print(self.bar)
    
class NewFoo(Foo):
    spam = 'eggs'
    
# test_fun(Foo)

# Foo = MyMettaclass('Foo', (), {})

# NewFoo = MyMettaclass('NewFoo', (Foo, ), {'spam':'eggs'})

print(Foo.SPAM)
print(NewFoo.SPAM)

print(Foo._SECRET_ATTR)