# selenium元素定位

from selenium import webdriver          # 导入浏览器驱动


driver = webdriver.Chrome()             # 初始化
driver.get('https://www.baidu.com')     # 打开百度首页

# 通过id定位
element = driver.find_element_by_id("kw")
print(element)

# 通过name定位
element = driver.find_element_by_name("wd")
print(element)

# 通过class name定位
element = driver.find_element_by_class_name("s_ipt")
print(element)

# 通过tag name定位
element = driver.find_element_by_tag_name("input")
print(element)

# 通过xpath定位
element = driver.find_element_by_xpath("//*[@id='kw']")
print(element)

# 通过css定位
element = driver.find_element_by_css_selector("#kw")
print(element)


print(driver.title)                     # 打印网页标题
driver.quit()                           # 关闭浏览器
