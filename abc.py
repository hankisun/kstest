import abc


class BaseClass(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def study(self):
        pass

    @abc.abstractmethod
    def go_to_school(self):
        pass


class Students(BaseClass):
    def study(self):
        print("Students > study()")

    def go_to_school(self):
        print("Students > go_to_school")


jim = Students()
jim.study()
