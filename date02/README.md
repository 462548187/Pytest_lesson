# pytest_fixture 框架入门

## fixture 提供数据源
##### test_fixture.py

```python
import pytest

@pytest.fixture()
def some_data():
    return 42

def test_some_data(some_data):
    assert some_data == 42

```