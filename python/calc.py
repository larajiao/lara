# coding:utf-8
# 日期： 2020-05-09 10:29   
# 作者: 焦硕 
# PyCharm   


class Calc:
    def add(self, a, b):
        return a + b

    def div(self, a, b):
        result = a / b
        return result



if __name__ == '__main__':
    print(Calc().div(3.5, 7))
