from abc import ABC
from abc import abstractmethod


class Template(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def func1(self):
        pass

    @abstractmethod
    def func2(self):
        pass

    @staticmethod
    def comm_func():
        print("Run f1, f2")

    def execute(self):
        self.comm_func()
        self.func1()
        self.func2()


class TemplateImpl_1(Template):
    def func1(self):
        print("TemplateImpl_1 > func1 called")

    def func2(self):
        print("TemplateImpl_1 > func2 called")


class TemplateImpl_2(Template):
    def func1(self):
        print("TemplateImpl_2 > func1 called")

    def func2(self):
        print("TemplateImpl_2 > func2 called")


print()
t_impl1 = TemplateImpl_1()
# help(t_impl1)
t_impl1.execute()
print()
t_impl2 = TemplateImpl_2()
# help(t_impl2)
t_impl2.execute()
