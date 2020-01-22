#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-01-22 15:19
# @Author  : Yingqing Shan
# @Site    : 
# @File    : test_fuc_markers.py
# @Software: PyCharm

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


if __name__ == "__main__":
    run_code = 0
