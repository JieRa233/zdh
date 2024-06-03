from selenium import webdriver
from selenium.webdriver.common.by import By
# 导入Select类
from selenium.webdriver.support.ui import Select
# 导入ActionChains类
from selenium.webdriver.common.action_chains import ActionChains

# 环境变量已经配置
wd = webdriver.Chrome()
# 等待最大时间
wd.implicitly_wait(5)


"""

#更多动作

wd.get('https://www.baidu.com/')
#先实例化
ac = ActionChains(wd)
#调用鼠标移动到元素上，使用find选择一个对象放进去，使用perform()执行动作
ac.move_to_element(wd.find_element(By.CSS_SELECTOR, '[name="tj_briicon"]')).perform()

"""



# 弹出对话框：
# 获取网站
wd.get('https://cdn2.byhy.net/files/selenium/test4.html')

# Alert弹出框，寻找并单击

wd.find_element(By.ID, 'b1').click()
# 打印 弹出框 提示信息
print(wd.switch_to.alert.text)
# 点击 OK 按钮
wd.switch_to.alert.accept()

# Confirm弹出框

# 找到按钮并点击
wd.find_element(By.ID, 'b2').click()
# 打印弹出框提示信息
print(wd.switch_to.alert.text)
# 点击OK按钮
wd.switch_to.alert.accept()
# 找到按钮并点击
wd.find_element(By.ID, 'b2').click()
# 点击取消按钮
wd.switch_to.alert.dismiss()

# Prompt弹出框

# 找到按钮并点击
wd.find_element(By.ID, 'b3').click()
# 获取alert对象
alert = wd.switch_to.alert
# 打印弹出框提示信息
print(alert.text)
# 通过alert对象的方法，输入信息
alert.send_keys('web自动化 - selenium')
# 通过alert对象的方法点击OK按钮
alert.accept()
# 找到按钮并点击
wd.find_element(By.ID, 'b3').click()
alert = wd.switch_to.alert
# 通过alert对象的方法来点击 Cancel 按钮
alert.dismiss()

input('')