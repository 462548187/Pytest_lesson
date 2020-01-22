#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-01-22 15:56
# @Author  : Yingqing Shan
# @Site    : 
# @File    : test_fixture01.py
# @Software: PyCharm

import pytest

@pytest.fixture()
def some_data():
    return 42


def test_some_data(some_data):
    assert some_data == 42
