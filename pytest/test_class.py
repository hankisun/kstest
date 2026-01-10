import pytest

class Item:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    

class TestClass:
    def test_one(self):
        x = 'this'
        assert 'h' in x

    def test_two(self):
        x = 'hello'
        assert hasattr(x, 'hello')

    @pytest.mark.parametrize("n,expected", [(1, 2), (3, 4)])
    def test_simple_case(self, n, expected):
        assert n + 1 == expected

    @pytest.mark.parametrize("n,expected", [(1, 2), (3, 4)])
    def test_weird_simple_case(self, n, expected):
        assert (n * 1) + 1 == expected

    @pytest.mark.parametrize('item', 
                             [Item('han', 30),
                              Item('jung', 20)])
    def test_item(self):
        # item = Item('han', 30)
        assert 'han' == item.name
        assert 30 == item.age
