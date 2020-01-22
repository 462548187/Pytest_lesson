# pytest学习笔记

**安装命令**<br>
```bash
$ pip install pytest
```

**查看已安装列表**<br>
```bash
$ pip list
```

**显示pytest详细信息**<br>
```bash
$ pip show pytest
```

**显示pytest版本信息**<br>
```bash
$ pytest --version
```
**pytest帮助**<br>
```bash
$ pytest --help
```

## 第一个测试

写法加法函数，然后编写改函数的测试方法。

##### test_func.py 文件
```python
def add(x,y):
    return x+y

def test01():
    assert 2 == add(1,1)

def test02():
    assert 2 != add(1,1)
```

```bash
$ pytest --vv test_func.py
or
$ pytest test_func/py
```

##  计算测试时间
计算显示每个测试执行的时间
```bash
$ pytest --durations=0 -vv test_func.py
```

## 测试例外的发生
##### test_func_extend.py
```python
import pytest

def func(x):
    if x == 0:
        raise ValueError("value error!")
    else:
        pass

# func(0)

def test_mytest01():
    with pytest.raises(ValueError):
        func(0)

def test_mytest02():
    assert func(1) == None
```

## 测试例外的发生
##### test_func_paramer.py 文件
```python
import pytest

def add(x, y):
    return x + y

@pytest.mark.parametrize(
    "x,y,expected",
    [
        (1, 1, 2),
        (2, 2, 4),
        (10, 10, 20)
    ]
)
def test_add(x, y, expected):
    assert add(x, y) == expected

```

##分组测试
将测试方法分为不同的测试组，测试时可以单独测试某个组的方法。
```bash
$ pytest --markers
$ nano pytest.ini
...
[pytest]
markers = 
    g1 : group1 .
    g2 : group2 .
...

$ pytest --markets
```

##### test_func_markers.py 文件
```python
import pytest

@pytest.mark.g1
def test_func01():
    pass

@pytest.mark.g2
def test_func02():
    pass

@pytest.mark.g1
def test_func03():
    pass

@pytest.mark.g2
def test_fun04():
    pass

@pytest.mark.g1
def test_func05():
    pass
```

#### Terminal 执行命令
```bash
$ pytest -vv test_func_markers.py
$ pytest -vv -m g1
$ pytest -vv -m g2
```