
import sys

import pytest
import yaml

sys.path.append('..')
print(sys.path)
from pythoncode.Calculator import Calculator


def get_datas():
    with open("./datas/calc.yml") as f:
        datas = yaml.safe_load(f)
    return (datas['add']['datas'], datas['add']['ids'],datas['div']['datas'], datas['div']['ids'])

# yaml json excel csv xml
# 测试类
class TestCalc:
    datas: list = get_datas()

    # 前置条件
    def setup_class(self):
        print("开始计算")
        self.calc = Calculator()

    # 后置条件
    def teardown_class(self):
        print("结束计算")


    # 加法
    @pytest.mark.parametrize("a, b, result", datas[0], ids=datas[1])
    def test_add(self, a, b, result):
        print(f"a={a} , b ={b} ,result={result}")
        assert result == self.calc.add(a, b)

    # 除法
    @pytest.mark.parametrize("a, b, result", datas[2], ids=datas[3])
    def test_div(self, a, b, result):
        if b == 0:
            try:
                self.calc.div(a, b)
            except ZeroDivisionError as e:
                print('除数不能为0')
        else:
            print(f"a={a} , b ={b} ,result={result}")
            assert result == self.calc.div(a, b)