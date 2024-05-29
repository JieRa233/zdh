from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service #（设置环境变量可不写）

# 创建 WebDriver 对象，指明使用chrome浏览器驱动（设置环境变量可不写路径）
# wd = webdriver.Chrome(service=Service(r'f:\chromedriver\chromedriver.exe'))
wd = webdriver.Chrome()
wd.implicitly_wait(5)
"""

#根据id选择元素

# 调用WebDriver实例对象的get方法 可以让浏览器打开指定网址
wd.get('https://www.byhy.net/_files/stock1.html')
# 根据id选择元素，返回的就是该元素对应的WebElement对象
element = wd.find_element(By.ID, 'kw')
# 通过该 WebElement对象，就可以对页面元素进行操作了
# 比如输入字符串到输入框里
element.send_keys('通讯')   #加上\n就是相当于输入了回车
# 根据id选择元素,选择查询按钮
element = wd.find_element(By.ID, 'go')
# 调用点击方法,点击的位置是按钮的正中心
element.click()
#多次输入需要清理上一次输入的东西
element.clear() # 清除输入框已有的字符串
element.send_keys('科技\n')
#退出
wd.quit()

"""

"""

#根据根据class属性、tag名选择元素

wd.get('https://cdn2.byhy.net/files/selenium/sample1.html')
# 根据class name选择元素，返回的是一个列表
# 里面都是class属性值为animal的元素对应的WebElement对象（find_elements比ID多了一个s）
elements = wd.find_elements(By.CLASS_NAME, 'animal')
# 取出列表中的每个WebElement对象，打印出其text属性的值
# text属性就是该WebElement对象对应的元素在网页中的文本内容
for element in elements:
    print(element.text)  #通过WebElement对象的text属性可以获取该元素在网页中的文本内容。
print("//////////////////////////////////////以下是根据TAG名来寻找的")
#这里使用的是WebDriver对象，寻找范围是整个页面
elements = wd.find_elements(By.TAG_NAME, 'span')
for element in elements:
    print(element.text)
    
"""

"""
#通过WebElement对象选择元素

wd.get('https://cdn2.byhy.net/files/selenium/sample1.html')
#找到ID是container的元素
element = wd.find_element(By.ID,'container')
# WebElement对象选择元素的范围是该元素的内部，这里是限制选择元素的范围是：container元素的内部的TAG
spans = element.find_elements(By.TAG_NAME, 'span')
for span in spans:
    print(span.text)

"""


#等待界面元素出现

#设置等待最长时间,最上面已经设置
#wd.implicitly_wait(10)
wd.get('https://www.byhy.net/_files/stock1.html')
#获取搜索框
element = wd.find_element(By.ID, 'kw')
#输入内容并回车
element.send_keys('通讯\n')
# 返回页面ID为1的元素
element = wd.find_element(By.ID,'1')
print(element.text)







