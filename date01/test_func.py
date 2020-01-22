# coding = utf-8
def add(x, y):
    return x + y


def test01():
    assert 2 == add(1, 1)


def test02():
    assert 3 != add(1, 1)


