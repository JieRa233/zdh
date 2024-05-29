import pytest

#创建一个fixture来完成用例的前后置操作
#设置级别为函数级别，所有用例手动调用
@pytest.fixture(scope="function")
def exe_mysql():
    #前置操作
    print("连接数据库，获取数据")
    yield
    #后置操作
    print("关闭数据库")