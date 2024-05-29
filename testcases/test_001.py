#pytest用例风格一般使用函数或方法形式
import pytest


#函数方式
#形参中加上exe_mysql来使用这个fixture
def test_login01(exe_mysql):
    print("函数方式登录01")

@pytest.mark.skip(reason="无条件跳过1")
def test_login02():
    print("函数方式登录01")

@pytest.mark.skipif(3>2,reason="满足条件跳过")
def test_login03():
    print("函数方式登录01")

@pytest.mark.xfail(reason="应该失败的用例")
def test_login04():
    0/1
    print("函数方式登录01")


#方法形式
#一个“（）”代表一组数据
@pytest.mark.parametrize(["username","password"],[(1,2),(44,55),(77,88)])
@pytest.mark.run(order=1)  #设置优先级，越小越优先
class TestLogin:
    def test_login05(self,username,password):
        print("方法形式登录02")
#记得将参数传递给函数
#形参中加上exe_mysql来使用这个fixture
    def test_login06(self,username,password,exe_mysql):
        print("方法形式登录03")
        print(f"输入用户名:{username}")
        print(f"输入用户名:{password}")


