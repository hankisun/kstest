import pytest

# def func(x):
#     return x+1

# def test_answer():
#     assert func(3) == 4

# def f():
#     raise SystemExit(1)

# def test_mytest():
#     with pytest.raises(SystemExit):
#         f()

# def f2():
#     raise ExceptionGroup(
#         "Group message",
#         [
#             RuntimeError(),
#         ],
#     )

# def test_exception_in_group():
#     with pytest.raises(ExceptionGroup) as exinfo:
#         f2()

#     print(exinfo)
#     print(dir(exinfo))
#     print(exinfo.value)
#     print(exinfo.traceback)
#     print(exinfo.type)
#     print(exinfo.typename)
#     print(exinfo.tb)

#     assert exinfo.group_contains(RuntimeError)
#     assert not exinfo.group_contains(TypeError)

# # test_exception_in_group()


# def setup_function(function):
#     print("setting up", function)

# def test_func1():
#     assert False


# def test_func2():
#     assert False

class Foo:
    @property
    def foo(self):
        return 'something'
    @foo.setter
    def foo(self, value):
        pass

def foo2():
    return Foo.foo + ' special'

def han():
    return 'hannn'

def test_foo(mocker):
    mocker.patch('test_sample.Foo.foo', new_callable=han)
    # this_foo = Foo()
    assert foo2() == han() + ' special'