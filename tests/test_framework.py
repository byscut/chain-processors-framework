#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/28 3:09 下午
# @File    : test_framework.py
# @author  : Bai
# @Software: PyCharm
import unittest
from chain_processors.run_example import Runner


class TestProcessor(unittest.TestCase):

    def test1(self):
        model = Runner()
        result = model.predict(['1010111'])
        self.assertEqual(['1010111 - 自定义的字符串 - 自定义的字符串 - 自定义的字符串'], result)

