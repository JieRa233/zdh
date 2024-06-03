from selenium import webdriver
from selenium.webdriver.common.by import By
# 导入Select类
from selenium.webdriver.support.ui import Select
#环境变量已经配置
wd = webdriver.Chrome()
wd.implicitly_wait(5)

"""
#根据id属性选择元素

wd.get('https://cdn2.byhy.net/files/selenium/sample1.html')
#选择searchtext这个ID的元素
element = wd.find_element(By.CSS_SELECTOR, '#searchtext')
#这个元素是个输入框，可以进行输入
element.send_keys('你好')
#选择所有class属性值为animal的元素动物
#elements = wd.find_elements(By.CLASS_NAME, 'animal')  #同下
elements = wd.find_elements(By.CSS_SELECTOR, '.animal')
for element in elements:
    print(element.text)

wd.quit()

"""


"""

#选择 子元素 和 后代元素

wd.get('https://cdn2.byhy.net/files/selenium/sample1.html')
#选择ID为container的直接子元素div
elements = wd.find_elements(By.CSS_SELECTOR, '#container > div')
for element in elements:
    print('-----------------------------------------')
    print(element.get_attribute('outerHTML'))   #获取整个元素对应的HTML文本内容
    
"""


"""

#根据属性选择

wd.get('https://cdn2.byhy.net/files/selenium/sample1.html')
# 根据属性选择元素,使用[]括起来，等号前写名字，如果名字唯一，可省略等号后面
element = wd.find_element(By.CSS_SELECTOR, '[href="http://www.miitbeian.gov.cn"]')
# 打印出元素对应的html
print(element.get_attribute('outerHTML'))

"""


"""

#切换到frame（页面嵌套）

wd.get('https://cdn2.byhy.net/files/selenium/sample2.html')
# 先根据name属性值 'innerFrame'，切换到iframe中,如果像ID/NAME这些属性都没有,可以填写frame所对应的WebElement对象
#wd.switch_to.frame(wd.find_element(By.CSS_SELECTOR,'[src="sample1.html"]'))
wd.switch_to.frame('innerFrame')   #这是frame的name
#根据class name选择元素，返回的是 一个列表
elements = wd.find_elements(By.CLASS_NAME,'plant')
for element in elements:
    print(element.text)
#注意切回外层再执行其它的
wd.switch_to.default_content()
elements = wd.find_elements(By.CSS_SELECTOR,'span')
for element in elements:
    print(element.text)
wd.quit()

"""

"""

#切换窗口

wd.get('https://cdn2.byhy.net/files/selenium/sample3.html')
print(wd.title)
# mainWindow变量保存当前窗口的句柄
mainWindow = wd.current_window_handle
# 点击打开新窗口的链接
link = wd.find_element(By.TAG_NAME, "a")
link.click()
for handle in wd.window_handles:
    # 先切换到该窗口
    wd.switch_to.window(handle)
    # 得到该窗口的标题栏字符串，判断是不是我们要操作的那个窗口
    if 'Bing' in wd.title:
        # 如果是，那么这时候WebDriver对象就是对应的该该窗口，正好，跳出循环，
        break
# wd.title属性是当前窗口的标题栏文本
print(wd.title)
#通过前面保存的老窗口的句柄，自己切换到老窗口
wd.switch_to.window(mainWindow)
print(wd.title)
wd.find_element(By.ID,'outerbutton').click()

input('')

"""


"""

#选择框

#radio：

wd.get('https://cdn2.byhy.net/files/selenium/test2.html')
# 获取当前选中的元素，选择checked是“checked”状态的元素，checked对radio和checkbox类型的input有效
element = wd.find_element(By.CSS_SELECTOR,'#s_radio input[name="teacher"]:checked')
#打印选择元素中的内容
print('当前选中的是: ' + element.get_attribute('value'))
# 点选小雷老师
wd.find_element(By.CSS_SELECTOR,'#s_radio input[value="小雷老师"]').click()

#checkbox框：

# 先把已经选中的选项全部点击一下,这里要加s,他们的checked值都是‘checked’
elements = wd.find_elements(By.CSS_SELECTOR, '#s_checkbox input[name="teacher"]:checked')
for element in elements:
    element.click()
# 再点击小雷老师
wd.find_element(By.CSS_SELECTOR, "#s_checkbox input[value='小雷老师']").click()

#select单选框：

# 创建Select对象，通过查找ID的方式
select = Select(wd.find_element(By.ID, "ss_single"))
# 通过 Select 对象选中小雷老师
select.select_by_visible_text("小雷老师")

#select多选框：
# 创建Select对象,通过查找ID的方式
select = Select(wd.find_element(By.ID, "ss_multi"))
# 清除所有已经选中的选项
select.deselect_all()
# 选择小雷老师 和 小凯老师
select.select_by_visible_text("小雷老师")
select.select_by_visible_text("小凯老师")

input('')

"""




#








