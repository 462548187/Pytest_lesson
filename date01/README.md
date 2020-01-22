# pytest学习笔记

**安装命令**<br>
```bash
$pip install pytest
```

**查看已安装列表**<br>
```bash
$pip list
```

**显示pytest详细信息**<br>
```bash
$pip show pytest
```

**显示pytest版本信息**<br>
```bash
$pytest --version
```
**pytest帮助**<br>
```bash
$pytest --help
```

### 第一个测试

写法加法函数，然后编写改函数的测试方法。

#### test_func.py
```python
def add(x,y):
    return x+y

def test01():
    assert 2 == add(1,1)

def test02():
    assert 2 != add(1,1)
```

```bash
$pytest --vv test_func.py
or
$pytest test_func/py
```
