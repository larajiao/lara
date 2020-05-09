# coding:utf-8
# 日期： 2020-05-09 10:29   
# 作者: 焦硕 
# PyCharm   


import pytest
from python.calc import *

"""
等价类：有效等价类，整数、浮点数、负数相加或相除
       有效等价类，字母
"""

class TestCalc:
    @pytest.mark.parametrize("a,b,expected", [(97, 13, 110), (34.5, 23.3, 57.8), (-23, -34, -57),
                                              ('a', 'b', 'ab'), ([1, 2, 3], [4, 5, 6], [1, 2, 3, 4, 5, 6])])
    def test_add1(self, a, b, expected):
        self.calc = Calc()
        result = self.calc.add(a, b)
        assert result == expected

    @pytest.mark.parametrize("a,b,expected", [(5, 5, 1), (5, 0, '除数不能为0'), (-5, -4, 1.25), (3.5, 7, 0.5)])
    def test_div1(self, a, b, expected):
        if b != 0:
            self.calc = Calc()
            result = self.calc.div(a, b)
            assert result == expected
        else:
            print("b等于0，不符合除法规则")


if __name__ == '__main__':
    pytest.main(['-vs', 'test_calc.py'])
