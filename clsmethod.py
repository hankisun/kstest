class Language:
    language = "English"

    def __init__(self):
        self.show = "my language is " + self.language

    @classmethod
    def cls_language(cls):
        return cls()

    @staticmethod
    def static_language():
        return Language()

    def print_language(self):
        print(self.show)


class Derived(Language):
    language = "Korean"


a = Derived()
print(a.language)
a.static_language().print_language()
a.cls_language().print_language()
