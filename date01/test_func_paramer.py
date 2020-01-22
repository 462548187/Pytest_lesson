#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-01-22 12:37
# @Author  : Yingqing Shan
# @Site    : 
# @File    : test_func_paramer.py.py
# @Software: PyCharm

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


if __name__ == "__main__":
    run_code = 0
